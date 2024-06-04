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

import lvgl as lv
from machine import LCD, Pin
from tp import cst816
init_data = (

    0, 0, 0x11,
    2, 0, 120,

    0, 1, 0x36,
    1, 1, 0x00,

    0, 1, 0x3A,
    1, 1, 0x05,

    0, 5, 0xB2,
    1, 1, 0x1F,
    1, 1, 0x1F,
    1, 1, 0x00,
    1, 1, 0x33,
    1, 1, 0x33,

    0, 1, 0xB7,
    1, 1, 0x00,

    0, 1, 0xBB,
    1, 1, 0x36,

    0, 1, 0xC2,
    1, 1, 0x01,

    0, 1, 0xC3,
    1, 1, 0x13,

    0, 1, 0xC4,
    1, 1, 0x20,

    0, 1, 0xC6,
    1, 1, 0x13,

    0, 1, 0xD6,
    1, 1, 0xA1,

    0, 2, 0xD0,
    1, 1, 0xA4,
    1, 1, 0xA1,

    0, 4, 0x2a,
    1, 1, 0x00,
    1, 1, 0x00,
    1, 1, 0x00,
    1, 1, 0xef,

    0, 4, 0x2b,
    1, 1, 0x00,
    1, 1, 0x00,
    1, 1, 0x00,
    1, 1, 0xef,

    0, 14, 0xE0,
    1, 1, 0xF0,
    1, 1, 0x08,
    1, 1, 0x0E,
    1, 1, 0x09,
    1, 1, 0x08,
    1, 1, 0x04,
    1, 1, 0x2F,
    1, 1, 0x33,
    1, 1, 0x45,
    1, 1, 0x36,
    1, 1, 0x13,
    1, 1, 0x12,
    1, 1, 0x2A,
    1, 1, 0x2D,

    0, 14, 0xE1,
    1, 1, 0xF0,
    1, 1, 0x0E,
    1, 1, 0x12,
    1, 1, 0x0C,
    1, 1, 0x0A,
    1, 1, 0x15,
    1, 1, 0x2E,
    1, 1, 0x32,
    1, 1, 0x44,
    1, 1, 0x39,
    1, 1, 0x17,
    1, 1, 0x18,
    1, 1, 0x2B,
    1, 1, 0x2F,

    0, 3, 0xE4,
    1, 1, 0x1D,
    1, 1, 0x00,
    1, 1, 0x00,

    0, 0, 0x21,

    0, 0, 0x29,

    0, 1, 0xc7,
    1, 1, 0x04,

    0, 1, 0xcc,
    1, 1, 0x18,
)

XSTART_H = 0xf0
XSTART_L = 0xf1
YSTART_H = 0xf2
YSTART_L = 0xf3
XEND_H = 0xE0
XEND_L = 0xE1
YEND_H = 0xE2
YEND_L = 0xE3

XSTART = 0xD0
XEND = 0xD1
YSTART = 0xD2
YEND = 0xD3

lcd = LCD()

init_buf = bytearray(init_data)

init_data2 = (
    0, 4, 0x2a,
    1, 1, XSTART_H,
    1, 1, XSTART_L,
    1, 1, XEND_H,
    1, 1, XEND_L,
    0, 4, 0x2b,
    1, 1, YSTART_H,
    1, 1, YSTART_L,
    1, 1, YEND_H,
    1, 1, YEND_L,
    0, 0, 0x2c,
)
invalid = bytearray(init_data2)

init_data3 = (
    0, 0, 0x28,
    2, 0, 120,
    0, 0, 0x10,
)
displayoff = bytearray(init_data3)

init_data4 = (
    0, 0, 0x11,
    2, 0, 20,
    0, 0, 0x29,
)
displayon = bytearray(init_data4)

lcd_ctrl = Pin(Pin.GPIO17, Pin.OUT, Pin.PULL_DISABLE, 1)
lcd.lcd_init(init_buf, 240, 240, 26000, 1, 4, 0, invalid, displayon, displayoff, None)

LCD_SIZE_W = 240
LCD_SIZE_H = 240

# 初始化lvgl
lv.init()

# Register SDL display driver.
disp_buf1 = lv.disp_draw_buf_t()
buf1_1 = bytearray(LCD_SIZE_W * LCD_SIZE_H * 2)
disp_buf1.init(buf1_1, None, len(buf1_1))
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.draw_buf = disp_buf1
disp_drv.flush_cb = lcd.lcd_write
disp_drv.hor_res = LCD_SIZE_W
disp_drv.ver_res = LCD_SIZE_H
disp_drv.register()

# CST816初始化
tp_cst816 = cst816(irq=14, reset=19)
tp_cst816.activate()
tp_cst816.init()
print("cst816 init...")
# LVGL触摸注册
indev_drv = lv.indev_drv_t()
indev_drv.init()
indev_drv.type = lv.INDEV_TYPE.POINTER
indev_drv.read_cb = tp_cst816.read
indev_drv.long_press_time = 300
indev_drv.register()
gpio4 = Pin(Pin.GPIO14, Pin.OUT, Pin.PULL_PU, 0)

# 启动lvgv线程
lv.tick_inc(5)
lv.task_handler()
