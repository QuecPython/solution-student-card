from usr.common import Abstract
import machine
import osTimer
from misc import PowerKey
from usr import EventMesh
from machine import Pin


class BtnDevice(Abstract):

    def __init__(self, tp=None):
        self.pk = PowerKey()
        self.__pwk_timer = osTimer()
        self.keypad = machine.KeyPad(3, 3)
        self.__PowerDownTimeOut = 2000
        self.__tp = tp

    def post_processor_after_instantiation(self):
        self.keypad.init()
        self.keypad.set_callback(self.key_callback)
        self.pk.powerKeyEventRegister(self.pwk_callback)
        if self.__tp:

            self.__tp.set_callback(self.__ui_callback)

    def __ui_callback(self, para):
        print("para = {}".format(para))
        if para == 0:
            EventMesh.publish("done_left_to_right")
            print("<-")
        elif para == 1:
            EventMesh.publish("done_right_to_left")
            print("->")
        elif para == 2:
            EventMesh.publish("done_bottom_to_top")
            print("^")
        elif para == 3:
            EventMesh.publish("done_top_to_bottom")
            print("V")
        elif para == 4:
            EventMesh.publish("done_return")
            print("return")
        elif para == 5:
            EventMesh.publish("done_click")
            print("CLICK")
        elif (para == 6):
            EventMesh.publish("done_error")
            print("error")

    def key_callback(self, l_list):
        if l_list[0] == 1:
            # 马达震动预留
            pass
        if (l_list[1] == 1) and (l_list[2] == 1):
            if l_list[0] == 1:
                EventMesh.publish("btn1_press")
            else:
                EventMesh.publish("btn1_release")

        elif (l_list[1] == 3) and (l_list[2] == 1):
            if l_list[0] == 1:
                EventMesh.publish("btn2_press")
            else:
                EventMesh.publish("btn2_release")
        elif (l_list[1] == 1) and (l_list[2] == 2):
            if l_list[0] == 1:
                EventMesh.publish("btn3_press")
            else:
                EventMesh.publish("btn3_release")
        elif (l_list[1] == 2) and (l_list[2] == 1):
            if l_list[0] == 1:
                EventMesh.publish("btn4_press")
            else:
                EventMesh.publish("btn4_release")
        elif (l_list[1] == 2) and (l_list[2] == 2):
            if l_list[0] == 1:
                EventMesh.publish("btn5_press")
            else:
                EventMesh.publish("btn5_release")
        elif (l_list[1] == 3) and (l_list[2] == 2):
            if l_list[0] == 1:
                EventMesh.publish("btn6_press")
            else:
                EventMesh.publish("btn6_release")
        elif (l_list[1] == 1) and (l_list[2] == 3):
            if l_list[0] == 1:
                EventMesh.publish("btn7_press")
            else:
                EventMesh.publish("btn7_release")

    def pwk_callback(self, status):
        print('==pwr:', status)
        if status == 1:
            self.__pwk_timer.start(self.__PowerDownTimeOut, 0, self.__pwk_long_press_cb)
        elif status == 0:
            self.__pwk_timer.stop()
            # print("btn_back:{}".format(mdls.screen_size_style[mdls.models][1]))
            EventMesh.publish("btn8_press")

    def __pwk_long_press_cb(self, *args):
        '''KEY2:联动屏幕右下角或返回键长按关机'''
        EventMesh.publish("btn8_long_press")

    def start(self):
        self.post_processor_after_instantiation()
