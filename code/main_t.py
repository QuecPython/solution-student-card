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

from usr import EventMesh
from usr.common import Abstract
from usr.lcd import *
from usr.btn_device_ec600n import BtnDevice
import hmac


class App(object):
    def __init__(self):
        self.managers = []

    def append_manager(self, manager):
        if isinstance(manager, Abstract):
            manager.post_processor_after_instantiation()
            self.managers.append(manager)
        return self

    def start(self):
        for manager in self.managers:
            manager.post_processor_before_initialization()
            manager.initialization()
            manager.post_processor_after_initialization()


class XSKApp(App):
    def __init__(self):
        super(XSKApp, self).__init__()
        self.__ui = None

    def set_ui(self, ui):
        self.__ui = ui

    def start(self):
        if self.__ui is not None:
            self.__ui.start()
        super().start()
        self.__ui.finish()


if __name__ == '__main__':
    import usr.mgr as mgr
    import usr.ui as _ui

    btn_device = BtnDevice(tp_cst816)
    btn_device.start()
    # from usr.common import LogAdapter;EventMesh.set_log(LogAdapter('eventMesh'))
    ui = _ui.UI(lcd_ctrl)
    ui.add_screen(_ui.MainScreen()) \
        .add_screen(_ui.DropDownMenuScreen()) \
        .add_screen(_ui.MenuScreen()) \
        .add_screen(_ui.AddrBookScreen()) \
        .add_screen(_ui.ClassDetailScreen()) \
        .add_screen(_ui.ClassDateScreen()) \
        .add_screen(_ui.SettingsScreen()) \
        .add_screen(_ui.MenuQrcodeScreen()) \
        .add_screen(_ui.SettingsVolumeScreen()) \
        .add_screen(_ui.SettingBrightNessScreen()) \
        .add_screen(_ui.SettingWallPaperScreen()) \
        .add_screen(_ui.SettingTimeModeScreen()) \
        .add_screen(_ui.SettingContextualModelModeScreen()) \
        .add_screen(_ui.ClearCallRecordMode()) \
        .add_screen(_ui.ClkListScreen()) \
        .add_screen(_ui.NewEditClk()) \
        .add_screen(_ui.ClkRingTong()) \
        .add_screen(_ui.AboutScreen()) \
        .add_screen(_ui.MsgDetailScreen()) \
        .add_screen(_ui.CallScreen()) \
        .add_screen(_ui.PowerDownScreen()) \
        .add_screen(_ui.IdleScreen()) \
        .add_screen(_ui.LearnInfoScreen()) \
        .add_screen(_ui.NormalScreen()) \
        .add_screen(_ui.Menu2Screen()) \
        .add_screen(_ui.HealthQrcodeScreen()) \
        .add_screen(_ui.AddrDetailScreen()) \
        .add_screen(_ui.VersionUpdateScreen()) \
        .add_screen(_ui.CallLogScreen()) \
        .add_screen(_ui.CLKTimeScreen()) \
        .add_screen(_ui.ClkPeriod()) \

    app = XSKApp()
    app.set_ui(ui)
    app.append_manager(mgr.DeviceInfoManager()) \
        .append_manager(mgr.MediaManager()) \
        .append_manager(mgr.BrightNessLevelManager()) \
        .append_manager(mgr.TimeModeManager()) \
        .append_manager(mgr.ContextualModelManager()) \
        .append_manager(mgr.VersionUpdateManager()) \
        .append_manager(mgr.AboutManager()) \
        .append_manager(mgr.StudentInfoManager()) \
        .append_manager(mgr.BatteryManager()) \
        .append_manager(mgr.AddrBookManager()) \
        .append_manager(mgr.WallPaperManager()) \
        .append_manager(mgr.ClassDetailManager()) \
        .append_manager(mgr.CallLogManager()) \
        .append_manager(mgr.ClockManager())
    app.start()

    EventMesh.publish("load_screen", {"screen": "main"})
