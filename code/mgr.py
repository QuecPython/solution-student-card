# Copyright (c) Quectel Wireless Solution, Co., Ltd.All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import osTimer, sim, net, utime, modem
from usr.common import Abstract, LogAdapter
from misc import USB, Power, ADC
from machine import ExtInt, Pin
from usr import EventMesh
import audio
from machine import RTC

BATTERY_OCV_TABLE = {
    "nix_coy_mnzo2": {
        55: {
            4152: 100, 4083: 95, 4023: 90, 3967: 85, 3915: 80, 3864: 75, 3816: 70, 3773: 65, 3737: 60, 3685: 55,
            3656: 50, 3638: 45, 3625: 40, 3612: 35, 3596: 30, 3564: 25, 3534: 20, 3492: 15, 3457: 10, 3410: 5, 3380: 0,
        },
        20: {
            4143: 100, 4079: 95, 4023: 90, 3972: 85, 3923: 80, 3876: 75, 3831: 70, 3790: 65, 3754: 60, 3720: 55,
            3680: 50, 3652: 45, 3634: 40, 3621: 35, 3608: 30, 3595: 25, 3579: 20, 3548: 15, 3511: 10, 3468: 5, 3430: 0,
        },
        0: {
            4147: 100, 4089: 95, 4038: 90, 3990: 85, 3944: 80, 3899: 75, 3853: 70, 3811: 65, 3774: 60, 3741: 55,
            3708: 50, 3675: 45, 3651: 40, 3633: 35, 3620: 30, 3608: 25, 3597: 20, 3585: 15, 3571: 10, 3550: 5, 3500: 0,
        },
    },
}


class Battery(object):
    """This class is for battery info.

    This class can get battery voltage and energy.
    if adc_args is not None, use cbc to read battery

    adc_args: (adc_num, adc_period, factor)

        adc_num: ADC channel num
        adc_period: Cyclic read ADC cycle period
        factor: calculation coefficient
    """

    def __init__(self, adc_args=None, chrg_gpion=None, stdby_gpion=None):
        self.__energy = 100
        self.__temp = 20

        # ADC params
        self.__adc = None
        if adc_args:
            self.__adc_num, self.__adc_period, self.__factor = adc_args
            if not isinstance(self.__adc_num, int):
                raise TypeError("adc_args adc_num is not int number.")
            if not isinstance(self.__adc_period, int):
                raise TypeError("adc_args adc_period is not int number.")
            if not isinstance(self.__factor, float):
                raise TypeError("adc_args factor is not int float.")
            self.__adc = ADC()

        # Charge params
        self.__charge_callback = None
        self.__charge_status = None
        self.__chrg_gpion = chrg_gpion
        self.__stdby_gpion = stdby_gpion
        self.__chrg_gpio = None
        self.__stdby_gpio = None
        self.__chrg_exint = None
        self.__stdby_exint = None
        if self.__chrg_gpion is not None and self.__stdby_gpion is not None:
            self.__init_charge()

    def __chrg_callback(self, args):
        self.__update_charge_status()
        if self.__charge_callback is not None:
            self.__charge_callback(self.__charge_status)

    def __stdby_callback(self, args):
        self.__update_charge_status()
        if self.__charge_callback is not None:
            self.__charge_callback(self.__charge_status)

    def __update_charge_status(self):
        if self.__chrg_gpio.read() == 1 and self.__stdby_gpio.read() == 1:
            self.__charge_status = 0
        elif self.__chrg_gpio.read() == 0 and self.__stdby_gpio.read() == 1:
            self.__charge_status = 1
        elif self.__chrg_gpio.read() == 1 and self.__stdby_gpio.read() == 0:
            self.__charge_status = 2
        else:
            raise TypeError("CHRG and STDBY cannot be 0 at the same time!")

    def __init_charge(self):
        self.__chrg_gpio = Pin(self.__chrg_gpion, Pin.IN, Pin.PULL_DISABLE)
        self.__stdby_gpio = Pin(self.__stdby_gpion, Pin.IN, Pin.PULL_DISABLE)
        self.__chrg_exint = ExtInt(self.__chrg_gpion, ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, self.__chrg_callback)
        self.__stdby_exint = ExtInt(self.__stdby_gpion, ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU,
                                    self.__stdby_callback)
        self.__chrg_exint.enable()
        self.__stdby_exint.enable()
        self.__update_charge_status()

    def __get_soc_from_dict(self, key, volt_arg):
        """Get battery energy from map"""
        if key in BATTERY_OCV_TABLE["nix_coy_mnzo2"]:
            volts = sorted(BATTERY_OCV_TABLE["nix_coy_mnzo2"][key].keys(), reverse=True)
            pre_volt = 0
            volt_not_under = 0  # Determine whether the voltage is lower than the minimum voltage value of soc.
            for volt in volts:
                if volt_arg > volt:
                    volt_not_under = 1
                    soc1 = BATTERY_OCV_TABLE["nix_coy_mnzo2"][key].get(volt, 0)
                    soc2 = BATTERY_OCV_TABLE["nix_coy_mnzo2"][key].get(pre_volt, 0)
                    break
                else:
                    pre_volt = volt
            if pre_volt == 0:  # Input Voltarg > Highest Voltarg
                return soc1
            elif volt_not_under == 0:
                return 0
            else:
                return soc2 - (soc2 - soc1) * (pre_volt - volt_arg) // (pre_volt - volt)

    def __get_soc(self, temp, volt_arg, bat_type="nix_coy_mnzo2"):
        """Get battery energy by temperature and voltage"""
        if bat_type == "nix_coy_mnzo2":
            if temp > 30:
                return self.__get_soc_from_dict(55, volt_arg)
            elif temp < 10:
                return self.__get_soc_from_dict(0, volt_arg)
            else:
                return self.__get_soc_from_dict(20, volt_arg)

    def __get_power_vbatt(self):
        return int(sum([Power.getVbatt() for i in range(100)]) / 100)

    def __get_adc_vbatt(self):
        self.__adc.open()
        utime.sleep_ms(self.__adc_period)
        adc_list = list()
        for i in range(self.__adc_period):
            adc_list.append(self.__adc.read(self.__adc_num))
            utime.sleep_ms(self.__adc_period)
        adc_list.remove(min(adc_list))
        adc_list.remove(max(adc_list))
        adc_value = int(sum(adc_list) / len(adc_list))
        self.__adc.close()
        vbatt_value = adc_value * (self.__factor + 1)
        return vbatt_value

    def set_temp(self, temp):
        """Set now temperature."""
        if isinstance(temp, int) or isinstance(temp, float):
            self.__temp = temp
            return True
        return False

    def get_voltage(self):
        """Get battery voltage"""
        if self.__adc is None:
            return self.__get_power_vbatt()
        else:
            return self.__get_adc_vbatt()

    def get_energy(self):
        """Get battery energy"""
        self.__energy = self.__get_soc(self.__temp, self.get_voltage())
        return self.__energy

    def set_charge_callback(self, charge_callback):
        if self.__chrg_gpion is not None and self.__stdby_gpion is not None:
            if callable(charge_callback):
                self.__charge_callback = charge_callback
                return True
        return False

    def get_charge_status(self):
        return self.__charge_status


class BatteryManager(Abstract):
    def __init__(self):
        """电池管理器"""
        self.battery = Battery()
        self.low_battery = False

    def post_processor_after_instantiation(self):
        """订阅此类所有的事件到 EventMesh中"""
        EventMesh.subscribe("get_battery", self.get_battery)

    def get_battery(self, event=None, msg=None):
        battery = self.battery.get_energy()
        return battery


class DeviceInfoManager(Abstract):
    """
        设备信息管理
    """

    def __init__(self):
        self.__city = None
        self.__location = None
        self.timer_push_schedule = osTimer()
        self.usb = USB()
        self.battery_push_schedule = osTimer()
        self.check_battery_list = []
        self.__bat_num = 0
        self.usb.setCallback(self.usb_event_cb)
        self.log = LogAdapter(self.__class__.__name__)
        self.rtc = RTC()
        self.adc = ADC()

    def post_processor_after_instantiation(self):
        """订阅此类所有的事件到 EventMesh中"""
        EventMesh.subscribe("screen_get_ope", self.get_device_ope)
        EventMesh.subscribe("screen_get_sig", self.get_signal)
        EventMesh.subscribe("screen_get_time", self.get_time)
        EventMesh.subscribe("about_get_imei", self.get_imei)
        EventMesh.subscribe("about_get_iccid", self.get_ic_cid)
        EventMesh.subscribe("about_get_phonenum", self.get_phone_num)
        EventMesh.subscribe("screen_get_battery", self.get_battery)
        EventMesh.subscribe("get_fw_version", self.get_device_fw_version)
        EventMesh.subscribe("get_standby_time", self.get_standby_time)
        EventMesh.subscribe("sim_slot_get", self.sim_slot_get)
        EventMesh.subscribe("sim_slot_switch", self.sim_slot_switch)
        self.timer_push_schedule.start(20000, 1, self.publish_event)
        # self.battery_push_schedule.start(3000, 1, self.__check_battery)
        self.log.debug("post_processor_after_instantiation finished")
        # 设备开机立刻更新一次参数
        self.publish_event()

    # def __check_battery(self, *args):
    #     self.check_battery_list.append(EventMesh.publish("get_battery"))
    #     if len(self.check_battery_list) > 2:
    #         check_battery_list = self.check_battery_list.copy()
    #         check_battery_list.remove(min(self.check_battery_list))
    #         check_battery_list.remove(max(self.check_battery_list))
    #         _bat = sum(check_battery_list) / len(check_battery_list)
    #         if len(self.check_battery_list) > 20:
    #             self.check_battery_list = self.check_battery_list[1:]
    #         self.__bat_num = _bat
    #     else:
    #         return EventMesh.publish("get_battery")

    def publish_event(self, *args, **kwargs):
        """
        主动推送事件
        :param args:
        :param kwargs:
        :return:
        """
        EventMesh.publish("time", self.get_time())
        EventMesh.publish("battery", self.get_battery())
        EventMesh.publish("signal", self.get_signal())

    def get_device_ope(self, event, msg):
        """
        获取设备运营商信息
        :param event:
        :param msg:
        :return: 运营商
        """
        net_ope_map = {
            "UNICOM": "中国联通HD",
            "CMCC": "中国移动HD",
            "CT": "中国电信HD"
        }
        """获取运营商"""
        try:
            short_eons = net.operatorName()[1]
        except Exception:
            return "无"
        return net_ope_map.get(short_eons, None)

    def get_signal(self, event=None, msg=None):
        """
        获取信号事件
        :param event:
        :param msg:
        :return: int 类型
        """
        return net.csqQueryPoll()

    def get_time_bucket(self, time):
        if time < 12:
            return '上午'
        else:
            return '下午'
        # if time >= 0 and time < 5:
        #     return '凌晨'
        # elif time >= 5 and time < 8:
        #     return '早晨'
        # elif time >= 8 and time < 11:
        #     return '上午'
        # elif time >= 11 and time < 13:
        #     return '中午'
        # elif time >= 13 and time < 16:
        #     return '下午'
        # elif time >= 16 and time < 19:
        #     return '傍晚'
        # else:
        #     return '晚上'

    def get_week(self, week):
        if week == 1:
            return '一'
        elif week == 2:
            return '二'
        elif week == 3:
            return '三'
        elif week == 4:
            return '四'
        elif week == 5:
            return '五'
        elif week == 6:
            return '六'
        elif week == 7 or week == 0:
            return '日'

    def get_time(self, event=None, msg=None):
        """
        获取时间事件
        :param event:
        :param msg:
        :return: HH:MM 格式
        """
        rtc_time = self.rtc.datetime()
        date = ("%02d-%02d 星期%s" % (rtc_time[1], rtc_time[2], self.get_week(rtc_time[3])))
        time = ("%02d:%02d" % (rtc_time[4], rtc_time[5]))
        time_quantum = ("%s" % (self.get_time_bucket(rtc_time[4])))

        result = [time, time_quantum, date]
        return result

    def get_imei(self, event, msg):
        """
        获取imsi号s事件
        :param event:
        :param msg:
        :return: str imsi
        """
        return modem.getDevImei()

    def get_ic_cid(self, event, msg):
        """
        获取ic cid事件
        :param event:
        :param msg:
        :return: str ic cid
        """
        return sim.getIccid()

    def get_phone_num(self, event, msg):
        """
        获取电话号码事件
        :param event:
        :param msg:
        :return: str number
        """
        return sim.getPhoneNumber()

    def get_battery(self, event=None, msg=None):
        """
        获取电池事件,暂时没支持
        :param event:
        :param msg:
        :return:
        """

        charge_state = '0'
        if self.get_usb_state() == 1:
            charge_state = '1'
        else:
            charge_state = '0'

        vbat = ""
        self.adc.open()
        temp = self.adc.read(ADC.ADC0)
        self.adc.close()
        temp = temp * 4

        if temp <= 3500:
            vbat = "U:/static/vbat_20.png"
        elif temp <= 3600:
            vbat = "U:/static/vbat_40.png"
        elif temp <= 3800:
            vbat = "U:/static/vbat_60.png"
        elif temp <= 4000:
            vbat = "U:/static/vbat_80.png"
        else:
            vbat = "U:/static/vbat_100.png"

        result = [charge_state, vbat]

        return result

    def get_device_fw_version(self, *args):
        '''
        获取设备固件版本号
        '''
        fw_version = modem.getDevFwVersion()
        if isinstance(fw_version, str):
            return fw_version
        return "--"

    def get_standby_time(self, *args):
        '''
        获取设备单次开机待机时间
        '''
        time_msg = utime.time()
        d = int(
            time_msg / 86400)  # The int call removes the decimals.  Conveniently, it always rounds down.  int(2.9) returns 2 instead of 3, for example.
        time_msg -= (
                d * 86400)  # This updates the value of x to show that the already counted seconds won't be double counted or anything.
        h = int(time_msg / 3600)
        time_msg -= (h * 3600)
        m = int(time_msg / 60)
        time_msg -= (m * 60)
        s = time_msg
        result = "{}天{}小时{}分".format(d, h, m)
        return result

    def sim_slot_get(self, topic=None, msg=None):
        return sim.getCurSimid()

    def sim_slot_switch(self, topic=None, slot=None):
        """
        sim 卡槽切换
        :param topic:
        :param slot:
        :return: 切换sim卡卡槽  0 切换成功, 1 无需切换, -1 切换失败
        """
        if self.sim_slot_get() == slot:
            return 1
        else:
            return sim.switchCard(slot)

    def usb_event_cb(self, state):
        EventMesh.publish("battery", self.get_battery())

    def get_usb_state(self):
        state = self.usb.getStatus()
        if state == -1:
            state = 0
        return state


class MediaManager(Abstract):
    def __init__(self):
        self.aud = audio.Audio(0)
        self.tts = audio.TTS(0)
        self.tts.setVolume(1)

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("push_add_device_voice", self.add)
        EventMesh.subscribe("push_reduce_device_voice", self.reduce)
        EventMesh.subscribe("get_device_voice", self.get)

    def add(self, event, msg):
        vo = self.get() + 1
        self.aud.setVolume(vo)

    def reduce(self, event, msg):
        vo = self.get() - 1
        self.aud.setVolume(vo)

    def get(self, event=None, msg=None):
        return self.aud.getVolume()


class BrightNessLevelManager(Abstract):
    def __init__(self):
        self.level = 0

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("push_add_brightness_level", self.add)
        EventMesh.subscribe("push_reduce_brightness_level", self.reduce)
        EventMesh.subscribe("get_brightness_level", self.get)

    def add(self, event, msg):
        if self.level < 4:
            self.level = self.level + 1

    def reduce(self, event, msg):
        if self.level > 0:
            self.level = self.level - 1

    def get(self, event=None, msg=None):
        return self.level


class TimeModeManager(Abstract):
    def __init__(self):
        self.mode = 0

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("push_time_mode", self.set)
        EventMesh.subscribe("get_time_mode", self.get)

    def get(self, event=None, msg=None):
        return self.mode

    def set(self, event=None, msg=None):
        self.mode = msg


class ContextualModelManager(Abstract):
    def __init__(self):
        self.mode = 0

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("get_contextual_model_mode", self.get)
        EventMesh.subscribe("push_contextual_model_mode", self.set)

    def get(self, event=None, msg=None):
        return self.mode

    def set(self, event=None, msg=None):
        self.mode = msg


class VersionUpdateManager(Abstract):
    def __init__(self):
        pass

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("get_version_update_info", self.get)

    def get(self, event=None, msg=None):
        return "111333"


class AboutManager(Abstract):
    def __init__(self):
        pass

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("get_about_info", self.get)

    def get(self, event=None, msg=None):
        return "111222"


class StudentInfoManager(Abstract):
    def post_processor_after_instantiation(self):
        EventMesh.subscribe("get_student_info", self.get)

    def get(self, event, msg):
        return ["合肥二中", "jaxsen", "九年级", "10班", 'U:/static/headshort.png']


class AddrBookManager(Abstract):
    # 通讯录
    def post_processor_after_instantiation(self):
        EventMesh.subscribe("get_addr_book_list", self.get)
        # 可通过此push_addr_book_list主动推送

    def get(self, event, msg):
        return [
            ["张三", "18175001940"],
            ["李四", "18175001940"],
            ["王五", "18175001940"],
            ["王五", "18175001940"],
            ["王五", "18175001940"],
        ]


class CallLogManager(Abstract):
    # 通话记录
    def __init__(self):
        self.l = [
            # 电话   次数    时间  姓名
            ["18175001940", "8", "12:59", "张三"],
            ["18175001940", "8", "12:58", "张三"],
            ["18175001940", "9", "12:59", "张三"],
            ["18175001940", "5", "12:59", "李四"],
            ["18175001940", "6", "12:59", "李四"],
        ]

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("get_call_log_list", self.get)
        EventMesh.subscribe("call_user", self.call_user)

    def get(self, event, msg):
        return self.l

    def call_user(self, event, msg):
        # msg int 类型
        content = self.l[msg]
        # 参数1 姓名  参数2  电话   参数3 1/主动呼叫  0别人呼叫
        EventMesh.publish("call_in", [content[-1], content[0], 1])


class WallPaperManager(Abstract):
    def __init__(self):
        self.l = [
            # 电话   次数    时间  姓名
            {"url": "U:/static/normal.png", "checked": 1},
            {"url": "U:/static/mp1557714591.png", "checked": 0},
            {"url": "U:/static/mp505517547.png", "checked": 0},
        ]

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("get_bg_img_list", self.get)
        EventMesh.subscribe("set_wall_paper_mode", self.set_wall_paper_mode)

    def set_wall_paper_mode(self, event, msg):
        content = self.l[msg]
        for i, v in enumerate(self.l):
            if i == msg:
                v["checked"] = 1
            else:
                v["checked"] = 0
        EventMesh.publish("set_bg_img", content["url"])

    def get(self, event, msg):
        return self.l


class ClassDetailManager(Abstract):
    def __init__(self):
        self.class_map = {
            7: {
                "name": "星期日",
                "morn": ["语文", "语文", "数学", "数学"],
                "after": ["语文", "语文", "数学", "数学"],
                "night": ["语文", "数学", "无", "无"]
            },
            1: {
                "name": "星期一",
                "morn": ["语文", "语文", "数学", "数学"],
                "after": ["语文", "语文", "数学", "数学"],
                "night": ["语文", "数学", "无", "无"]
            },
            2: {
                "name": "星期二",
                "morn": ["语文", "语文", "数学", "数学"],
                "after": ["语文", "语文", "数学", "数学"],
                "night": ["语文", "数学", "无", "无"]
            },
            3: {
                "name": "星期三",
                "morn": ["语文", "语文", "数学", "数学"],
                "after": ["语文", "语文", "数学", "数学"],
                "night": ["语文", "数学", "无", "无"]
            },
            4: {
                "name": "星期四",
                "morn": ["语文", "语文", "数学", "数学"],
                "after": ["语文", "语文", "数学", "数学"],
                "night": ["语文", "数学", "无", "无"]
            },
            5: {
                "name": "星期五",
                "morn": ["语文", "语文", "数学", "数学"],
                "after": ["语文", "语文", "数学", "数学"],
                "night": ["语文", "数学", "无", "无"]
            },
            6: {
                "name": "星期六",
                "morn": ["语文", "语文", "数学", "数学"],
                "after": ["语文", "语文", "数学", "数学"],
                "night": ["语文", "数学", "无", "无"]
            },

        }

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("get_class_detail", self.get)

    def get(self, event, msg):
        return self.class_map[msg]


class ClockManager(Abstract):
    def __init__(self):
        super().__init__()
        self.clock_list = []

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("get_clock_info_list", self.get)
        EventMesh.subscribe("push_clock_info", self.set)

    def get(self, event, msg):
        return self.clock_list

    def set(self, event, msg):
        print("msg = {}".format(msg))
        idx = msg.get("idx")
        if idx is not None:
            # 修改
            clock_info = self.clock_list[idx]
            clock_info["time"] = msg["time"]
            clock_info["period_list"] = msg["period_list"]
            clock_info["ring_tone_mode"] = msg["ring_tone_mode"]
            clock_info["checked"] = msg["checked"]
        else:
            # 添加
            self.clock_list.append(
                {
                    "time": msg["time"],
                    "period_list": msg["period_list"],
                    "ring_tone_mode": msg["ring_tone_mode"],
                    "checked": msg["ring_tone_mode"],
                }
            )
