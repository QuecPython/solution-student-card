import utime
import osTimer
import lvgl as lv
from usr import EventMesh
from misc import Power

# -----------------------------------------style create--------------------------------------
# create style style_screen

style_screen = lv.style_t()
style_screen.init()
style_screen.set_radius(0)
style_screen.set_bg_color(lv.color_make(0x2f, 0x2d, 0x2d))
style_screen.set_bg_opa(255)
style_screen.set_border_width(0)
style_screen.set_pad_left(0)
style_screen.set_pad_right(0)
style_screen.set_pad_top(0)
style_screen.set_pad_bottom(0)

# -----------------------------------------------IDLE SCREEN-----------------------------------------------------
idle = lv.obj()

idle2 = lv.obj(idle)
# power_down2 = lv.obj()
idle2.center()
idle2.set_size(240, 240)
idle2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

idle_img = lv.img(idle2)
idle_img.set_size(240, 240)
idle_img.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)
idle_img.set_src("U:/static/idle.jpg")
lv.scr_load(idle)
# --------------------------------------------------------------------------------------------------------------

style_screen2 = lv.style_t()
style_screen2.init()
style_screen2.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
style_screen2.set_bg_opa(255)

style_img = lv.style_t()
style_img.init()
style_img.set_img_opa(255)


# 默认白色
class FontStyle(object):
    def __init__(self):
        self.style = lv.style_t()

    def style_font(self, font, space, color=lv.color_make(0xff, 0xff, 0xff)):
        self.style.init()
        self.style.set_bg_opa(0)
        self.style.set_text_color(color)
        self.style.set_text_font(font)
        self.style.set_text_letter_space(space)
        return self.style


style_font_bold_18_style = FontStyle()
style_font_bold_18 = style_font_bold_18_style.style_font(lv.font_bold_18, 2)
style_font_bold_34_style = FontStyle()
style_font_bold_34 = style_font_bold_34_style.style_font(lv.font_bold_34, 2)

style_font_bold_34_space_0_default_style = FontStyle()
style_font_bold_34_space_0_default = style_font_bold_34_space_0_default_style.style_font(lv.font_bold_34, 0)

style_font_regular_18_space_0_default_style = FontStyle()
style_font_regular_18_space_0_default = style_font_regular_18_space_0_default_style.style_font(lv.font_regular_18, 0)

style_font_regular_12_space_0_default_style = FontStyle()
style_font_regular_12_space_0_default = style_font_regular_12_space_0_default_style.style_font(lv.font_regular_12, 0)

style_font_regular_22_space_2_default_style = FontStyle()
style_font_regular_22_space_2_default = style_font_regular_22_space_2_default_style.style_font(lv.font_regular_22, 2)

style_font_regular_14_space_0_default_style = FontStyle()
style_font_regular_14_space_0_default = style_font_regular_14_space_0_default_style.style_font(lv.font_regular_14, 0)

style_font_regular_14_space_1_default_style = FontStyle()
style_font_regular_14_space_1_default = style_font_regular_14_space_1_default_style.style_font(lv.font_regular_14, 1)

style_font_regular_24_space_2_default_style = FontStyle()
style_font_regular_24_space_2_default = style_font_regular_24_space_2_default_style.style_font(lv.font_regular_24, 2)

style_font_regular_20_space_2_default_style = FontStyle()
style_font_regular_20_space_2_default = style_font_regular_20_space_2_default_style.style_font(lv.font_regular_20, 2)

style_font_regular_20_space_0_default_style = FontStyle()
style_font_regular_20_space_0_default = style_font_regular_20_space_2_default_style.style_font(lv.font_regular_20, 0)

style_font_regular_18_space_1_default_style = FontStyle()
style_font_regular_18_space_1_default = style_font_regular_18_space_1_default_style.style_font(lv.font_regular_18, 1)

style_font_regular_18_space_2_default_style = FontStyle()
style_font_regular_18_space_2_default = style_font_regular_18_space_2_default_style.style_font(lv.font_regular_18, 2)

style_font_regular_18_space_2_default_anim_style = FontStyle()
style_font_regular_18_space_2_default_anim = style_font_regular_18_space_2_default_style.style_font(lv.font_regular_18,
                                                                                                    2)
style_font_regular_18_space_2_default_anim.set_anim_speed(10)

style_font_regular_18_space_2_white_style = FontStyle()
style_font_regular_18_space_2_white = style_font_regular_18_space_2_white_style.style_font(lv.font_regular_18, 2,
                                                                                           lv.color_make(0x00, 0x00,
                                                                                                         0x00))
style_font_regular_18_space_0_white_style = FontStyle()
style_font_regular_18_space_0_white = style_font_regular_18_space_2_white_style.style_font(lv.font_regular_18, 0,
                                                                                           lv.color_make(0x00, 0x00,
                                                                                                         0x00))

style_font_regular_24_space_0_white_style = FontStyle()
style_font_regular_24_space_0_white = style_font_regular_24_space_0_white_style.style_font(lv.font_regular_24, 0,
                                                                                           lv.color_make(0x00, 0x00,
                                                                                                         0x00))
style_font_regular_22_space_0_white_style = FontStyle()
style_font_regular_22_space_0_white = style_font_regular_22_space_0_white_style.style_font(lv.font_regular_22, 0,
                                                                                           lv.color_make(0x00, 0x00,
                                                                                                         0x00))

style_font_regular_14_space_0_white_style = FontStyle()
style_font_regular_14_space_0_white = style_font_regular_14_space_0_white_style.style_font(lv.font_regular_14, 0,
                                                                                           lv.color_make(0x00, 0x00,
                                                                                                         0x00))

# create style style_list
style_list = lv.style_t()
style_list.init()
style_list.set_radius(3)
style_list.set_bg_color(lv.color_make(0x2f, 0x2d, 0x2d))
style_list.set_bg_opa(255)
style_list.set_border_width(0)
style_list.set_pad_left(0)
style_list.set_pad_right(0)
style_list.set_pad_top(0)

# create style style_list_scro
style_list_scro = lv.style_t()
style_list_scro.init()
style_list_scro.set_radius(3)
style_list_scro.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
style_list_scro.set_bg_opa(11)

# create style style_list_scro
style_scro = lv.style_t()
style_scro.init()
style_scro.set_bg_opa(0)

# create style style_dropdown_cont
style_dropdown_cont = lv.style_t()
style_dropdown_cont.init()
style_dropdown_cont.set_radius(0)
style_dropdown_cont.set_bg_color(lv.color_make(0x2e, 0x29, 0x29))
style_dropdown_cont.set_bg_opa(218)
style_dropdown_cont.set_border_width(0)
style_dropdown_cont.set_pad_left(0)
style_dropdown_cont.set_pad_right(0)
style_dropdown_cont.set_pad_top(0)
style_dropdown_cont.set_pad_bottom(0)

style_tv = lv.style_t()
style_tv.init()
style_tv.set_radius(0)
style_tv.set_bg_opa(0)

# create style style_call_cont
style_call_cont = lv.style_t()
style_call_cont.init()
style_call_cont.set_radius(6)
style_call_cont.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
style_call_cont.set_bg_opa(39)
style_call_cont.set_border_width(0)
style_call_cont.set_pad_left(0)
style_call_cont.set_pad_right(0)
style_call_cont.set_pad_top(0)
style_call_cont.set_pad_bottom(0)

# create style style_line
style_line = lv.style_t()
style_line.init()
style_line.set_line_color(lv.color_make(0x00, 0xa0, 0xe9))
style_line.set_line_width(2)
style_line.set_line_rounded(255)

# create style style_line2
style_line2 = lv.style_t()
style_line2.init()
style_line2.set_line_color(lv.color_make(0xff, 0xff, 0xff))
style_line2.set_line_width(1)
style_line2.set_line_rounded(255)

# create style style_btn
style_btn = lv.style_t()
style_btn.init()
style_btn.set_bg_opa(0)
style_btn.set_shadow_opa(0)
style_btn.set_border_width(0)


# switch style
class SwStyle(object):
    def __init__(self):
        self.style = lv.style_t()

    def style_sw(self, color=lv.color_make(0xe6, 0xe2, 0xe6)):
        self.style.init()
        self.style.set_radius(100)
        self.style.set_bg_color(color)
        self.style.set_bg_opa(255)
        return self.style


default_sw_style = SwStyle()
sw_style = default_sw_style.style_sw()

default_sw_69b7f7_style = SwStyle()
sw_69b7f7_style = default_sw_69b7f7_style.style_sw(lv.color_make(0x69, 0xb7, 0xf7))

default_sw_black_style = SwStyle()
sw_black_style = default_sw_black_style.style_sw(lv.color_make(0xff, 0xff, 0xff))


# cont style
class ContStyle(object):
    def __init__(self):
        self.style = lv.style_t()

    def style_cont(self, radius, color1, color2, opa):
        self.style.init()
        self.style.set_radius(radius)
        self.style.set_bg_color(color1)
        self.style.set_bg_grad_color(color2)
        self.style.set_bg_grad_dir(lv.GRAD_DIR.VER)
        self.style.set_bg_opa(opa)
        self.style.set_border_width(0)
        self.style.set_pad_left(0)
        self.style.set_pad_right(0)
        self.style.set_pad_top(0)
        self.style.set_pad_bottom(0)
        return self.style


# create style style_bar
style_bar = lv.style_t()
style_bar.init()
style_bar.set_radius(10)
style_bar.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
style_bar.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
style_bar.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_bar.set_bg_opa(60)
style_bar.set_pad_left(0)
style_bar.set_pad_right(0)
style_bar.set_pad_top(0)
style_bar.set_pad_bottom(0)

style_bar_indic = lv.style_t()
style_bar_indic.init()
style_bar_indic.set_radius(10)
style_bar_indic.set_bg_color(lv.color_make(0x21, 0x95, 0xf6))
style_bar_indic.set_bg_grad_color(lv.color_make(0x21, 0x95, 0xf6))
style_bar_indic.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_bar_indic.set_bg_opa(255)
# -----------------------------------------style screen--------------------------------------

# -------------------------------------------main screen----------------------------------------------------------
main = lv.obj()
main2 = lv.obj(main)
# main2 = lv.obj()
main2.center()
main2.set_size(240, 240)
main2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)
main_img_1 = lv.img(main2)
main_img_1.set_pos(0, 0)
main_img_1.set_size(240, 240)
main_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
main_img_1_img = "U:/static/normal.png"

main_img_1.set_src(main_img_1_img)
main_img_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

main_time_1 = lv.label(main2)
main_time_1.set_pos(16, 63)
main_time_1.set_size(104, 32)
main_time_1.set_text("11:06")
main_time_1.set_long_mode(lv.label.LONG.WRAP)
main_time_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
main_time_2 = lv.label(main2)
main_time_2.set_pos(137, 75)
main_time_2.set_size(45, 19)
main_time_2.set_text("上午")
main_time_2.set_long_mode(lv.label.LONG.WRAP)
main_time_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)

main_time_1.add_style(style_font_bold_34, lv.PART.MAIN | lv.STATE.DEFAULT)
# add style for main_time_2
main_time_2.add_style(style_font_bold_18, lv.PART.MAIN | lv.STATE.DEFAULT)

main_date_1 = lv.label(main2)
main_date_1.set_pos(17, 120)
main_date_1.set_size(150, 19)
main_date_1.set_text("6-15 星期三")
main_date_1.set_long_mode(lv.label.LONG.WRAP)
main_date_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)

main_date_1.add_style(style_font_bold_18, lv.PART.MAIN | lv.STATE.DEFAULT)

main_img_2 = lv.img(main2)
main_img_2.set_pos(207, 3)
main_img_2.set_size(30, 16)
main_img_2.add_flag(lv.obj.FLAG.CLICKABLE)
# 电量显示
main_img_2_img = "U:/static/vbat_100.png"

main_img_2.set_src(main_img_2_img)

# add style for main_img_2
main_img_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

main_img_3 = lv.img(main2)
main_img_3.set_pos(147, 3)
main_img_3.set_size(16, 16)
main_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
# 闹钟标识
main_img_3_img = "U:/static/mp-895447498.png"
main_img_3.set_src(main_img_3_img)
main_img_3.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

main_img_4 = lv.img(main2)
main_img_4.set_pos(128, 3)
main_img_4.set_size(11, 16)
main_img_4.add_flag(lv.obj.FLAG.CLICKABLE)

# 定位标识
main_img_4_img = "U:/static/mp-1553323012.png"

main_img_4.set_src(main_img_4_img)
main_img_4.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

# 信号等级
main_img_5 = lv.img(main2)
main_img_5.set_pos(2, 3)
main_img_5.set_size(16, 16)
main_img_5.add_flag(lv.obj.FLAG.CLICKABLE)

main_img_5_img = "U:/static/mp2123144873.png"

main_img_5.set_src(main_img_5_img)
main_img_5.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

main_img_6 = lv.img(main2)
main_img_6.set_pos(51, 6)
main_img_6.set_size(62, 12)
main_img_6.add_flag(lv.obj.FLAG.CLICKABLE)

# SIM卡类型 中国移动
main_img_6_img = "U:/static/mp995713883.png"

main_img_6.set_src(main_img_6_img)
main_img_6.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

main_img_7 = lv.img(main2)
main_img_7.set_pos(32, 7)
main_img_7.set_size(14, 9)
main_img_7.add_flag(lv.obj.FLAG.CLICKABLE)

# 4G
main_img_7_img = "U:/static/mp1203753931.png"

main_img_7.set_src(main_img_7_img)
main_img_7.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

main_img_11 = lv.img(main2)
main_img_11.set_pos(197, 3)
main_img_11.set_size(6, 16)
main_img_11.add_flag(lv.obj.FLAG.CLICKABLE)

# 充电标识
main_img_11_img = "U:/static/charge_in.png"

main_img_11.set_src(main_img_11_img)
main_img_11.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

main_cont_1 = lv.obj(main2)
main_cont_1.set_pos(30, 40)
main_cont_1.set_size(180, 180)
main_img_13 = lv.img(main_cont_1)
main_img_13.set_pos(50, 40)
main_img_13.set_size(50, 110)
main_img_13.add_flag(lv.obj.FLAG.CLICKABLE)

main_img_13_img = "U:/static/mp-485020138.png"

main_img_13.set_src(main_img_13_img)
main_img_13.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

main_img_12 = lv.img(main_cont_1)
main_img_12.set_pos(25, -1)
main_img_12.set_size(96, 24)
main_img_12.add_flag(lv.obj.FLAG.CLICKABLE)

main_img_12_img = "U:/static/mp-1269336439.png"

main_img_12.set_src(main_img_12_img)
main_img_12.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

# 测温
main_temperature_title = lv.label(main2)
main_temperature_title.set_pos(30, 150)
main_temperature_title.set_size(90, 19)
main_temperature_title.set_text("体温记录")
main_temperature_title.set_long_mode(lv.label.LONG.WRAP)
main_temperature_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

main_temperature_arc = lv.img(main2)
main_temperature_arc.set_pos(40, 180)
main_temperature_arc.set_size(55, 54)
main_temperature_arc.set_src("U:/static/arc.png")

main_temperature_value = lv.label(main2)
main_temperature_value.set_pos(49, 197)
main_temperature_value.set_size(90, 19)
main_temperature_value.set_text("36.5")
main_temperature_value.set_long_mode(lv.label.LONG.WRAP)
main_temperature_value.add_style(style_font_regular_18_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

main_step_title = lv.label(main2)
main_step_title.set_pos(140, 150)
main_step_title.set_size(90, 19)
main_step_title.set_text("今日步数")
main_step_title.set_long_mode(lv.label.LONG.WRAP)
main_step_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

main_step_arc = lv.img(main2)
main_step_arc.set_pos(145, 180)
main_step_arc.set_size(55, 54)
main_step_arc.set_src("U:/static/arc.png")

main_step_value = lv.label(main2)
main_step_value.set_pos(149, 197)
main_step_value.set_size(90, 19)
main_step_value.set_text("21020")
main_step_value.set_long_mode(lv.label.LONG.WRAP)
main_step_value.add_style(style_font_regular_18_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

# add style for main_cont_1
main_cont_1_style_cont = ContStyle()
main_cont_1.add_style(
    main_cont_1_style_cont.style_cont(7, lv.color_make(0xff, 0xff, 0xff), lv.color_make(0xff, 0xff, 0xff), 216),
    lv.PART.MAIN | lv.STATE.DEFAULT)
main_cont_1.add_flag(lv.obj.FLAG.HIDDEN)

# -------------------------------------------dropdown screen----------------------------------------------------------
dropdown = lv.obj()
dropdown2 = lv.obj(dropdown)
# dropdown2 = lv.obj()
dropdown2.center()
dropdown2.set_size(240, 240)
# dropdown2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
dropdown2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_img_1 = lv.img(dropdown2)
dropdown_img_1.set_pos(0, 0)
dropdown_img_1.set_size(240, 240)
dropdown_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

dropdown_img_1_img = "U:/static/normal.png"

dropdown_img_1.set_src(dropdown_img_1_img)
dropdown_img_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_time_1 = lv.label(dropdown2)
dropdown_time_1.set_pos(16, 63)
dropdown_time_1.set_size(104, 32)
dropdown_time_1.set_text("11:06")
dropdown_time_1.set_long_mode(lv.label.LONG.WRAP)
dropdown_time_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
dropdown_time_2 = lv.label(dropdown2)
dropdown_time_2.set_pos(137, 75)
dropdown_time_2.set_size(45, 19)
dropdown_time_2.set_text("上午")
dropdown_time_2.set_long_mode(lv.label.LONG.WRAP)
dropdown_time_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
dropdown_time_1.add_style(style_font_bold_34, lv.PART.MAIN | lv.STATE.DEFAULT)
dropdown_time_2.add_style(style_font_bold_18, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_date_1 = lv.label(dropdown2)
dropdown_date_1.set_pos(17, 120)
dropdown_date_1.set_size(150, 19)
dropdown_date_1.set_text("6-15 星期三")
dropdown_date_1.set_long_mode(lv.label.LONG.WRAP)
dropdown_date_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
dropdown_date_1.add_style(style_font_bold_18, lv.PART.MAIN | lv.STATE.DEFAULT)

# 测温
dropdown_temperature_title = lv.label(dropdown2)
dropdown_temperature_title.set_pos(30, 150)
dropdown_temperature_title.set_size(90, 19)
dropdown_temperature_title.set_text("体温记录")
dropdown_temperature_title.set_long_mode(lv.label.LONG.WRAP)
dropdown_temperature_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_temperature_arc = lv.img(dropdown2)
dropdown_temperature_arc.set_pos(40, 180)
dropdown_temperature_arc.set_size(55, 54)
dropdown_temperature_arc.set_src("U:/static/arc.png")

dropdown_temperature_value = lv.label(dropdown2)
dropdown_temperature_value.set_pos(49, 197)
dropdown_temperature_value.set_size(90, 19)
dropdown_temperature_value.set_text("36.5")
dropdown_temperature_value.set_long_mode(lv.label.LONG.WRAP)
dropdown_temperature_value.add_style(style_font_regular_18_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_step_title = lv.label(dropdown2)
dropdown_step_title.set_pos(140, 150)
dropdown_step_title.set_size(90, 19)
dropdown_step_title.set_text("今日步数")
dropdown_step_title.set_long_mode(lv.label.LONG.WRAP)
dropdown_step_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_step_arc = lv.img(dropdown2)
dropdown_step_arc.set_pos(145, 180)
dropdown_step_arc.set_size(55, 54)
dropdown_step_arc.set_src("U:/static/arc.png")

dropdown_step_value = lv.label(dropdown2)
dropdown_step_value.set_pos(149, 197)
dropdown_step_value.set_size(90, 19)
dropdown_step_value.set_text("21020")
dropdown_step_value.set_long_mode(lv.label.LONG.WRAP)
dropdown_step_value.add_style(style_font_regular_18_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_cont_1 = lv.obj(dropdown2)
dropdown_cont_1.set_pos(0, 0)
dropdown_cont_1.set_size(240, 240)

dropdown_cont_2 = lv.obj(dropdown_cont_1)
dropdown_cont_2.set_pos(14, 27)
dropdown_cont_2.set_size(212, 68)

dropdown_cont_2_cont_style = ContStyle()
dropdown_cont_2.add_style(
    dropdown_cont_2_cont_style.style_cont(0, lv.color_make(0xfc, 0xfc, 0xfc), lv.color_make(0xfc, 0xfc, 0xfc), 92),
    lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_label_4 = lv.label(dropdown_cont_1)
dropdown_label_4.set_pos(65, 65)
dropdown_label_4.set_size(45, 17)
dropdown_label_4.set_text("13%")
dropdown_label_4.set_long_mode(lv.label.LONG.WRAP)
dropdown_label_4.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
dropdown_label_4.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_img_3 = lv.img(dropdown_cont_1)
dropdown_img_3.set_pos(22, 38)
dropdown_img_3.set_size(15, 15)
dropdown_img_3.add_flag(lv.obj.FLAG.CLICKABLE)

dropdown_img_3_img = "U:/static/mp1614307047.png"

dropdown_img_3.set_src(dropdown_img_3_img)
dropdown_img_3.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_label_3 = lv.label(dropdown_cont_1)
dropdown_label_3.set_pos(41, 35)
dropdown_label_3.set_size(28, 17)
dropdown_label_3.set_text("4G")
dropdown_label_3.set_long_mode(lv.label.LONG.WRAP)
dropdown_label_3.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
dropdown_label_3.add_style(style_font_regular_18_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_label_2 = lv.label(dropdown_cont_1)
dropdown_label_2.set_pos(68, 35)
dropdown_label_2.set_size(83, 19)
dropdown_label_2.set_text("中国移动")
dropdown_label_2.set_long_mode(lv.label.LONG.WRAP)
dropdown_label_2.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
dropdown_label_2.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_label_1 = lv.label(dropdown_cont_1)
dropdown_label_1.set_pos(161, 68)
dropdown_label_1.set_size(57, 21)
dropdown_label_1.set_text("11:06")
dropdown_label_1.set_long_mode(lv.label.LONG.WRAP)
dropdown_label_1.set_style_text_align(lv.TEXT_ALIGN.RIGHT, 0)
dropdown_label_1.add_style(style_font_regular_18_space_1_default, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_img_2 = lv.img(dropdown_cont_1)
dropdown_img_2.set_pos(195, 45)
dropdown_img_2.set_size(16, 15)
dropdown_img_2.add_flag(lv.obj.FLAG.CLICKABLE)

dropdown_img_2_img = "U:/static/mp131050697.png"

dropdown_img_2.set_src(dropdown_img_2_img)
dropdown_img_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_img_11 = lv.img(dropdown_cont_1)
dropdown_img_11.set_pos(23, 70)
dropdown_img_11.set_size(6, 16)
dropdown_img_11.add_flag(lv.obj.FLAG.CLICKABLE)

# 充电标识
dropdown_img_11_img = "U:/static/charge_in.png"

dropdown_img_11.set_src(dropdown_img_11_img)
dropdown_img_11.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_img_4 = lv.img(dropdown_cont_1)
dropdown_img_4.set_pos(31, 70)
dropdown_img_4.set_size(30, 16)
dropdown_img_4.add_flag(lv.obj.FLAG.CLICKABLE)

dropdown_img_4_img = "U:/static/mp-1117716976.png"

dropdown_img_4.set_src(dropdown_img_4_img)
dropdown_img_4.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_img_7 = lv.img(dropdown_cont_1)
dropdown_img_7.set_pos(165, 145)
dropdown_img_7.set_size(70, 70)
dropdown_img_7.add_flag(lv.obj.FLAG.CLICKABLE)

dropdown_img_7_img = "U:/static/mp7842493.png"

dropdown_img_7.set_src(dropdown_img_7_img)
dropdown_img_7.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_img_6 = lv.img(dropdown_cont_1)
dropdown_img_6.set_pos(85, 145)
dropdown_img_6.set_size(70, 70)
dropdown_img_6.add_flag(lv.obj.FLAG.CLICKABLE)

dropdown_img_6_img = "U:/static/mp7842493.png"

dropdown_img_6.set_src(dropdown_img_6_img)
dropdown_img_6.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_img_5 = lv.img(dropdown_cont_1)
dropdown_img_5.set_pos(4, 145)
dropdown_img_5.set_size(70, 70)
dropdown_img_5.add_flag(lv.obj.FLAG.CLICKABLE)

dropdown_img_5_img = "U:/static/mp7842493.png"

dropdown_img_5.set_src(dropdown_img_5_img)
dropdown_img_5.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

dropdown_imgbtn_1 = lv.imgbtn(dropdown_cont_1)
dropdown_imgbtn_1.set_pos(23, 163)
dropdown_imgbtn_1.set_size(30, 30)

dropdown_imgbtn_1_imgReleased = "U:/static/mp-1036500799.png"
dropdown_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, dropdown_imgbtn_1_imgReleased, None, None)

dropdown_imgbtn_1_imgPressed = "U:/static/mp-1036500799.png"
dropdown_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, dropdown_imgbtn_1_imgPressed, None, None)

dropdown_imgbtn_1_imgCheckedReleased = "U:/static/mp-1036500799.png"
dropdown_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dropdown_imgbtn_1_imgCheckedReleased, None, None)

dropdown_imgbtn_1_imgCheckedPressed = "U:/static/mp-1036500799.png"
dropdown_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dropdown_imgbtn_1_imgCheckedPressed, None, None)

dropdown_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
dropdown_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
dropdown_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
dropdown_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

dropdown_imgbtn_2 = lv.imgbtn(dropdown_cont_1)
dropdown_imgbtn_2.set_pos(102, 166)
dropdown_imgbtn_2.set_size(35, 25)

dropdown_imgbtn_2_imgReleased = "U:/static/mp-759646071.png"
dropdown_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, dropdown_imgbtn_2_imgReleased, None, None)

dropdown_imgbtn_2_imgPressed = "U:/static/mp-759646071.png"
dropdown_imgbtn_2.set_src(lv.imgbtn.STATE.PRESSED, dropdown_imgbtn_2_imgPressed, None, None)

dropdown_imgbtn_2_imgCheckedReleased = "U:/static/mp-759646071.png"
dropdown_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dropdown_imgbtn_2_imgCheckedReleased, None, None)

dropdown_imgbtn_2_imgCheckedPressed = "U:/static/mp-759646071.png"
dropdown_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dropdown_imgbtn_2_imgCheckedPressed, None, None)

dropdown_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
dropdown_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
dropdown_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
dropdown_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

dropdown_imgbtn_3 = lv.imgbtn(dropdown_cont_1)
dropdown_imgbtn_3.set_pos(187, 163)
dropdown_imgbtn_3.set_size(30, 30)

dropdown_imgbtn_3_imgReleased = "U:/static/mp-855818693.png"
dropdown_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, dropdown_imgbtn_3_imgReleased, None, None)

dropdown_imgbtn_3_imgPressed = "U:/static/mp-855818693.png"
dropdown_imgbtn_3.set_src(lv.imgbtn.STATE.PRESSED, dropdown_imgbtn_3_imgPressed, None, None)

dropdown_imgbtn_3_imgCheckedReleased = "U:/static/mp-855818693.png"
dropdown_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, dropdown_imgbtn_3_imgCheckedReleased, None, None)

dropdown_imgbtn_3_imgCheckedPressed = "U:/static/mp-855818693.png"
dropdown_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, dropdown_imgbtn_3_imgCheckedPressed, None, None)

dropdown_imgbtn_3.add_flag(lv.obj.FLAG.CHECKABLE)
dropdown_imgbtn_3.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
dropdown_imgbtn_3.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
dropdown_imgbtn_3.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

dropdown_cont_1.add_style(style_dropdown_cont, lv.PART.MAIN | lv.STATE.DEFAULT)
# ---------------------------------------health screen --------------------------------------------------------------
health_qrcode = lv.obj()
health_qrcode2 = lv.obj(health_qrcode)
# qrcode2 = lv.obj()
health_qrcode2.center()
health_qrcode2.set_size(240, 240)
# qrcode2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)

health_qrcode2_1 = lv.img(health_qrcode2)
health_qrcode2_1.set_pos(0, 0)
health_qrcode2_1.set_size(240, 240)
health_qrcode2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
health_qrcode2_1_img = "U:/static/normal.png"

health_qrcode2_1.set_src(health_qrcode2_1_img)
health_qrcode2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

health_qrcode2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

bg_color = lv.palette_lighten(lv.PALETTE.LIGHT_BLUE, 5)
fg_color = lv.palette_darken(lv.PALETTE.BLUE, 4)

qr = lv.qrcode(health_qrcode2, 140, fg_color, bg_color)
# Set data
data = "18828282828"
qr.update(data, len(data))
qr.center()
# Add a border with bg_color
qr.set_style_border_color(bg_color, 0)
qr.set_style_border_width(5, 0)

qrcode_phone_num = lv.label(health_qrcode2)
qrcode_phone_num.set_pos(0, 201)
qrcode_phone_num.set_size(240, 27)
qrcode_phone_num.set_text("绿码")
qrcode_phone_num.set_long_mode(lv.label.LONG.WRAP)
qrcode_phone_num.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
qrcode_phone_num.add_style(style_font_regular_18_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------qrcode screen----------------------------------------------------------
qrcode = lv.obj()
qrcode2 = lv.obj(qrcode)
# qrcode2 = lv.obj()
qrcode2.center()
qrcode2.set_size(240, 240)
# qrcode2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)

qrcode2_1 = lv.img(qrcode2)
qrcode2_1.set_pos(0, 0)
qrcode2_1.set_size(240, 240)
qrcode2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
qrcode2_1_img = "U:/static/normal.png"

qrcode2_1.set_src(qrcode2_1_img)
qrcode2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

qrcode2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

bg_color = lv.palette_lighten(lv.PALETTE.LIGHT_BLUE, 5)
fg_color = lv.palette_darken(lv.PALETTE.BLUE, 4)

qr = lv.qrcode(qrcode2, 140, fg_color, bg_color)
# Set data
data = "18828282828"
qr.update(data, len(data))
qr.center()
# Add a border with bg_color
qr.set_style_border_color(bg_color, 0)
qr.set_style_border_width(5, 0)

qrcode_phone_num = lv.label(qrcode2)
qrcode_phone_num.set_pos(0, 201)
qrcode_phone_num.set_size(240, 27)
qrcode_phone_num.set_text("18828282828")
qrcode_phone_num.set_long_mode(lv.label.LONG.WRAP)
qrcode_phone_num.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
qrcode_phone_num.add_style(style_font_regular_18_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------pullup screen----------------------------------------------------------

pullup = lv.obj()
pullup2 = lv.obj(pullup)
# pullup2 = lv.obj()
pullup2.center()
pullup2.set_size(240, 240)
# pullup2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
pullup2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

pullup_img_1 = lv.img(pullup2)
pullup_img_1.set_pos(53, 145)
pullup_img_1.set_size(135, 60)
pullup_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

pullup_img_1_img = "U:/static/mp-658613786.png"

pullup_img_1.set_src(pullup_img_1_img)
pullup_img_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

pullup_img_2 = lv.img(pullup2)
pullup_img_2.set_pos(75, 156)
pullup_img_2.set_size(90, 35)
pullup_img_2.add_flag(lv.obj.FLAG.CLICKABLE)

pullup_img_2_img = "U:/static/mp-1205647634.png"

pullup_img_2.set_src(pullup_img_2_img)
pullup_img_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

pullup_img_3 = lv.img(pullup2)
pullup_img_3.set_pos(9, 27)
pullup_img_3.set_size(65, 65)
pullup_img_3.add_flag(lv.obj.FLAG.CLICKABLE)

pullup_img_3_img = "U:/static/mp553521582.png"

pullup_img_3.set_src(pullup_img_3_img)
pullup_img_3.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

pullup_img_4 = lv.img(pullup2)
pullup_img_4.set_pos(87, 27)
pullup_img_4.set_size(65, 65)
pullup_img_4.add_flag(lv.obj.FLAG.CLICKABLE)

pullup_img_4_img = "U:/static/mp553521582.png"

pullup_img_4.set_src(pullup_img_4_img)
pullup_img_4.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

pullup_img_5 = lv.img(pullup2)
pullup_img_5.set_pos(166, 27)
pullup_img_5.set_size(65, 65)
pullup_img_5.add_flag(lv.obj.FLAG.CLICKABLE)

pullup_img_5_img = "U:/static/mp553521582.png"

pullup_img_5.set_src(pullup_img_5_img)
pullup_img_5.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

pullup_label_1 = lv.label(pullup2)
pullup_label_1.set_pos(17, 44)
pullup_label_1.set_size(49, 33)
pullup_label_1.set_text("1")
pullup_label_1.set_long_mode(lv.label.LONG.WRAP)
pullup_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
pullup_label_1.add_style(style_font_bold_34_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

pullup_label_2 = lv.label(pullup2)
pullup_label_2.set_pos(95, 44)
pullup_label_2.set_size(49, 33)
pullup_label_2.set_text("2")
pullup_label_2.set_long_mode(lv.label.LONG.WRAP)
pullup_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
pullup_label_2.add_style(style_font_bold_34_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

pullup_label_3 = lv.label(pullup2)
pullup_label_3.set_pos(175, 44)
pullup_label_3.set_size(49, 33)
pullup_label_3.set_text("3")
pullup_label_3.set_long_mode(lv.label.LONG.WRAP)
pullup_label_3.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
pullup_label_3.add_style(style_font_bold_34_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------call screen----------------------------------------------------------

call = lv.obj()
call2 = lv.obj(call)
# call2 = lv.obj()
call2.center()
call2.set_size(240, 240)
# call2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
call2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

call2_1 = lv.img(call2)
call2_1.set_pos(0, 0)
call2_1.set_size(240, 240)
call2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
call2_1_img = "U:/static/normal.png"

call2_1.set_src(call2_1_img)
call2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

call_name = lv.label(call2)
call_name.set_pos(68, 35)
call_name.set_size(99, 25)
call_name.set_text("美美")
call_name.set_long_mode(lv.label.LONG.WRAP)
call_name.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
call_name.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

call_phone = lv.label(call2)
call_phone.set_pos(66, 68)
call_phone.set_size(105, 16)
call_phone.set_text("18888888888")
call_phone.set_long_mode(lv.label.LONG.WRAP)
call_phone.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
call_phone.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

call_state = lv.label(call2)
call_state.set_pos(66, 88)
call_state.set_size(105, 16)
call_state.set_text("正在呼叫")
call_state.set_long_mode(lv.label.LONG.WRAP)
call_state.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
call_state.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

call_cont_1 = lv.obj(call2)
call_cont_1.set_pos(30, 142)
call_cont_1.set_size(80, 80)
call_speaker = lv.img(call_cont_1)
call_speaker.set_pos(15, 15)
call_speaker.set_size(50, 50)

call_speaker_imgReleased = "U:/static/mp2109784762.png"
call_speaker.set_src(call_speaker_imgReleased)
call_speaker.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
call_speaker.add_flag(lv.obj.FLAG.CLICKABLE)

# add style for call_cont_1
call_cont_1.add_style(style_call_cont, lv.PART.MAIN | lv.STATE.DEFAULT)

call_cont_2 = lv.obj(call2)
call_cont_2.set_pos(130, 141)
call_cont_2.set_size(80, 80)
call_answer = lv.img(call_cont_2)
call_answer.set_pos(15, 15)
call_answer.set_size(53, 52)

call_answer_imgReleased = "U:/static/mp523231338.png"
call_answer.set_src(call_answer_imgReleased)
call_answer.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
call_answer.add_flag(lv.obj.FLAG.CLICKABLE)

call_cont_2.add_style(style_call_cont, lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------menu screen----------------------------------------------------------
addr_detail = lv.obj()
addr_detail2 = lv.obj(addr_detail)
# addr_detail2 = lv.obj()
addr_detail2.center()
addr_detail2.set_size(240, 240)
# addr_detail2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
addr_detail2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

addr_detail2_1 = lv.img(addr_detail2)
addr_detail2_1.set_pos(0, 0)
addr_detail2_1.set_size(240, 240)
addr_detail2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
addr_detail2_1_img = "U:/static/normal.png"

addr_detail2_1.set_src(addr_detail2_1_img)
addr_detail2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

addr_detail_name = lv.label(addr_detail2)
addr_detail_name.set_pos(68, 35)
addr_detail_name.set_size(99, 25)
addr_detail_name.set_text("美美")
addr_detail_name.set_long_mode(lv.label.LONG.WRAP)
addr_detail_name.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
addr_detail_name.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

addr_detail_phone = lv.label(addr_detail2)
addr_detail_phone.set_pos(66, 68)
addr_detail_phone.set_size(105, 16)
addr_detail_phone.set_text("18888888888")
addr_detail_phone.set_long_mode(lv.label.LONG.WRAP)
addr_detail_phone.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
addr_detail_phone.add_style(style_font_regular_18_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------menu screen----------------------------------------------------------

menu = lv.obj()

menu2 = lv.obj(menu)
# menu2 = lv.obj()
menu2.center()
menu2.set_size(240, 240)
# menu2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
menu2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

menu_1 = lv.img(menu2)
menu_1.set_pos(0, 0)
menu_1.set_size(240, 240)
menu_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
menu_1_img = "U:/static/normal.png"

menu_1.set_src(menu_1_img)
menu_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

menu_img_4 = lv.img(menu2)
menu_img_4.set_pos(49, 96)
menu_img_4.set_size(32, 16)
menu_img_4.add_flag(lv.obj.FLAG.CLICKABLE)

menu_img_4_img = "U:/static/mp1968072128.png"

menu_img_4.set_src(menu_img_4_img)
menu_img_4.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

menu_phone = lv.imgbtn(menu2)
menu_phone.set_pos(30, 21)
menu_phone.set_size(70, 70)

menu_phone_imgReleased = "U:/static/mp523231338.png"
menu_phone.set_src(lv.imgbtn.STATE.RELEASED, menu_phone_imgReleased, None, None)
menu_phone.set_src(lv.imgbtn.STATE.PRESSED, menu_phone_imgReleased, None, None)
menu_phone.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, menu_phone_imgReleased, None, None)
menu_phone.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, menu_phone_imgReleased, None, None)
menu_phone.add_flag(lv.obj.FLAG.CHECKABLE)
menu_phone.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
menu_phone.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
menu_phone.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

menu_img_6 = lv.img(menu2)
menu_img_6.set_pos(159, 198)
menu_img_6.set_size(32, 16)
menu_img_6.add_flag(lv.obj.FLAG.CLICKABLE)
menu_img_6_img = "U:/static/mp31411395.png"
menu_img_6.set_src(menu_img_6_img)
menu_img_6.set_pivot(0, 0)
menu_img_6.set_angle(0)
menu_img_6.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

menu_img_5 = lv.img(menu2)
menu_img_5.set_pos(40, 198)
menu_img_5.set_size(50, 16)
menu_img_5.add_flag(lv.obj.FLAG.CLICKABLE)
menu_img_5_img = "U:/static/mp-1315051266.png"
menu_img_5.set_src(menu_img_5_img)
menu_img_5.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

menu_msg = lv.imgbtn(menu2)
menu_msg.set_pos(140, 21)
menu_msg.set_size(70, 70)
menu_msg_imgReleased = "U:/static/job_notice.png"
menu_msg.set_src(lv.imgbtn.STATE.RELEASED, menu_msg_imgReleased, None, None)
menu_msg.set_src(lv.imgbtn.STATE.PRESSED, menu_msg_imgReleased, None, None)
menu_msg.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, menu_msg_imgReleased, None, None)
menu_msg.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, menu_msg_imgReleased, None, None)
menu_msg.add_flag(lv.obj.FLAG.CHECKABLE)
menu_msg.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
menu_msg.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
menu_msg.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

menu_img_3 = lv.img(menu2)
menu_img_3.set_pos(159, 96)
menu_img_3.set_size(32, 16)
menu_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
menu_img_3_img = "U:/static/mp-109137215.png"
menu_img_3.set_src(menu_img_3_img)
menu_img_3.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

menu_img_2 = lv.img(menu2)
menu_img_2.set_pos(110, 225)
menu_img_2.set_size(21, 4)
menu_img_2.add_flag(lv.obj.FLAG.CLICKABLE)
menu_img_2_img = "U:/static/mp249033207.png"
menu_img_2.set_src(menu_img_2_img)
menu_img_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

menu_setting = lv.imgbtn(menu2)
menu_setting.set_pos(140, 124)
menu_setting.set_size(70, 70)
menu_setting_imgReleased = "U:/static/mp-1413429395.png"
menu_setting.set_src(lv.imgbtn.STATE.RELEASED, menu_setting_imgReleased, None, None)
menu_setting.set_src(lv.imgbtn.STATE.PRESSED, menu_setting_imgReleased, None, None)
menu_setting.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, menu_setting_imgReleased, None, None)
menu_setting.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, menu_setting_imgReleased, None, None)
menu_setting.add_flag(lv.obj.FLAG.CHECKABLE)
menu_setting.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
menu_setting.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
menu_setting.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

menu_class = lv.imgbtn(menu2)
menu_class.set_pos(30, 124)
menu_class.set_size(70, 70)
menu_class_imgReleased = "U:/static/mp663779948.png"
menu_class.set_src(lv.imgbtn.STATE.RELEASED, menu_class_imgReleased, None, None)
menu_class.set_src(lv.imgbtn.STATE.PRESSED, menu_class_imgReleased, None, None)
menu_class.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, menu_class_imgReleased, None, None)
menu_class.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, menu_class_imgReleased, None, None)
menu_class.add_flag(lv.obj.FLAG.CHECKABLE)
menu_class.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
menu_class.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
menu_class.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

menu_img_10 = lv.img(menu2)
menu_img_10.set_pos(110, 225)
menu_img_10.set_size(21, 4)
menu_img_10.add_flag(lv.obj.FLAG.CLICKABLE)
menu_img_10_img = "U:/static/mp182026454.png"
menu_img_10.set_src(menu_img_10_img)
menu_img_10.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

# -------------------------------------------- menu_2 screen -----------------------------------------------------------
menu_2 = lv.obj()

menu2_2 = lv.obj(menu_2)
# menu2 = lv.obj()
menu2_2.center()
menu2_2.set_size(240, 240)
menu2_2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

menu2_1 = lv.img(menu2_2)
menu2_1.set_pos(0, 0)
menu2_1.set_size(240, 240)
menu2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
menu2_1_img = "U:/static/normal.png"

menu2_1.set_src(menu2_1_img)
menu2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

menu2_img_10 = lv.img(menu2_2)
menu2_img_10.set_pos(150, 198)
menu2_img_10.set_size(50, 16)
menu2_img_10.add_flag(lv.obj.FLAG.CLICKABLE)
menu2_img_10_img = "U:/static/health_code_label.png"
menu2_img_10.set_src(menu2_img_10_img)
menu2_img_10.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

menu2_img_9 = lv.img(menu2_2)
menu2_img_9.set_pos(40, 198)
menu2_img_9.set_size(50, 16)
menu2_img_9.add_flag(lv.obj.FLAG.CLICKABLE)

menu2_img_9_img = "U:/static/mp-550101220.png"

menu2_img_9.set_src(menu2_img_9_img)
menu2_img_9.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

menu2_img_8 = lv.img(menu2_2)
menu2_img_8.set_pos(159, 96)
menu2_img_8.set_size(32, 16)
menu2_img_8.add_flag(lv.obj.FLAG.CLICKABLE)

menu2_img_8_img = "U:/static/mp655812831.png"

menu2_img_8.set_src(menu2_img_8_img)
menu2_img_8.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

menu2_img_7 = lv.img(menu2_2)
menu2_img_7.set_pos(49, 96)
menu2_img_7.set_size(32, 16)
menu2_img_7.add_flag(lv.obj.FLAG.CLICKABLE)
menu2_img_7_img = "U:/static/mp-1561945122.png"
menu2_img_7.set_src(menu2_img_7_img)
menu2_img_7.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

menu2_health_qrcode = lv.imgbtn(menu2_2)
menu2_health_qrcode.set_pos(140, 124)
menu2_health_qrcode.set_size(70, 70)
menu2_health_qrcode_imgReleased = "U:/static/health_qrcode.png"
menu2_health_qrcode.set_src(lv.imgbtn.STATE.RELEASED, menu2_health_qrcode_imgReleased, None, None)
menu2_health_qrcode.set_src(lv.imgbtn.STATE.PRESSED, menu2_health_qrcode_imgReleased, None, None)
menu2_health_qrcode.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, menu2_health_qrcode_imgReleased, None, None)
menu2_health_qrcode.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, menu2_health_qrcode_imgReleased, None, None)
menu2_health_qrcode.add_flag(lv.obj.FLAG.CHECKABLE)
menu2_health_qrcode.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
menu2_health_qrcode.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
menu2_health_qrcode.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

menu2_qrcode = lv.imgbtn(menu2_2)
menu2_qrcode.set_pos(30, 124)
menu2_qrcode.set_size(70, 70)
menu2_qrcode_imgReleased = "U:/static/mp-648479349.png"
menu2_qrcode.set_src(lv.imgbtn.STATE.RELEASED, menu2_qrcode_imgReleased, None, None)
menu2_qrcode.set_src(lv.imgbtn.STATE.PRESSED, menu2_qrcode_imgReleased, None, None)
menu2_qrcode.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, menu2_qrcode_imgReleased, None, None)
menu2_qrcode.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, menu2_qrcode_imgReleased, None, None)
menu2_qrcode.add_flag(lv.obj.FLAG.CHECKABLE)
menu2_qrcode.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
menu2_qrcode.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
menu2_qrcode.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

menu2_shutdown = lv.imgbtn(menu2_2)
menu2_shutdown.set_pos(140, 21)
menu2_shutdown.set_size(70, 70)

menu2_shutdown_imgReleased = "U:/static/mp1428729994.png"
menu2_shutdown.set_src(lv.imgbtn.STATE.RELEASED, menu2_shutdown_imgReleased, None, None)
menu2_shutdown.set_src(lv.imgbtn.STATE.PRESSED, menu2_shutdown_imgReleased, None, None)
menu2_shutdown.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, menu2_shutdown_imgReleased, None, None)
menu2_shutdown.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, menu2_shutdown_imgReleased, None, None)
menu2_shutdown.add_flag(lv.obj.FLAG.CHECKABLE)
menu2_shutdown.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
menu2_shutdown.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
menu2_shutdown.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

menu2_clk = lv.imgbtn(menu_2)
menu2_clk.set_pos(30, 21)
menu2_clk.set_size(70, 70)

menu2_clk_imgReleased = "U:/static/clock.png"
menu2_clk.set_src(lv.imgbtn.STATE.RELEASED, menu2_clk_imgReleased, None, None)
menu2_clk.set_src(lv.imgbtn.STATE.PRESSED, menu2_clk_imgReleased, None, None)
menu2_clk.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, menu2_clk_imgReleased, None, None)
menu2_clk.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, menu2_clk_imgReleased, None, None)
menu2_clk.add_flag(lv.obj.FLAG.CHECKABLE)
menu2_clk.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
menu2_clk.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
menu2_clk.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

menu2_img_10 = lv.img(menu2_2)
menu2_img_10.set_pos(110, 225)
menu2_img_10.set_size(21, 4)
menu2_img_10.add_flag(lv.obj.FLAG.CLICKABLE)
menu2_img_10_img = "U:/static/mp249033207.png"
menu2_img_10.set_src(menu2_img_10_img)
menu2_img_10.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
# --------------------------------------------addr_book screen----------------------------------------------------------
addr_book = lv.obj()

addr_book2 = lv.obj(addr_book)
# addr_book2 = lv.obj()
addr_book2.center()
addr_book2.set_size(240, 240)
# addr_book2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
addr_book2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

addr_book2_1 = lv.img(addr_book2)
addr_book2_1.set_pos(0, 0)
addr_book2_1.set_size(240, 240)
addr_book2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
addr_book2_1_img = "U:/static/normal.png"

addr_book2_1.set_src(addr_book2_1_img)
addr_book2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

addr_book_title = lv.label(addr_book2)
addr_book_title.set_pos(69, 21)
addr_book_title.set_size(96, 21)
addr_book_title.set_text("通讯录")
addr_book_title.set_long_mode(lv.label.LONG.WRAP)
addr_book_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
addr_book_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

addr_book_list_1 = lv.list(addr_book2)
addr_book_list_1.set_pos(18, 54)
addr_book_list_1.set_size(180, 156)

# addr_book_list_1_btn_0_img = "U:/static/mp1480923465.png"
# addr_book_list_1_btn_0 = addr_book_list_1.add_btn(addr_book_list_1_btn_0_img, "三三")
#
# # add style for addr_book_list_1_btn_0
# addr_book_list_1_btn_0.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)
#
# addr_book_list_1_btn_1_img = "U:/static/mp1480923465.png"
# addr_book_list_1_btn_1 = addr_book_list_1.add_btn(addr_book_list_1_btn_1_img, "星星")
#
# # add style for addr_book_list_1_btn_1
# addr_book_list_1_btn_1.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)
#
# addr_book_list_1_btn_2_img = "U:/static/mp1480923465.png"
# addr_book_list_1_btn_2 = addr_book_list_1.add_btn(addr_book_list_1_btn_2_img, "五五")
# addr_book_list_1_btn_2.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)
#
addr_book_list_1.add_style(style_list, lv.PART.MAIN | lv.STATE.DEFAULT)
addr_book_list_1.add_style(style_list_scro, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

# --------------------------------------------class_detail screen----------------------------------------------------
class_detail = lv.obj()

class_detail2 = lv.obj(class_detail)

# class_detail2 = lv.obj()
class_detail2.center()
class_detail2.set_size(240, 240)
# class_detail2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
class_detail2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail2_1 = lv.img(class_detail2)
class_detail2_1.set_pos(0, 0)
class_detail2_1.set_size(240, 240)
class_detail2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
class_detail2_1_img = "U:/static/normal.png"

class_detail2_1.set_src(class_detail2_1_img)
class_detail2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_cont = lv.obj(class_detail2)
class_detail_cont.set_pos(0, 0)
class_detail_cont.set_size(240, 50)
class_detail_cont_style = ContStyle()
class_detail_cont.add_style(
    class_detail_cont_style.style_cont(0, lv.color_make(0x0f, 0x4c, 0x81), lv.color_make(0x0f, 0x4c, 0x81), 255),
    lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_title = lv.label(class_detail_cont)
class_detail_title.set_pos(70, 11)
class_detail_title.set_size(101, 26)
class_detail_title.set_text("星期二")
class_detail_title.set_long_mode(lv.label.LONG.WRAP)
class_detail_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_title.add_style(style_font_regular_24_space_0_white,
                             lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_tileview_1 = lv.tileview(class_detail2)
class_detail_tileview_1.set_pos(0, 50)
class_detail_tileview_1.set_size(240, 190)
class_detail_tileview_1_morning = class_detail_tileview_1.add_tile(0, 0, lv.DIR.RIGHT)
class_detail_line_1 = lv.line(class_detail_tileview_1_morning)
class_detail_line_1.set_pos(58, 0)
class_detail_line_1.set_size(10, 190)
line_points = [
    {"x": 0, "y": 0},
    {"x": 0, "y": 190},
]
class_detail_line_1.set_points(line_points, 2)

class_detail_line_1.add_style(style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_3 = lv.label(class_detail_tileview_1_morning)
class_detail_label_3.set_pos(104, 16)
class_detail_label_3.set_size(100, 27)
class_detail_label_3.set_text("语文")
class_detail_label_3.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_3.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_3.add_style(style_font_regular_18_space_2_white,
                               lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_4 = lv.label(class_detail_tileview_1_morning)
class_detail_label_4.set_pos(104, 64)
class_detail_label_4.set_size(100, 27)
class_detail_label_4.set_text("语文")
class_detail_label_4.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_4.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_4.add_style(style_font_regular_18_space_2_white,
                               lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_5 = lv.label(class_detail_tileview_1_morning)
class_detail_label_5.set_pos(104, 112)
class_detail_label_5.set_size(100, 27)
class_detail_label_5.set_text("数学")
class_detail_label_5.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_5.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_5.add_style(style_font_regular_18_space_2_white,
                               lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_6 = lv.label(class_detail_tileview_1_morning)
class_detail_label_6.set_pos(104, 156)
class_detail_label_6.set_size(100, 27)
class_detail_label_6.set_text("数学")
class_detail_label_6.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_6.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_6.add_style(style_font_regular_18_space_2_white,
                               lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_2 = lv.label(class_detail_tileview_1_morning)
class_detail_label_2.set_pos(10, 66)
class_detail_label_2.set_size(46, 56)
class_detail_label_2.set_text("上午")
class_detail_label_2.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_2.add_style(style_font_regular_24_space_0_white,
                               lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_line_2 = lv.line(class_detail_tileview_1_morning)
class_detail_line_2.set_pos(60, 47)
class_detail_line_2.set_size(180, 10)
line_points = [
    {"x": 0, "y": 0},
    {"x": 180, "y": 0},
]
class_detail_line_2.set_points(line_points, 2)
class_detail_line_2.add_style(style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_line_3 = lv.line(class_detail_tileview_1_morning)
class_detail_line_3.set_pos(60, 94)
class_detail_line_3.set_size(180, 10)
line_points = [
    {"x": 0, "y": 0},
    {"x": 180, "y": 0},
]
class_detail_line_3.set_points(line_points, 2)
class_detail_line_3.add_style(style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_line_4 = lv.line(class_detail_tileview_1_morning)
class_detail_line_4.set_pos(60, 142)
class_detail_line_4.set_size(180, 10)
line_points = [
    {"x": 0, "y": 0},
    {"x": 180, "y": 0},
]
class_detail_line_4.set_points(line_points, 2)
class_detail_line_4.add_style(style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_tileview_1_afternoon = class_detail_tileview_1.add_tile(1, 0, lv.DIR.LEFT | lv.DIR.RIGHT)
class_detail_line_5 = lv.line(class_detail_tileview_1_afternoon)
class_detail_line_5.set_pos(58, 0)
class_detail_line_5.set_size(10, 190)
line_points = [
    {"x": 0, "y": 0},
    {"x": 0, "y": 190},
]
class_detail_line_5.set_points(line_points, 2)
class_detail_line_5.add_style(style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_8 = lv.label(class_detail_tileview_1_afternoon)
class_detail_label_8.set_pos(105, 16)
class_detail_label_8.set_size(100, 25)
class_detail_label_8.set_text("语文")
class_detail_label_8.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_8.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_8.add_style(style_font_regular_18_space_2_white,
                               lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_9 = lv.label(class_detail_tileview_1_afternoon)
class_detail_label_9.set_pos(104, 64)
class_detail_label_9.set_size(100, 25)
class_detail_label_9.set_text("语文")
class_detail_label_9.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_9.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_9.add_style(style_font_regular_18_space_2_white,
                               lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_10 = lv.label(class_detail_tileview_1_afternoon)
class_detail_label_10.set_pos(105, 112)
class_detail_label_10.set_size(100, 25)
class_detail_label_10.set_text("语文")
class_detail_label_10.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_10.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_10.add_style(style_font_regular_18_space_2_white,
                                lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_11 = lv.label(class_detail_tileview_1_afternoon)
class_detail_label_11.set_pos(105, 156)
class_detail_label_11.set_size(100, 25)
class_detail_label_11.set_text("语文")
class_detail_label_11.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_11.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_11.add_style(style_font_regular_18_space_2_white,
                                lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_7 = lv.label(class_detail_tileview_1_afternoon)
class_detail_label_7.set_pos(10, 65)
class_detail_label_7.set_size(46, 56)
class_detail_label_7.set_text("下午")
class_detail_label_7.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_7.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_7.add_style(style_font_regular_24_space_0_white,
                               lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_line_6 = lv.line(class_detail_tileview_1_afternoon)
class_detail_line_6.set_pos(60, 47)
class_detail_line_6.set_size(180, 10)
line_points = [
    {"x": 0, "y": 0},
    {"x": 180, "y": 0},
]
class_detail_line_6.set_points(line_points, 2)
class_detail_line_6.add_style(style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_line_7 = lv.line(class_detail_tileview_1_afternoon)
class_detail_line_7.set_pos(60, 94)
class_detail_line_7.set_size(180, 10)
line_points = [
    {"x": 0, "y": 0},
    {"x": 180, "y": 0},
]
class_detail_line_7.set_points(line_points, 2)
class_detail_line_7.add_style(style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_line_8 = lv.line(class_detail_tileview_1_afternoon)
class_detail_line_8.set_pos(60, 142)
class_detail_line_8.set_size(180, 10)
line_points = [
    {"x": 0, "y": 0},
    {"x": 180, "y": 0},
]
class_detail_line_8.set_points(line_points, 2)
class_detail_line_8.add_style(style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_tileview_1_night = class_detail_tileview_1.add_tile(2, 0, lv.DIR.LEFT)
class_detail_line_9 = lv.line(class_detail_tileview_1_night)
class_detail_line_9.set_pos(58, 0)
class_detail_line_9.set_size(10, 190)
line_points = [
    {"x": 0, "y": 0},
    {"x": 0, "y": 190},
]
class_detail_line_9.set_points(line_points, 2)
class_detail_line_9.add_style(style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_13 = lv.label(class_detail_tileview_1_night)
class_detail_label_13.set_pos(104, 16)
class_detail_label_13.set_size(100, 25)
class_detail_label_13.set_text("语文")
class_detail_label_13.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_13.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_13.add_style(style_font_regular_18_space_2_white,
                                lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_14 = lv.label(class_detail_tileview_1_night)
class_detail_label_14.set_pos(104, 64)
class_detail_label_14.set_size(100, 25)
class_detail_label_14.set_text("语文")
class_detail_label_14.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_14.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_14.add_style(style_font_regular_18_space_2_white,
                                lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_15 = lv.label(class_detail_tileview_1_night)
class_detail_label_15.set_pos(104, 112)
class_detail_label_15.set_size(100, 25)
class_detail_label_15.set_text("语文")
class_detail_label_15.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_15.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_15.add_style(style_font_regular_18_space_2_white,
                                lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_16 = lv.label(class_detail_tileview_1_night)
class_detail_label_16.set_pos(104, 156)
class_detail_label_16.set_size(100, 25)
class_detail_label_16.set_text("语文")
class_detail_label_16.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_16.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_16.add_style(style_font_regular_18_space_2_white,
                                lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_label_12 = lv.label(class_detail_tileview_1_night)
class_detail_label_12.set_pos(10, 65)
class_detail_label_12.set_size(46, 56)
class_detail_label_12.set_text("晚上")
class_detail_label_12.set_long_mode(lv.label.LONG.WRAP)
class_detail_label_12.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
class_detail_label_12.add_style(style_font_regular_24_space_0_white,
                                lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_line_10 = lv.line(class_detail_tileview_1_night)
class_detail_line_10.set_pos(60, 47)
class_detail_line_10.set_size(180, 10)
line_points = [
    {"x": 0, "y": 0},
    {"x": 180, "y": 0},
]
class_detail_line_10.set_points(line_points, 2)
class_detail_line_10.add_style(style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_line_11 = lv.line(class_detail_tileview_1_night)
class_detail_line_11.set_pos(60, 94)
class_detail_line_11.set_size(180, 10)
line_points = [
    {"x": 0, "y": 0},
    {"x": 180, "y": 0},
]
class_detail_line_11.set_points(line_points, 2)
class_detail_line_11.add_style(style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_line_12 = lv.line(class_detail_tileview_1_night)
class_detail_line_12.set_pos(60, 142)
class_detail_line_12.set_size(180, 10)
line_points = [
    {"x": 0, "y": 0},
    {"x": 180, "y": 0},
]
class_detail_line_12.set_points(line_points, 2)
class_detail_line_12.add_style(style_line, lv.PART.MAIN | lv.STATE.DEFAULT)

class_detail_tileview_1.add_style(style_screen2, lv.PART.MAIN | lv.STATE.DEFAULT)
class_detail_tileview_1.add_style(style_scro, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)

# --------------------------------------------class_date screen----------------------------------------------------

class_date = lv.obj()
class_date2 = lv.obj(class_date)

# class_date2 = lv.obj()
class_date2.center()
class_date2.set_size(240, 240)
# class_date2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
class_date2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

class_date2_1 = lv.img(class_date2)
class_date2_1.set_pos(0, 0)
class_date2_1.set_size(240, 240)
class_date2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
class_date2_1_img = "U:/static/normal.png"

class_date2_1.set_src(class_date2_1_img)
class_date2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

class_date_btn_1 = lv.btn(class_date2)
class_date_btn_1.set_pos(17, 32)
class_date_btn_1.set_size(94, 27)
class_date_img_1 = lv.img(class_date_btn_1)
class_date_btn_1.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_img_1.set_pos(0, 6)
class_date_img_1.set_size(15, 15)
class_date_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
class_date_img_1_img = "U:/static/mp-1897490797.png"
class_date_img_1.set_src(class_date_img_1_img)
class_date_img_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_btn_1_label = lv.label(class_date_btn_1)
class_date_btn_1_label.set_pos(25, 0)
class_date_btn_1_label.set_text("星期一")
class_date_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
# class_date_btn_1_label.align(lv.ALIGN.CENTER, 0, 0)
class_date_btn_1_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
class_date_btn_1_label.set_style_text_font(lv.font_regular_24, lv.STATE.DEFAULT)

class_date_btn_2 = lv.btn(class_date2)
class_date_btn_2.set_pos(135, 32)
class_date_btn_2.set_size(94, 27)
class_date_img_2 = lv.img(class_date_btn_2)
class_date_btn_2.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_img_2.set_pos(0, 6)
class_date_img_2.set_size(15, 15)
class_date_img_2.add_flag(lv.obj.FLAG.CLICKABLE)
class_date_img_2_img = "U:/static/mp-814621292.png"
class_date_img_2.set_src(class_date_img_2_img)
class_date_img_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_btn_2_label = lv.label(class_date_btn_2)
class_date_btn_2_label.set_pos(25, 0)
class_date_btn_2_label.set_text("星期二")
class_date_btn_2.set_style_pad_all(0, lv.STATE.DEFAULT)
# class_date_btn_2_label.align(lv.ALIGN.CENTER, 0, 0)
class_date_btn_2_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
class_date_btn_2_label.set_style_text_font(lv.font_regular_24, lv.STATE.DEFAULT)

class_date_btn_3 = lv.btn(class_date2)
class_date_btn_3.set_pos(17, 84)
class_date_btn_3.set_size(94, 27)
class_date_img_3 = lv.img(class_date_btn_3)
class_date_btn_3.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_img_3.set_pos(0, 6)
class_date_img_3.set_size(15, 15)
class_date_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
class_date_img_3_img = "U:/static/mp-814621292.png"
class_date_img_3.set_src(class_date_img_3_img)
class_date_img_3.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_btn_3_label = lv.label(class_date_btn_3)
class_date_btn_3_label.set_pos(25, 0)
class_date_btn_3_label.set_text("星期三")
class_date_btn_3.set_style_pad_all(0, lv.STATE.DEFAULT)
# class_date_btn_3_label.align(lv.ALIGN.CENTER, 0, 0)
class_date_btn_3_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
class_date_btn_3_label.set_style_text_font(lv.font_regular_24, lv.STATE.DEFAULT)

class_date_btn_4 = lv.btn(class_date2)
class_date_btn_4.set_pos(135, 84)
class_date_btn_4.set_size(94, 27)
class_date_img_4 = lv.img(class_date_btn_4)
class_date_btn_4.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_img_4.set_pos(0, 6)
class_date_img_4.set_size(15, 15)
class_date_img_4.add_flag(lv.obj.FLAG.CLICKABLE)
class_date_img_4_img = "U:/static/mp-814621292.png"
class_date_img_4.set_src(class_date_img_4_img)
class_date_img_4.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_btn_4_label = lv.label(class_date_btn_4)
class_date_btn_4_label.set_pos(25, 0)
class_date_btn_4_label.set_text("星期四")
class_date_btn_4.set_style_pad_all(0, lv.STATE.DEFAULT)
# class_date_btn_4_label.align(lv.ALIGN.CENTER, 0, 0)
class_date_btn_4_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
class_date_btn_4_label.set_style_text_font(lv.font_regular_24, lv.STATE.DEFAULT)

class_date_btn_5 = lv.btn(class_date2)
class_date_btn_5.set_pos(17, 138)
class_date_btn_5.set_size(94, 27)
class_date_img_5 = lv.img(class_date_btn_5)
class_date_btn_5.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_img_5.set_pos(0, 6)
class_date_img_5.set_size(15, 15)
class_date_img_5.add_flag(lv.obj.FLAG.CLICKABLE)
class_date_img_5_img = "U:/static/mp-814621292.png"
class_date_img_5.set_src(class_date_img_5_img)
class_date_img_5.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_btn_5_label = lv.label(class_date_btn_5)
class_date_btn_5_label.set_pos(25, 0)
class_date_btn_5_label.set_text("星期五")
class_date_btn_5.set_style_pad_all(0, lv.STATE.DEFAULT)
# class_date_btn_5_label.align(lv.ALIGN.CENTER, 0, 0)
class_date_btn_5_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
class_date_btn_5_label.set_style_text_font(lv.font_regular_24, lv.STATE.DEFAULT)

class_date_btn_6 = lv.btn(class_date2)
class_date_btn_6.set_pos(135, 138)
class_date_btn_6.set_size(94, 27)
class_date_img_6 = lv.img(class_date_btn_6)
class_date_btn_6.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_img_6.set_pos(0, 6)
class_date_img_6.set_size(15, 15)
class_date_img_6.add_flag(lv.obj.FLAG.CLICKABLE)
class_date_img_6_img = "U:/static/mp-814621292.png"
class_date_img_6.set_src(class_date_img_6_img)
class_date_img_6.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_btn_6_label = lv.label(class_date_btn_6)
class_date_btn_6_label.set_pos(25, 0)
class_date_btn_6_label.set_text("星期六")
class_date_btn_6.set_style_pad_all(0, lv.STATE.DEFAULT)
# class_date_btn_6_label.align(lv.ALIGN.CENTER, 0, 0)
class_date_btn_6_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
class_date_btn_6_label.set_style_text_font(lv.font_regular_24, lv.STATE.DEFAULT)

class_date_btn_7 = lv.btn(class_date2)
class_date_btn_7.set_pos(17, 195)
class_date_btn_7.set_size(94, 27)
class_date_img_7 = lv.img(class_date_btn_7)
class_date_btn_7.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_img_7.set_pos(0, 6)
class_date_img_7.set_size(15, 15)
class_date_img_7.add_flag(lv.obj.FLAG.CLICKABLE)
class_date_img_7_img = "U:/static/mp-814621292.png"
class_date_img_7.set_src(class_date_img_7_img)
class_date_img_7.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
class_date_btn_7_label = lv.label(class_date_btn_7)
class_date_btn_7_label.set_pos(25, 0)
class_date_btn_7_label.set_text("星期日")
class_date_btn_7.set_style_pad_all(0, lv.STATE.DEFAULT)
# class_date_btn_7_label.align(lv.ALIGN.CENTER, 0, 0)
class_date_btn_7_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
class_date_btn_7_label.set_style_text_font(lv.font_regular_24, lv.STATE.DEFAULT)
# --------------------------------------------call_log screen----------------------------------------------------
call_log = lv.obj()
call_log2 = lv.obj(call_log)
# call_log2 = lv.obj()
call_log2.center()
call_log2.set_size(240, 240)
# call_log2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
call_log2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

call_log_1 = lv.img(call_log2)
call_log_1.set_pos(0, 0)
call_log_1.set_size(240, 240)
call_log_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
call_log_1_img = "U:/static/normal.png"

call_log_1.set_src(call_log_1_img)
call_log_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

call_log_title = lv.label(call_log2)
call_log_title.set_pos(69, 21)
call_log_title.set_size(96, 21)
call_log_title.set_text("通话记录")
call_log_title.set_long_mode(lv.label.LONG.WRAP)
call_log_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
call_log_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

call_log_list_1 = lv.list(call_log2)
call_log_list_1.set_pos(18, 54)
call_log_list_1.set_size(180, 156)
# --------------------------------------------msg_detail screen----------------------------------------------------
msg_detail = lv.obj()
msg_detail2 = lv.obj(msg_detail)
# msg_detail2 = lv.obj()
msg_detail2.center()
msg_detail2.set_size(240, 240)
# msg_detail2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
msg_detail2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

msg_detail2_1 = lv.img(msg_detail2)
msg_detail2_1.set_pos(0, 0)
msg_detail2_1.set_size(240, 240)
msg_detail2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
msg_detail2_1_img = "U:/static/normal.png"

msg_detail2_1.set_src(msg_detail2_1_img)
msg_detail2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

msg_detail_name = lv.label(msg_detail2)
msg_detail_name.set_pos(72, 21)
msg_detail_name.set_size(96, 21)
msg_detail_name.set_text("作业通知")
msg_detail_name.set_long_mode(lv.label.LONG.WRAP)
msg_detail_name.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
msg_detail_name.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

msg_detail_cont_1 = lv.obj(msg_detail2)
msg_detail_cont_1.set_pos(0, 55)
msg_detail_cont_1.set_size(240, 185)
msg_detail_cont_style = ContStyle()
msg_detail_cont_1.add_style(
    msg_detail_cont_style.style_cont(0, lv.color_make(0x2f, 0x2d, 0x2d), lv.color_make(0x2f, 0x2d, 0x2d), 255),
    lv.PART.MAIN | lv.STATE.DEFAULT)

msg_detail_msg = lv.label(msg_detail_cont_1)
msg_detail_msg.set_text(
    "语文: \r\n"
    "1.3号本写12课生字\r\n"
    "2.高分突破P62\r\n "
    "数学: \r\n 1.完成课本P78\r\n 2.计算达人P62,P63\r\n 3.天天练 预习与写题\r\n 4. 背诵课文, 预习备课")
msg_detail_msg.set_long_mode(lv.label.LONG.WRAP)
msg_detail_msg.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
msg_detail_msg.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)
# --------------------------------------------setting screen----------------------------------------------------
setting_scr = lv.obj()
setting_scr2 = lv.obj(setting_scr)
# setting_scr2 = lv.obj()
setting_scr2.center()
setting_scr2.set_size(240, 240)
# setting_scr2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
setting_scr2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)
setting_scr2.clear_flag(lv.obj.FLAG.SCROLLABLE)

setting_scr2_1 = lv.img(setting_scr2)
setting_scr2_1.set_pos(0, 0)
setting_scr2_1.set_size(240, 240)
setting_scr2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
setting_scr2_1_img = "U:/static/normal.png"

setting_scr2_1.set_src(setting_scr2_1_img)
setting_scr2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_title = lv.label(setting_scr2)
setting_scr_title.set_pos(69, 21)
setting_scr_title.set_size(96, 21)
setting_scr_title.set_text("设置")
setting_scr_title.set_long_mode(lv.label.LONG.WRAP)
setting_scr_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
setting_scr_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_cont_1 = lv.obj(setting_scr2)
setting_scr_cont_1.set_pos(0, 50)
setting_scr_cont_1.set_size(240, 199)
setting_cont_style = ContStyle()
setting_scr_cont_1.add_style(
    setting_cont_style.style_cont(0, lv.color_make(0x2f, 0x2d, 0x2d), lv.color_make(0x2f, 0x2d, 0x2d), 255),
    lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_btn_1 = lv.btn(setting_scr_cont_1)
setting_scr_btn_1.set_pos(100, 20)
setting_scr_btn_1.set_size(124, 38)
setting_scr_btn_1_label = lv.label(setting_scr_btn_1)
setting_scr_btn_1_label.set_text("音量")
setting_scr_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
setting_scr_btn_1_label.align(lv.ALIGN.LEFT_MID, 0, 0)
setting_scr_btn_1_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
setting_scr_btn_1_label.set_style_text_font(lv.font_regular_20, lv.STATE.DEFAULT)
setting_scr_btn_1.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_btn_2 = lv.btn(setting_scr_cont_1)
setting_scr_btn_2.set_pos(100, 80)
setting_scr_btn_2.set_size(124, 38)
setting_scr_btn_2_label = lv.label(setting_scr_btn_2)
setting_scr_btn_2_label.set_text("显示")
setting_scr_btn_2.set_style_pad_all(0, lv.STATE.DEFAULT)
setting_scr_btn_2_label.align(lv.ALIGN.LEFT_MID, 0, 0)
setting_scr_btn_2_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
setting_scr_btn_2_label.set_style_text_font(lv.font_regular_20, lv.STATE.DEFAULT)
setting_scr_btn_2.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_btn_3 = lv.btn(setting_scr_cont_1)
setting_scr_btn_3.set_pos(100, 140)
setting_scr_btn_3.set_size(69, 38)
setting_scr_btn_3_label = lv.label(setting_scr_btn_3)
setting_scr_btn_3_label.set_text("壁纸")
setting_scr_btn_3.set_style_pad_all(0, lv.STATE.DEFAULT)
setting_scr_btn_3_label.align(lv.ALIGN.LEFT_MID, 0, 0)
setting_scr_btn_3_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
setting_scr_btn_3_label.set_style_text_font(lv.font_regular_20, lv.STATE.DEFAULT)
setting_scr_btn_3.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_btn_4 = lv.btn(setting_scr_cont_1)
setting_scr_btn_4.set_pos(100, 200)
setting_scr_btn_4.set_size(69, 38)
setting_scr_btn_4_label = lv.label(setting_scr_btn_4)
setting_scr_btn_4_label.set_text("时间")
setting_scr_btn_4.set_style_pad_all(0, lv.STATE.DEFAULT)
setting_scr_btn_4_label.align(lv.ALIGN.LEFT_MID, 0, 0)
setting_scr_btn_4_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
setting_scr_btn_4_label.set_style_text_font(lv.font_regular_20, lv.STATE.DEFAULT)
setting_scr_btn_4.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_btn_5 = lv.btn(setting_scr_cont_1)
setting_scr_btn_5.set_pos(100, 260)
setting_scr_btn_5.set_size(124, 38)
setting_scr_btn_5_label = lv.label(setting_scr_btn_5)
setting_scr_btn_5_label.set_text("情景模式")
setting_scr_btn_5.set_style_pad_all(0, lv.STATE.DEFAULT)
setting_scr_btn_5_label.align(lv.ALIGN.LEFT_MID, 0, 0)
setting_scr_btn_5_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
setting_scr_btn_5_label.set_style_text_font(lv.font_regular_20, lv.STATE.DEFAULT)
setting_scr_btn_5.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_btn_6 = lv.btn(setting_scr_cont_1)
setting_scr_btn_6.set_pos(100, 320)
setting_scr_btn_6.set_size(124, 38)
setting_scr_btn_6_label = lv.label(setting_scr_btn_6)
setting_scr_btn_6_label.set_text("版本更新")
setting_scr_btn_6.set_style_pad_all(0, lv.STATE.DEFAULT)
setting_scr_btn_6_label.align(lv.ALIGN.LEFT_MID, 0, 0)
setting_scr_btn_6_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
setting_scr_btn_6_label.set_style_text_font(lv.font_regular_20, lv.STATE.DEFAULT)
setting_scr_btn_6.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_btn_7 = lv.btn(setting_scr_cont_1)
setting_scr_btn_7.set_pos(100, 380)
setting_scr_btn_7.set_size(124, 38)
setting_scr_btn_7_label = lv.label(setting_scr_btn_7)
setting_scr_btn_7_label.set_text("关于设备")
setting_scr_btn_7.set_style_pad_all(0, lv.STATE.DEFAULT)
setting_scr_btn_7_label.align(lv.ALIGN.LEFT_MID, 0, 0)
setting_scr_btn_7_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
setting_scr_btn_7_label.set_style_text_font(lv.font_regular_20, lv.STATE.DEFAULT)
setting_scr_btn_7.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_btn_8 = lv.btn(setting_scr_cont_1)
setting_scr_btn_8.set_pos(100, 440)
setting_scr_btn_8.set_size(124, 38)
setting_scr_btn_8_label = lv.label(setting_scr_btn_8)
setting_scr_btn_8_label.set_text("清除通话记录")
setting_scr_btn_8.set_style_pad_all(0, lv.STATE.DEFAULT)
setting_scr_btn_8_label.align(lv.ALIGN.LEFT_MID, 0, 0)
setting_scr_btn_8_label.set_style_text_color(lv.color_make(0xff, 0xff, 0xff), lv.STATE.DEFAULT)
setting_scr_btn_8_label.set_style_text_font(lv.font_regular_20, lv.STATE.DEFAULT)
setting_scr_btn_8.add_style(style_btn, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_img_8 = lv.img(setting_scr_cont_1)
setting_scr_img_8.set_pos(35, 22)
setting_scr_img_8.set_size(40, 40)
setting_scr_img_8.add_flag(lv.obj.FLAG.CLICKABLE)
setting_scr_img_8_img = "U:/static/mp350979546.png"
setting_scr_img_8.set_src(setting_scr_img_8_img)
setting_scr_img_8.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_img_1 = lv.img(setting_scr_cont_1)
setting_scr_img_1.set_pos(35, 82)
setting_scr_img_1.set_size(40, 40)
setting_scr_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
setting_scr_img_1_img = "U:/static/mp340914952.png"
setting_scr_img_1.set_src(setting_scr_img_1_img)
setting_scr_img_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_img_3 = lv.img(setting_scr_cont_1)
setting_scr_img_3.set_pos(35, 142)
setting_scr_img_3.set_size(40, 40)
setting_scr_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
setting_scr_img_3_img = "U:/static/mp56820649.png"
setting_scr_img_3.set_src(setting_scr_img_3_img)
setting_scr_img_3.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_img_2 = lv.img(setting_scr_cont_1)
setting_scr_img_2.set_pos(35, 202)
setting_scr_img_2.set_size(40, 40)
setting_scr_img_2.add_flag(lv.obj.FLAG.CLICKABLE)
setting_scr_img_2_img = "U:/static/mp-2057631494.png"
setting_scr_img_2.set_src(setting_scr_img_2_img)
setting_scr_img_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_img_6 = lv.img(setting_scr_cont_1)
setting_scr_img_6.set_pos(35, 262)
setting_scr_img_6.set_size(40, 40)
setting_scr_img_6.add_flag(lv.obj.FLAG.CLICKABLE)
setting_scr_img_6_img = "U:/static/mp-511367957.png"
setting_scr_img_6.set_src(setting_scr_img_6_img)
setting_scr_img_6.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_img_5 = lv.img(setting_scr_cont_1)
setting_scr_img_5.set_pos(35, 322)
setting_scr_img_5.set_size(40, 40)
setting_scr_img_5.add_flag(lv.obj.FLAG.CLICKABLE)
setting_scr_img_5_img = "U:/static/mp1943906810.png"
setting_scr_img_5.set_src(setting_scr_img_5_img)
setting_scr_img_5.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_img_4 = lv.img(setting_scr_cont_1)
setting_scr_img_4.set_pos(35, 382)
setting_scr_img_4.set_size(40, 40)
setting_scr_img_4.add_flag(lv.obj.FLAG.CLICKABLE)
setting_scr_img_4_img = "U:/static/mp-1079556563.png"
setting_scr_img_4.set_src(setting_scr_img_4_img)
setting_scr_img_4.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

setting_scr_img_7 = lv.img(setting_scr_cont_1)
setting_scr_img_7.set_pos(35, 442)
setting_scr_img_7.set_size(40, 40)
setting_scr_img_7.add_flag(lv.obj.FLAG.CLICKABLE)
setting_scr_img_7_img = "U:/static/mp-433207078.png"
setting_scr_img_7.set_src(setting_scr_img_7_img)
setting_scr_img_7.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------clk_list screen----------------------------------------------------
clk_list = lv.obj()
clk_list2 = lv.obj(clk_list)
# clk_list2 = lv.obj()
clk_list2.center()
clk_list2.set_size(240, 240)
# clk_list2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
clk_list2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_list2_1 = lv.img(clk_list2)
clk_list2_1.set_pos(0, 0)
clk_list2_1.set_size(240, 240)
clk_list2_1.add_flag(lv.obj.FLAG.CLICKABLE)
# 背景图片
clk_list2_1_img = "U:/static/normal.png"

clk_list2_1.set_src(clk_list2_1_img)
clk_list2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_list_title = lv.label(clk_list2)
clk_list_title.set_pos(69, 18)
clk_list_title.set_size(96, 21)
clk_list_title.set_text("闹钟列表")
clk_list_title.set_long_mode(lv.label.LONG.WRAP)
clk_list_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
clk_list_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_list_imgbtn_cont_1 = lv.obj(clk_list2)
clk_list_imgbtn_cont_1.set_pos(0, 55)
clk_list_imgbtn_cont_1.set_size(60, 180)
clk_list_imgbtn_cont_1.add_flag(lv.obj.FLAG.CLICKABLE)
clk_list_imgbtn_cont_style = ContStyle()
clk_list_imgbtn_cont_1.add_style(
    clk_list_imgbtn_cont_style.style_cont(0, lv.color_make(0x2f, 0x2d, 0x2d), lv.color_make(0x2f, 0x2d, 0x2d), 255),
    lv.PART.MAIN | lv.STATE.DEFAULT)
clk_list_imgbtn_1 = lv.img(clk_list_imgbtn_cont_1)
clk_list_imgbtn_1.set_pos(10, 70)
clk_list_imgbtn_1.set_size(40, 40)
clk_list_imgbtn_1.set_src("U:/static/mp1361446723.png")
clk_list_imgbtn_1.add_flag(lv.obj.FLAG.CLICKABLE)

clk_list_line_1 = lv.line(clk_list2)
clk_list_line_1.set_pos(57, 59)
clk_list_line_1.set_size(20, 180)
line_points = [
    {"x": 0, "y": 0},
    {"x": 0, "y": 170},
]
clk_list_line_1.set_points(line_points, 2)
clk_list_line_1.add_style(style_line2, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_list_cont = lv.obj(clk_list2)
clk_list_cont.set_pos(66, 57)
clk_list_cont.set_size(165, 173)
clk_list_cont_style = ContStyle()
clk_list_cont.add_style(
    clk_list_cont_style.style_cont(0, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 0),
    lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------new_edit_clk screen----------------------------------------------------
# 编辑闹钟则更改new_edit_clk_title.set_text("编辑闹钟"),new_edit_clk_imgbtn_1.set_src  mp-775222478
new_edit_clk = lv.obj()

new_edit_clk2 = lv.obj(new_edit_clk)
# new_edit_clk2 = lv.obj()
new_edit_clk2.center()
new_edit_clk2.set_size(240, 240)
# new_edit_clk2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
new_edit_clk2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

new_edit_clk2_1 = lv.img(new_edit_clk2)
new_edit_clk2_1.set_pos(0, 0)
new_edit_clk2_1.set_size(240, 240)
new_edit_clk2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
new_edit_clk2_1_img = "U:/static/normal.png"
new_edit_clk2_1.set_src(new_edit_clk2_1_img)
new_edit_clk2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

new_edit_clk_title = lv.label(new_edit_clk2)
new_edit_clk_title.set_pos(69, 18)
new_edit_clk_title.set_size(96, 21)
new_edit_clk_title.set_text("新建闹钟")
new_edit_clk_title.set_long_mode(lv.label.LONG.WRAP)
new_edit_clk_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
new_edit_clk_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

new_edit_clk_line_1 = lv.line(new_edit_clk2)
new_edit_clk_line_1.set_pos(57, 59)
new_edit_clk_line_1.set_size(20, 180)
line_points = [
    {"x": 0, "y": 0},
    {"x": 0, "y": 170},
]
new_edit_clk_line_1.set_points(line_points, 2)
new_edit_clk_line_1.add_style(style_line2, lv.PART.MAIN | lv.STATE.DEFAULT)

new_edit_clk_cont_1 = lv.obj(new_edit_clk2)
new_edit_clk_cont_1.set_pos(69, 60)
new_edit_clk_cont_1.set_size(160, 50)

new_edit_clk_img_2 = lv.imgbtn(new_edit_clk_cont_1)
new_edit_clk_img_2.set_pos(123, 8)
new_edit_clk_img_2.set_size(33, 35)
new_edit_clk_img_2.add_flag(lv.obj.FLAG.CHECKABLE)

new_edit_clk_img_2.set_src(lv.imgbtn.STATE.RELEASED, "U:/static/mp-70920201.png", None, None)
new_edit_clk_img_2.set_src(lv.imgbtn.STATE.PRESSED, "U:/static/mp-70920201.png", None, None)
new_edit_clk_img_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, "U:/static/mp-70920201.png", None, None)
new_edit_clk_img_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, "U:/static/mp-70920201.png", None, None)
new_edit_clk_img_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
new_edit_clk_img_2.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
new_edit_clk_img_2.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

new_edit_clk_label_4 = lv.label(new_edit_clk_cont_1)
new_edit_clk_label_4.set_pos(8, 17)
new_edit_clk_label_4.set_size(90, 18)
new_edit_clk_label_4.set_text("14:02AM")
new_edit_clk_label_4.set_long_mode(lv.label.LONG.WRAP)
new_edit_clk_label_4.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
new_edit_clk_label_4.add_style(style_font_regular_18_space_2_white,
                               lv.PART.MAIN | lv.STATE.DEFAULT)
new_edit_clk_cont_1_style = ContStyle()
new_edit_clk_cont_1.add_style(
    new_edit_clk_cont_1_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

new_edit_clk_cont_2 = lv.obj(new_edit_clk2)
new_edit_clk_cont_2.set_pos(69, 120)
new_edit_clk_cont_2.set_size(160, 50)
new_edit_clk_img_3 = lv.imgbtn(new_edit_clk_cont_2)
new_edit_clk_img_3.set_pos(123, 8)
new_edit_clk_img_3.set_size(33, 35)
new_edit_clk_img_3.add_flag(lv.obj.FLAG.CHECKABLE)

new_edit_clk_img_3.set_src(lv.imgbtn.STATE.RELEASED, "U:/static/mp-70920201.png", None, None)
new_edit_clk_img_3.set_src(lv.imgbtn.STATE.PRESSED, "U:/static/mp-70920201.png", None, None)
new_edit_clk_img_3.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, "U:/static/mp-70920201.png", None, None)
new_edit_clk_img_3.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, "U:/static/mp-70920201.png", None, None)
new_edit_clk_img_3.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
new_edit_clk_img_3.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
new_edit_clk_img_3.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

new_edit_clk_label_2_5 = lv.label(new_edit_clk_cont_2)
new_edit_clk_label_2_5.set_pos(10, 18)
new_edit_clk_label_2_5.set_size(122, 18)
new_edit_clk_label_2_5.set_text("铃声")
new_edit_clk_label_2_5.set_long_mode(lv.label.LONG.WRAP)
new_edit_clk_label_2_5.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
new_edit_clk_label_2_5.add_style(style_font_regular_18_space_2_white,
                                 lv.PART.MAIN | lv.STATE.DEFAULT)
new_edit_clk_cont_2_style = ContStyle()
new_edit_clk_cont_2.add_style(
    new_edit_clk_cont_2_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

new_edit_clk_cont_3 = lv.obj(new_edit_clk2)
new_edit_clk_cont_3.set_pos(69, 179)
new_edit_clk_cont_3.set_size(160, 50)
new_edit_clk_img_4 = lv.imgbtn(new_edit_clk_cont_3)
new_edit_clk_img_4.set_pos(123, 8)
new_edit_clk_img_4.set_size(33, 35)
new_edit_clk_img_4.add_flag(lv.obj.FLAG.CHECKABLE)

new_edit_clk_img_4.set_src(lv.imgbtn.STATE.RELEASED, "U:/static/mp-70920201.png", None, None)
new_edit_clk_img_4.set_src(lv.imgbtn.STATE.PRESSED, "U:/static/mp-70920201.png", None, None)
new_edit_clk_img_4.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, "U:/static/mp-70920201.png", None, None)
new_edit_clk_img_4.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, "U:/static/mp-70920201.png", None, None)
new_edit_clk_img_4.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
new_edit_clk_img_4.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
new_edit_clk_img_4.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

new_edit_clk_label_3_5 = lv.label(new_edit_clk_cont_3)
new_edit_clk_label_3_5.set_pos(12, 17)
new_edit_clk_label_3_5.set_size(90, 18)
new_edit_clk_label_3_5.set_text("铃声")
new_edit_clk_label_3_5.set_long_mode(lv.label.LONG.WRAP)
new_edit_clk_label_3_5.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
new_edit_clk_label_3_5.add_style(style_font_regular_18_space_2_white,
                                 lv.PART.MAIN | lv.STATE.DEFAULT)

new_edit_clk_cont_3_style = ContStyle()
new_edit_clk_cont_3.add_style(
    new_edit_clk_cont_3_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

new_edit_clk_imgbtn_1 = lv.imgbtn(new_edit_clk2)
new_edit_clk_imgbtn_1.set_pos(9, 125)
new_edit_clk_imgbtn_1.set_size(40, 40)
new_edit_clk_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, "U:/static/mp398891043.png", None, None)
new_edit_clk_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, "U:/static/mp398891043.png", None, None)
new_edit_clk_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, "U:/static/mp398891043.png", None, None)
new_edit_clk_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, "U:/static/mp398891043.png", None, None)
new_edit_clk_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
new_edit_clk_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
new_edit_clk_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
new_edit_clk_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

# --------------------------------------------clk_time screen----------------------------------------------------
clk_time = lv.obj()

clk_time2 = lv.obj(clk_time)
# clk_time2 = lv.obj()
clk_time2.center()
clk_time2.set_size(240, 240)
# clk_time2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
clk_time2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_time_label_4 = lv.label(clk_time2)
clk_time_label_4.set_pos(116, 102)
clk_time_label_4.set_size(13, 25)
clk_time_label_4.set_text(":")
clk_time_label_4.set_long_mode(lv.label.LONG.WRAP)
clk_time_label_4.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)

clk_time_label_4.add_style(style_font_regular_20_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

# create style style_clk_time_roller_main_main_default
style_clk_time_roller_main_main_default = lv.style_t()
style_clk_time_roller_main_main_default.init()
style_clk_time_roller_main_main_default.set_radius(6)
style_clk_time_roller_main_main_default.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
style_clk_time_roller_main_main_default.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
style_clk_time_roller_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_clk_time_roller_main_main_default.set_bg_opa(102)
style_clk_time_roller_main_main_default.set_border_color(lv.color_make(0xff, 0xff, 0xff))
style_clk_time_roller_main_main_default.set_border_width(0)
style_clk_time_roller_main_main_default.set_text_color(lv.color_make(0x33, 0x33, 0x33))

# create style style_clk_time_roller_main_selected_default
style_clk_time_roller_main_selected_default = lv.style_t()
style_clk_time_roller_main_selected_default.init()
style_clk_time_roller_main_selected_default.set_bg_color(lv.color_make(0xff, 0xff, 0xff))
style_clk_time_roller_main_selected_default.set_bg_grad_color(lv.color_make(0xff, 0xff, 0xff))
style_clk_time_roller_main_selected_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_clk_time_roller_main_selected_default.set_bg_opa(255)
style_clk_time_roller_main_selected_default.set_text_color(lv.color_make(0x33, 0x33, 0x33))

imgbtn_ok = lv.imgbtn(clk_time2)
imgbtn_ok.set_pos(107, 194)
imgbtn_ok.set_size(30, 30)
imgbtn_ok.add_flag(lv.obj.FLAG.CHECKABLE)

imgbtn_ok.set_src(lv.imgbtn.STATE.RELEASED, "U:/static/mp-1364748740.png", None, None)
imgbtn_ok.set_src(lv.imgbtn.STATE.PRESSED, "U:/static/mp-1364748740.png", None, None)
imgbtn_ok.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, "U:/static/mp-1364748740.png", None, None)
imgbtn_ok.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, "U:/static/mp-1364748740.png", None, None)
imgbtn_ok.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
imgbtn_ok.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
imgbtn_ok.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

clk_time_roller_1 = lv.roller(clk_time2)
clk_time_roller_1.set_pos(47, 60)
clk_time_roller_1.set_options(
    "00\n01\n02\n03\n04\n05\n06\n07\n08\n09\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23",
    lv.roller.MODE.NORMAL)
clk_time_roller_1.set_visible_row_count(3)

clk_time_roller_1.set_style_text_font(lv.font_regular_18, lv.PART.MAIN | lv.STATE.DEFAULT)
clk_time_roller_1.set_style_text_font(lv.font_regular_18, lv.PART.MAIN | lv.STATE.FOCUSED)
clk_time_roller_1.set_style_text_font(lv.font_regular_18, lv.PART.SELECTED | lv.STATE.DEFAULT)

# add style for clk_time_roller_1
clk_time_roller_1.add_style(style_clk_time_roller_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)
# add style for clk_time_roller_1
clk_time_roller_1.add_style(style_clk_time_roller_main_selected_default, lv.PART.SELECTED | lv.STATE.DEFAULT)

clk_time_roller_2 = lv.roller(clk_time2)
clk_time_roller_2.set_pos(147, 60)
clk_time_roller_2.set_options(
    "00\n01\n02\n03\n04\n05\n06\n07\n08\n09\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n31\n30\n31\n32\n33\n34\n35\n36\n37\n38\n39\n40\n41\n42\n43\n44\n45\n46\n47\n48\n49\n50\n51\n52\n53\n54\n55\n56\n57\n58\n59",
    lv.roller.MODE.NORMAL)
clk_time_roller_2.set_visible_row_count(3)

clk_time_roller_2.set_style_text_font(lv.font_regular_18, lv.PART.MAIN | lv.STATE.DEFAULT)
clk_time_roller_2.set_style_text_font(lv.font_regular_18, lv.PART.MAIN | lv.STATE.FOCUSED)
clk_time_roller_2.set_style_text_font(lv.font_regular_18, lv.PART.SELECTED | lv.STATE.DEFAULT)

# add style for clk_time_roller_2
clk_time_roller_2.add_style(style_clk_time_roller_main_main_default, lv.PART.MAIN | lv.STATE.DEFAULT)
# add style for clk_time_roller_2
clk_time_roller_2.add_style(style_clk_time_roller_main_selected_default, lv.PART.SELECTED | lv.STATE.DEFAULT)

# --------------------------------------------clk_period screen----------------------------------------------------
clk_period = lv.obj()

clk_period2 = lv.obj(clk_period)
# clk_period2 = lv.obj()
clk_period2.center()
clk_period2.set_size(240, 240)
clk_period2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)
clk_period2.clear_flag(lv.obj.FLAG.SCROLLABLE)

clk_period2_1 = lv.img(clk_period2)
clk_period2_1.set_pos(0, 0)
clk_period2_1.set_size(240, 240)
clk_period2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
clk_period2_1_img = "U:/static/normal.png"

clk_period2_1.set_src(clk_period2_1_img)
clk_period2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_cont = lv.obj(clk_period2)
clk_period_cont.set_pos(0, 50)
clk_period_cont.set_size(240, 199)
clk_period_cont_style = ContStyle()
clk_period_cont.add_style(
    clk_period_cont_style.style_cont(0, lv.color_make(0x2f, 0x2d, 0x2d), lv.color_make(0x2f, 0x2d, 0x2d), 255),
    lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_title = lv.label(clk_period2)
clk_period_title.set_pos(69, 18)
clk_period_title.set_size(96, 21)
clk_period_title.set_text("闹钟周期")
clk_period_title.set_long_mode(lv.label.LONG.WRAP)
clk_period_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)

clk_period_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_cont_1 = lv.obj(clk_period_cont)
clk_period_cont_1.set_pos(17, 13)
clk_period_cont_1.set_size(205, 50)
clk_period_img_1 = lv.img(clk_period_cont_1)
clk_period_img_1.set_pos(158, 8)
clk_period_img_1.set_size(30, 30)
clk_period_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

clk_period_img_1_img = "U:/static/mp-1364748740.png"

clk_period_img_1.set_src(clk_period_img_1_img)

clk_period_img_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_label_1 = lv.label(clk_period_cont_1)
clk_period_label_1.set_pos(18, 15)
clk_period_label_1.set_size(79, 18)
clk_period_label_1.set_text("星期一")
clk_period_label_1.set_long_mode(lv.label.LONG.WRAP)
clk_period_label_1.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
clk_period_label_1.add_style(style_font_regular_18_space_2_white,
                             lv.PART.MAIN | lv.STATE.DEFAULT)
clk_period_cont_1_style = ContStyle()
clk_period_cont_1.add_style(
    clk_period_cont_1_style.style_cont(10, lv.color_make(0xff, 0xff, 0xff), lv.color_make(0xa8, 0xba, 0xf0), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_cont_2 = lv.obj(clk_period_cont)
clk_period_cont_2.set_pos(17, 71)
clk_period_cont_2.set_size(205, 50)
clk_period_img_2 = lv.img(clk_period_cont_2)
clk_period_img_2.set_pos(158, 11)
clk_period_img_2.set_size(30, 30)
clk_period_img_2.add_flag(lv.obj.FLAG.CLICKABLE)

clk_period_img_2_img = "U:/static/mp-861665386.png"

clk_period_img_2.set_src(clk_period_img_2_img)
clk_period_img_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_label_2 = lv.label(clk_period_cont_2)
clk_period_label_2.set_pos(18, 18)
clk_period_label_2.set_size(75, 18)
clk_period_label_2.set_text("星期二")
clk_period_label_2.set_long_mode(lv.label.LONG.WRAP)
clk_period_label_2.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
clk_period_label_2.add_style(style_font_regular_18_space_2_white,
                             lv.PART.MAIN | lv.STATE.DEFAULT)
clk_period_cont_2_style = ContStyle()
clk_period_cont_2.add_style(
    clk_period_cont_2_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_cont_3 = lv.obj(clk_period_cont)
clk_period_cont_3.set_pos(17, 129)
clk_period_cont_3.set_size(205, 50)
clk_period_img_3 = lv.img(clk_period_cont_3)
clk_period_img_3.set_pos(159, 9)
clk_period_img_3.set_size(30, 30)
clk_period_img_3.add_flag(lv.obj.FLAG.CLICKABLE)

clk_period_img_3_img = "U:/static/mp-861665386.png"

clk_period_img_3.set_src(clk_period_img_3_img)
clk_period_img_3.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_label_3 = lv.label(clk_period_cont_3)
clk_period_label_3.set_pos(18, 16)
clk_period_label_3.set_size(72, 18)
clk_period_label_3.set_text("星期三")
clk_period_label_3.set_long_mode(lv.label.LONG.WRAP)
clk_period_label_3.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
clk_period_label_3.add_style(style_font_regular_18_space_2_white,
                             lv.PART.MAIN | lv.STATE.DEFAULT)
clk_period_cont_3_style = ContStyle()
clk_period_cont_3.add_style(
    clk_period_cont_3_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_cont_4 = lv.obj(clk_period_cont)
clk_period_cont_4.set_pos(17, 187)
clk_period_cont_4.set_size(205, 50)
clk_period_img_4 = lv.img(clk_period_cont_4)
clk_period_img_4.set_pos(158, 11)
clk_period_img_4.set_size(30, 30)
clk_period_img_4.add_flag(lv.obj.FLAG.CLICKABLE)

clk_period_img_4_img = "U:/static/mp-861665386.png"

clk_period_img_4.set_src(clk_period_img_4_img)
clk_period_img_4.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_label_4 = lv.label(clk_period_cont_4)
clk_period_label_4.set_pos(18, 18)
clk_period_label_4.set_size(75, 18)
clk_period_label_4.set_text("星期四")
clk_period_label_4.set_long_mode(lv.label.LONG.WRAP)
clk_period_label_4.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
clk_period_label_4.add_style(style_font_regular_18_space_2_white,
                             lv.PART.MAIN | lv.STATE.DEFAULT)
clk_period_cont_4_style = ContStyle()
clk_period_cont_4.add_style(
    clk_period_cont_4_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_cont_5 = lv.obj(clk_period_cont)
clk_period_cont_5.set_pos(17, 245)
clk_period_cont_5.set_size(205, 50)
clk_period_img_5 = lv.img(clk_period_cont_5)
clk_period_img_5.set_pos(159, 9)
clk_period_img_5.set_size(30, 30)
clk_period_img_5.add_flag(lv.obj.FLAG.CLICKABLE)

clk_period_img_5_img = "U:/static/mp-861665386.png"

clk_period_img_5.set_src(clk_period_img_5_img)
clk_period_img_5.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_label_5 = lv.label(clk_period_cont_5)
clk_period_label_5.set_pos(18, 16)
clk_period_label_5.set_size(72, 18)
clk_period_label_5.set_text("星期五")
clk_period_label_5.set_long_mode(lv.label.LONG.WRAP)
clk_period_label_5.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
clk_period_label_5.add_style(style_font_regular_18_space_2_white,
                             lv.PART.MAIN | lv.STATE.DEFAULT)
clk_period_cont_5_style = ContStyle()
clk_period_cont_5.add_style(
    clk_period_cont_5_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_cont_6 = lv.obj(clk_period_cont)
clk_period_cont_6.set_pos(17, 303)
clk_period_cont_6.set_size(205, 50)
clk_period_img_6 = lv.img(clk_period_cont_6)
clk_period_img_6.set_pos(158, 11)
clk_period_img_6.set_size(30, 30)
clk_period_img_6.add_flag(lv.obj.FLAG.CLICKABLE)

clk_period_img_6_img = "U:/static/mp-861665386.png"

clk_period_img_6.set_src(clk_period_img_6_img)
clk_period_img_6.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_label_6 = lv.label(clk_period_cont_6)
clk_period_label_6.set_pos(18, 18)
clk_period_label_6.set_size(75, 18)
clk_period_label_6.set_text("星期六")
clk_period_label_6.set_long_mode(lv.label.LONG.WRAP)
clk_period_label_6.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
clk_period_label_6.add_style(style_font_regular_18_space_2_white,
                             lv.PART.MAIN | lv.STATE.DEFAULT)
clk_period_cont_6_style = ContStyle()
clk_period_cont_6.add_style(
    clk_period_cont_6_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_cont_7 = lv.obj(clk_period_cont)
clk_period_cont_7.set_pos(17, 361)
clk_period_cont_7.set_size(205, 50)
clk_period_img_7 = lv.img(clk_period_cont_7)
clk_period_img_7.set_pos(159, 9)
clk_period_img_7.set_size(30, 30)
clk_period_img_7.add_flag(lv.obj.FLAG.CLICKABLE)

clk_period_img_7_img = "U:/static/mp-861665386.png"

clk_period_img_7.set_src(clk_period_img_7_img)
clk_period_img_7.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_period_label_7 = lv.label(clk_period_cont_7)
clk_period_label_7.set_pos(18, 16)
clk_period_label_7.set_size(72, 18)
clk_period_label_7.set_text("星期日")
clk_period_label_7.set_long_mode(lv.label.LONG.WRAP)
clk_period_label_7.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
clk_period_label_7.add_style(style_font_regular_18_space_2_white,
                             lv.PART.MAIN | lv.STATE.DEFAULT)
clk_period_cont_7_style = ContStyle()
clk_period_cont_7.add_style(
    clk_period_cont_7_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

# clk_period_cont_8 = lv.obj(clk_period_cont)
# clk_period_cont_8.set_pos(17, 419)
# clk_period_cont_8.set_size(205, 50)
# clk_period_img_8 = lv.img(clk_period_cont_8)
# clk_period_img_8.set_pos(158, 11)
# clk_period_img_8.set_size(30, 30)
# clk_period_img_8.add_flag(lv.obj.FLAG.CLICKABLE)
#
# clk_period_img_8_img = "U:/static/mp-861665386.png"
#
# clk_period_img_8.set_src(clk_period_img_8_img)
# clk_period_img_8.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
#
# clk_period_label_8 = lv.label(clk_period_cont_8)
# clk_period_label_8.set_pos(18, 18)
# clk_period_label_8.set_size(75, 18)
# clk_period_label_8.set_text("星期日")
# clk_period_label_8.set_long_mode(lv.label.LONG.WRAP)
# clk_period_label_8.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
# clk_period_label_8.add_style(style_font_regular_18_space_2_white,
#                              lv.PART.MAIN | lv.STATE.DEFAULT)
# clk_period_cont_8_style = ContStyle()
# clk_period_cont_8.add_style(
#     clk_period_cont_8_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
#     lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------clk_ringtone screen----------------------------------------------------
clk_ringtone = lv.obj()

clk_ringtone2 = lv.obj(clk_ringtone)
# clk_ringtone2 = lv.obj()
clk_ringtone2.center()
clk_ringtone2.set_size(240, 240)
# clk_ringtone2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
clk_ringtone2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_ringtone2_1 = lv.img(clk_ringtone2)
clk_ringtone2_1.set_pos(0, 0)
clk_ringtone2_1.set_size(240, 240)
clk_ringtone2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
clk_ringtone2_1_img = "U:/static/normal.png"
clk_ringtone2_1.set_src(clk_ringtone2_1_img)
clk_ringtone2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_ringtone_title = lv.label(clk_ringtone2)
clk_ringtone_title.set_pos(69, 18)
clk_ringtone_title.set_size(96, 21)
clk_ringtone_title.set_text("闹钟铃声")
clk_ringtone_title.set_long_mode(lv.label.LONG.WRAP)
clk_ringtone_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
clk_ringtone_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_ringtone_cont = lv.obj(clk_ringtone2)
clk_ringtone_cont.set_pos(0, 50)
clk_ringtone_cont.set_size(240, 199)
clk_ringtone_cont_style = ContStyle()
clk_ringtone_cont.add_style(
    clk_period_cont_style.style_cont(0, lv.color_make(0x2f, 0x2d, 0x2d), lv.color_make(0x2f, 0x2d, 0x2d), 255),
    lv.PART.MAIN | lv.STATE.DEFAULT)

clk_ringtone_cont_1 = lv.obj(clk_ringtone_cont)
clk_ringtone_cont_1.set_pos(17, 13)
clk_ringtone_cont_1.set_size(205, 50)
clk_ringtone_img_1 = lv.img(clk_ringtone_cont_1)
clk_ringtone_img_1.set_pos(158, 8)
clk_ringtone_img_1.set_size(30, 30)
clk_ringtone_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

clk_ringtone_img_1_img = "U:/static/mp-1364748740.png"

clk_ringtone_img_1.set_src(clk_ringtone_img_1_img)

clk_ringtone_img_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_ringtone_label_1 = lv.label(clk_ringtone_cont_1)
clk_ringtone_label_1.set_pos(18, 15)
clk_ringtone_label_1.set_size(79, 18)
clk_ringtone_label_1.set_text("震动")
clk_ringtone_label_1.set_long_mode(lv.label.LONG.WRAP)
clk_ringtone_label_1.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
clk_ringtone_label_1.add_style(style_font_regular_18_space_2_white,
                               lv.PART.MAIN | lv.STATE.DEFAULT)
clk_ringtone_cont_1_style = ContStyle()
clk_ringtone_cont_1.add_style(
    clk_ringtone_cont_1_style.style_cont(10, lv.color_make(0xff, 0xff, 0xff), lv.color_make(0xa8, 0xba, 0xf0), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

clk_ringtone_cont_2 = lv.obj(clk_ringtone_cont)
clk_ringtone_cont_2.set_pos(17, 71)
clk_ringtone_cont_2.set_size(205, 50)
clk_ringtone_img_2 = lv.img(clk_ringtone_cont_2)
clk_ringtone_img_2.set_pos(158, 11)
clk_ringtone_img_2.set_size(30, 30)
clk_ringtone_img_2.add_flag(lv.obj.FLAG.CLICKABLE)

clk_ringtone_img_2_img = "U:/static/mp-861665386.png"

clk_ringtone_img_2.set_src(clk_ringtone_img_2_img)
clk_ringtone_img_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_ringtone_label_2 = lv.label(clk_ringtone_cont_2)
clk_ringtone_label_2.set_pos(18, 18)
clk_ringtone_label_2.set_size(75, 18)
clk_ringtone_label_2.set_text("响铃")
clk_ringtone_label_2.set_long_mode(lv.label.LONG.WRAP)
clk_ringtone_label_2.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
clk_ringtone_label_2.add_style(style_font_regular_18_space_2_white,
                               lv.PART.MAIN | lv.STATE.DEFAULT)
clk_ringtone_cont_2_style = ContStyle()
clk_ringtone_cont_2.add_style(
    clk_ringtone_cont_2_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

clk_ringtone_cont_3 = lv.obj(clk_ringtone_cont)
clk_ringtone_cont_3.set_pos(17, 129)
clk_ringtone_cont_3.set_size(205, 50)
clk_ringtone_img_3 = lv.img(clk_ringtone_cont_3)
clk_ringtone_img_3.set_pos(159, 9)
clk_ringtone_img_3.set_size(30, 30)
clk_ringtone_img_3.add_flag(lv.obj.FLAG.CLICKABLE)

clk_ringtone_img_3_img = "U:/static/mp-861665386.png"

clk_ringtone_img_3.set_src(clk_ringtone_img_3_img)
clk_ringtone_img_3.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

clk_ringtone_label_3 = lv.label(clk_ringtone_cont_3)
clk_ringtone_label_3.set_pos(18, 16)
clk_ringtone_label_3.set_size(72, 18)
clk_ringtone_label_3.set_text("震动加响铃")
clk_ringtone_label_3.set_long_mode(lv.label.LONG.WRAP)
clk_ringtone_label_3.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
clk_ringtone_label_3.add_style(style_font_regular_18_space_2_white,
                               lv.PART.MAIN | lv.STATE.DEFAULT)
clk_ringtone_cont_3_style = ContStyle()
clk_ringtone_cont_3.add_style(
    clk_ringtone_cont_3_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------mode screen----------------------------------------------------
mode = lv.obj()
mode2 = lv.obj(mode)
# mode2 = lv.obj()
mode2.center()
mode2.set_size(240, 240)
# mode2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
mode2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

mode2_1 = lv.img(mode2)
mode2_1.set_pos(0, 0)
mode2_1.set_size(240, 240)
mode2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
mode2_1_img = "U:/static/normal.png"

mode2_1.set_src(mode2_1_img)
mode2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

mode_title = lv.label(mode2)
mode_title.set_pos(69, 18)
mode_title.set_size(96, 21)
mode_title.set_text("情景模式")
mode_title.set_long_mode(lv.label.LONG.WRAP)
mode_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
mode_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

mode_cont_1 = lv.obj(mode2)
mode_cont_1.set_pos(17, 49)
mode_cont_1.set_size(205, 40)
mode_img_1_2 = lv.img(mode_cont_1)
mode_img_1_2.set_pos(161, 4)
mode_img_1_2.set_size(30, 30)
mode_img_1_2.add_flag(lv.obj.FLAG.CLICKABLE)

mode_img_1_2_img = "U:/static/mp-861665386.png"

mode_img_1_2.set_src(mode_img_1_2_img)
mode_img_1_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

mode_label_4 = lv.label(mode_cont_1)
mode_label_4.set_pos(13, 11)
mode_label_4.set_size(120, 18)
mode_label_4.set_text("铃声")
mode_label_4.set_long_mode(lv.label.LONG.WRAP)
mode_label_4.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
mode_label_4.add_style(style_font_regular_18_space_2_white,
                       lv.PART.MAIN | lv.STATE.DEFAULT)
mode_cont_1_style = ContStyle()
mode_cont_1.add_style(
    mode_cont_1_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

mode_cont_2 = lv.obj(mode2)
mode_cont_2.set_pos(17, 97)
mode_cont_2.set_size(205, 40)
mode_img_2_2 = lv.img(mode_cont_2)
mode_img_2_2.set_pos(161, 4)
mode_img_2_2.set_size(30, 30)
mode_img_2_2.add_flag(lv.obj.FLAG.CLICKABLE)

mode_img_2_2_img = "U:/static/mp-1364748740.png"

mode_img_2_2.set_src(mode_img_2_2_img)
mode_img_2_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

mode_label_2_5 = lv.label(mode_cont_2)
mode_label_2_5.set_pos(13, 11)
mode_label_2_5.set_size(120, 18)
mode_label_2_5.set_text("铃声加震动")
mode_label_2_5.set_long_mode(lv.label.LONG.WRAP)
mode_label_2_5.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
mode_label_2_5.add_style(style_font_regular_18_space_2_white,
                         lv.PART.MAIN | lv.STATE.DEFAULT)
mode_cont_2_style = ContStyle()
mode_cont_2.add_style(
    mode_cont_2_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

mode_cont_3 = lv.obj(mode2)
mode_cont_3.set_pos(17, 145)
mode_cont_3.set_size(205, 40)
mode_img_3_2 = lv.img(mode_cont_3)
mode_img_3_2.set_pos(161, 4)
mode_img_3_2.set_size(30, 30)
mode_img_3_2.add_flag(lv.obj.FLAG.CLICKABLE)

mode_img_3_2_img = "U:/static/mp-861665386.png"

mode_img_3_2.set_src(mode_img_3_2_img)
mode_img_3_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

mode_label_2_5 = lv.label(mode_cont_3)
mode_label_2_5.set_pos(13, 11)
mode_label_2_5.set_size(120, 18)
mode_label_2_5.set_text("震动")
mode_label_2_5.set_long_mode(lv.label.LONG.WRAP)
mode_label_2_5.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
# add style for mode_label_2_5
mode_label_2_5.add_style(style_font_regular_18_space_2_white,
                         lv.PART.MAIN | lv.STATE.DEFAULT)
mode_cont_3_style = ContStyle()
mode_cont_3.add_style(
    mode_cont_3_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

mode_cont_4 = lv.obj(mode2)
mode_cont_4.set_pos(17, 193)
mode_cont_4.set_size(205, 40)
mode_img_4_2 = lv.img(mode_cont_4)
mode_img_4_2.set_pos(161, 4)
mode_img_4_2.set_size(30, 30)
mode_img_4_2.add_flag(lv.obj.FLAG.CLICKABLE)

mode_img_4_2_img = "U:/static/mp-861665386.png"

mode_img_4_2.set_src(mode_img_4_2_img)
mode_img_4_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

mode_label_2_5 = lv.label(mode_cont_4)
mode_label_2_5.set_pos(13, 11)
mode_label_2_5.set_size(120, 18)
mode_label_2_5.set_text("静音")
mode_label_2_5.set_long_mode(lv.label.LONG.WRAP)
mode_label_2_5.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)

# add style for mode_label_2_5
mode_label_2_5.add_style(style_font_regular_18_space_2_white,
                         lv.PART.MAIN | lv.STATE.DEFAULT)
mode_cont_4_style = ContStyle()
mode_cont_4.add_style(
    mode_cont_4_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------time_mode screen----------------------------------------------------
time_mode = lv.obj()

time_mode2 = lv.obj(time_mode)
# time_mode2 = lv.obj()
time_mode2.center()
time_mode2.set_size(240, 240)
# time_mode2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
time_mode2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

time_mode2_1 = lv.img(time_mode2)
time_mode2_1.set_pos(0, 0)
time_mode2_1.set_size(240, 240)
time_mode2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
time_mode2_1_img = "U:/static/normal.png"

time_mode2_1.set_src(time_mode2_1_img)
time_mode2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

time_mode_title = lv.label(time_mode2)
time_mode_title.set_pos(69, 18)
time_mode_title.set_size(96, 21)
time_mode_title.set_text("时间")
time_mode_title.set_long_mode(lv.label.LONG.WRAP)
time_mode_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)

time_mode_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

time_mode_cont_1 = lv.obj(time_mode2)
time_mode_cont_1.set_pos(17, 79)
time_mode_cont_1.set_size(205, 49)
time_mode_select1 = lv.img(time_mode_cont_1)
time_mode_select1.set_pos(161, 7)
time_mode_select1.set_size(30, 30)
time_mode_select1.add_flag(lv.obj.FLAG.CLICKABLE)

time_mode_select1_img = "U:/static/mp-861665386.png"

time_mode_select1.set_src(time_mode_select1_img)
time_mode_select1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

time_mode_label1 = lv.label(time_mode_cont_1)
time_mode_label1.set_pos(13, 15)
time_mode_label1.set_size(120, 18)
time_mode_label1.set_text("12小时制")
time_mode_label1.set_long_mode(lv.label.LONG.WRAP)
time_mode_label1.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
# add style for time_mode_label1
time_mode_label1.add_style(style_font_regular_18_space_2_white,
                           lv.PART.MAIN | lv.STATE.DEFAULT)
time_mode_cont_1_style = ContStyle()
time_mode_cont_1.add_style(
    time_mode_cont_1_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

time_mode_cont_2 = lv.obj(time_mode2)
time_mode_cont_2.set_pos(17, 141)
time_mode_cont_2.set_size(205, 49)
time_mode_select2 = lv.img(time_mode_cont_2)
time_mode_select2.set_pos(161, 7)
time_mode_select2.set_size(30, 30)
time_mode_select2.add_flag(lv.obj.FLAG.CLICKABLE)

time_mode_select2_img = "U:/static/mp-1364748740.png"

time_mode_select2.set_src(time_mode_select2_img)
time_mode_select2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

time_mode_label2 = lv.label(time_mode_cont_2)
time_mode_label2.set_pos(13, 15)
time_mode_label2.set_size(120, 18)
time_mode_label2.set_text("24小时制")
time_mode_label2.set_long_mode(lv.label.LONG.WRAP)
time_mode_label2.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
time_mode_label2.add_style(style_font_regular_18_space_2_white,
                           lv.PART.MAIN | lv.STATE.DEFAULT)
time_mode_cont_2_style = ContStyle()
time_mode_cont_2.add_style(
    time_mode_cont_2_style.style_cont(10, lv.color_make(0xea, 0xe2, 0xf3), lv.color_make(0xbc, 0xb9, 0xe4), 226),
    lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------brightness screen----------------------------------------------------
brightness = lv.obj()

brightness2 = lv.obj(brightness)
# brightness2 = lv.obj()
brightness2.center()
brightness2.set_size(240, 240)
# brightness2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
brightness2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

brightness2_1 = lv.img(brightness2)
brightness2_1.set_pos(0, 0)
brightness2_1.set_size(240, 240)
brightness2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
brightness2_1_img = "U:/static/normal.png"

brightness2_1.set_src(brightness2_1_img)
brightness2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

brightness_title = lv.label(brightness2)
brightness_title.set_pos(69, 18)
brightness_title.set_size(96, 21)
brightness_title.set_text("显示")
brightness_title.set_long_mode(lv.label.LONG.WRAP)
brightness_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
brightness_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

brightness_tips1 = lv.label(brightness2)
brightness_tips1.set_pos(17, 165)
brightness_tips1.set_size(91, 15)
brightness_tips1.set_text("温馨提示:")
brightness_tips1.set_long_mode(lv.label.LONG.WRAP)
brightness_tips1.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
brightness_tips1.add_style(style_font_regular_12_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

brightness_tips2 = lv.label(brightness2)
brightness_tips2.set_pos(16, 187)
brightness_tips2.set_size(209, 15)
brightness_tips2.set_text("为保护您的眼睛，请根据光线调节亮度")
brightness_tips2.set_long_mode(lv.label.LONG.WRAP)
brightness_tips2.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
brightness_tips2.add_style(style_font_regular_12_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

brightness_cont_1 = lv.obj(brightness2)
brightness_cont_1.set_pos(60, 90)
brightness_cont_1.set_size(120, 60)
brightness_bar_1 = lv.bar(brightness_cont_1)
brightness_bar_1.set_pos(0, 27)
brightness_bar_1.set_size(120, 6)
brightness_bar_1.set_style_anim_time(1000, lv.PART.INDICATOR | lv.STATE.DEFAULT)
brightness_bar_1.set_mode(lv.bar.MODE.NORMAL)
brightness_bar_1.set_value(50, lv.ANIM.OFF)

# add style for brightness_bar_1
brightness_bar_1.add_style(style_bar, lv.PART.MAIN | lv.STATE.DEFAULT)
brightness_bar_1.add_style(style_bar_indic, lv.PART.INDICATOR | lv.STATE.DEFAULT)

# add style for brightness_cont_1
brightness_cont_1_style = ContStyle()
brightness_cont_1.add_style(
    brightness_cont_1_style.style_cont(5, lv.color_make(0xff, 0xff, 0xff), lv.color_make(0xff, 0xff, 0xff), 255),
    lv.PART.MAIN | lv.STATE.DEFAULT)

brightness_imgbtn_1 = lv.imgbtn(brightness2)
brightness_imgbtn_1.set_pos(8, 90)
brightness_imgbtn_1.set_size(50, 60)

brightness_imgbtn_1_imgReleased = "U:/static/mp-1704371323.png"
brightness_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, brightness_imgbtn_1_imgReleased, None, None)

brightness_imgbtn_1_imgPressed = "U:/static/mp-1704371323.png"
brightness_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, brightness_imgbtn_1_imgPressed, None, None)

brightness_imgbtn_1_imgCheckedReleased = "U:/static/mp-1704371323.png"
brightness_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, brightness_imgbtn_1_imgCheckedReleased, None, None)

brightness_imgbtn_1_imgCheckedPressed = "U:/static/mp-1704371323.png"
brightness_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, brightness_imgbtn_1_imgCheckedPressed, None, None)

brightness_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
brightness_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
brightness_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
brightness_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

brightness_imgbtn_2 = lv.imgbtn(brightness2)
brightness_imgbtn_2.set_pos(182, 90)
brightness_imgbtn_2.set_size(50, 60)

brightness_imgbtn_2_imgReleased = "U:/static/mp1401232660.png"
brightness_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, brightness_imgbtn_2_imgReleased, None, None)

brightness_imgbtn_2_imgPressed = "U:/static/mp1401232660.png"
brightness_imgbtn_2.set_src(lv.imgbtn.STATE.PRESSED, brightness_imgbtn_2_imgPressed, None, None)

brightness_imgbtn_2_imgCheckedReleased = "U:/static/mp1401232660.png"
brightness_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, brightness_imgbtn_2_imgCheckedReleased, None, None)

brightness_imgbtn_2_imgCheckedPressed = "U:/static/mp1401232660.png"
brightness_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, brightness_imgbtn_2_imgCheckedPressed, None, None)

brightness_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
brightness_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
brightness_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
brightness_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

# --------------------------------------------volume screen----------------------------------------------------
volume = lv.obj()

volume2 = lv.obj(volume)
# volume2 = lv.obj()
volume2.center()
volume2.set_size(240, 240)
# volume2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
volume2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

volume2_1 = lv.img(volume2)
volume2_1.set_pos(0, 0)
volume2_1.set_size(240, 240)
volume2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
volume2_1_img = "U:/static/normal.png"

volume2_1.set_src(volume2_1_img)
volume2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

volume_title = lv.label(volume2)
volume_title.set_pos(69, 18)
volume_title.set_size(96, 21)
volume_title.set_text("音量")
volume_title.set_long_mode(lv.label.LONG.WRAP)
volume_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
volume_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

volume_cont_1 = lv.obj(volume2)
volume_cont_1.set_pos(60, 90)
volume_cont_1.set_size(120, 60)
volume_bar_1 = lv.bar(volume_cont_1)
volume_bar_1.set_pos(0, 27)
volume_bar_1.set_size(120, 6)
volume_bar_1.set_style_anim_time(1000, lv.PART.INDICATOR | lv.STATE.DEFAULT)
volume_bar_1.set_mode(lv.bar.MODE.NORMAL)
volume_bar_1.set_value(50, lv.ANIM.OFF)

volume_bar_1.add_style(style_bar, lv.PART.MAIN | lv.STATE.DEFAULT)

volume_bar_1.add_style(style_bar_indic, lv.PART.INDICATOR | lv.STATE.DEFAULT)
volume_cont_1_style = ContStyle()
volume_cont_1.add_style(
    volume_cont_1_style.style_cont(5, lv.color_make(0xff, 0xff, 0xff), lv.color_make(0xff, 0xff, 0xff), 255),
    lv.PART.MAIN | lv.STATE.DEFAULT)

volume_imgbtn_1 = lv.imgbtn(volume2)
volume_imgbtn_1.set_pos(8, 90)
volume_imgbtn_1.set_size(50, 60)

volume_imgbtn_1_imgReleased = "U:/static/mp-1704371323.png"
volume_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, volume_imgbtn_1_imgReleased, None, None)

volume_imgbtn_1_imgPressed = "U:/static/mp-1704371323.png"
volume_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, volume_imgbtn_1_imgPressed, None, None)

volume_imgbtn_1_imgCheckedReleased = "U:/static/mp-1704371323.png"
volume_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, volume_imgbtn_1_imgCheckedReleased, None, None)

volume_imgbtn_1_imgCheckedPressed = "U:/static/mp-1704371323.png"
volume_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, volume_imgbtn_1_imgCheckedPressed, None, None)

volume_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
volume_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
volume_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
volume_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

volume_imgbtn_2 = lv.imgbtn(volume2)
volume_imgbtn_2.set_pos(182, 90)
volume_imgbtn_2.set_size(50, 60)

volume_imgbtn_2_imgReleased = "U:/static/mp1401232660.png"
volume_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, volume_imgbtn_2_imgReleased, None, None)

volume_imgbtn_2_imgPressed = "U:/static/mp1401232660.png"
volume_imgbtn_2.set_src(lv.imgbtn.STATE.PRESSED, volume_imgbtn_2_imgPressed, None, None)

volume_imgbtn_2_imgCheckedReleased = "U:/static/mp1401232660.png"
volume_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, volume_imgbtn_2_imgCheckedReleased, None, None)

volume_imgbtn_2_imgCheckedPressed = "U:/static/mp1401232660.png"
volume_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, volume_imgbtn_2_imgCheckedPressed, None, None)

volume_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
volume_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
volume_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
volume_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

# --------------------------------------------del_log screen----------------------------------------------------
del_log = lv.obj()

del_log2 = lv.obj(del_log)
# del_log2 = lv.obj()
del_log2.center()
del_log2.set_size(240, 240)
# del_log2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
del_log2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

del_log2_1 = lv.img(del_log2)
del_log2_1.set_pos(0, 0)
del_log2_1.set_size(240, 240)
del_log2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
del_log2_1_img = "U:/static/normal.png"

del_log2_1.set_src(del_log2_1_img)
del_log2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

del_log_title = lv.label(del_log2)
del_log_title.set_pos(51, 18)
del_log_title.set_size(137, 21)
del_log_title.set_text("清除通话记录")
del_log_title.set_long_mode(lv.label.LONG.WRAP)
del_log_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
del_log_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

del_log_cont_1 = lv.obj(del_log2)
del_log_cont_1.set_pos(32, 95)
del_log_cont_1.set_size(180, 80)
del_log_label_1 = lv.label(del_log_cont_1)
del_log_label_1.set_pos(38, 5)
del_log_label_1.set_size(100, 14)
del_log_label_1.set_text("确定删除?")
del_log_label_1.set_long_mode(lv.label.LONG.WRAP)
del_log_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
del_log_label_1.add_style(style_font_regular_14_space_1_default, lv.PART.MAIN | lv.STATE.DEFAULT)

del_log_imgbtn_1 = lv.imgbtn(del_log_cont_1)
del_log_imgbtn_1.set_pos(26, 38)
del_log_imgbtn_1.set_size(43, 33)

del_log_imgbtn_1_imgReleased = "U:/static/mp-1586757447.png"
del_log_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, del_log_imgbtn_1_imgReleased, None, None)

del_log_imgbtn_1_imgPressed = "U:/static/mp-1586757447.png"
del_log_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, del_log_imgbtn_1_imgPressed, None, None)

del_log_imgbtn_1_imgCheckedReleased = "U:/static/mp-1586757447.png"
del_log_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, del_log_imgbtn_1_imgCheckedReleased, None, None)

del_log_imgbtn_1_imgCheckedPressed = "U:/static/mp-1586757447.png"
del_log_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, del_log_imgbtn_1_imgCheckedPressed, None, None)

del_log_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
del_log_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
del_log_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
del_log_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

del_log_imgbtn_2 = lv.imgbtn(del_log_cont_1)
del_log_imgbtn_2.set_pos(110, 39)
del_log_imgbtn_2.set_size(38, 33)

del_log_imgbtn_2_imgReleased = "U:/static/mp686806719.png"
del_log_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, del_log_imgbtn_2_imgReleased, None, None)

del_log_imgbtn_2_imgPressed = "U:/static/mp686806719png"
del_log_imgbtn_2.set_src(lv.imgbtn.STATE.PRESSED, del_log_imgbtn_2_imgPressed, None, None)

del_log_imgbtn_2_imgCheckedReleased = "U:/static/mp686806719.png"
del_log_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, del_log_imgbtn_2_imgCheckedReleased, None, None)

del_log_imgbtn_2_imgCheckedPressed = "U:/static/mp686806719.png"
del_log_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, del_log_imgbtn_2_imgCheckedPressed, None, None)

del_log_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
del_log_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
del_log_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
del_log_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)
del_log_cont_1_style = ContStyle()
del_log_cont_1.add_style(
    del_log_cont_1_style.style_cont(6, lv.color_make(0xff, 0xff, 0xff), lv.color_make(0xff, 0xff, 0xff), 44),
    lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------about screen----------------------------------------------------
about = lv.obj()

about2 = lv.obj(about)
# about2 = lv.obj()
about2.center()
about2.set_size(240, 240)
# about2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
about2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

about2_1 = lv.img(about2)
about2_1.set_pos(0, 0)
about2_1.set_size(240, 240)
about2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
about2_1_img = "U:/static/normal.png"

about2_1.set_src(about2_1_img)
about2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

about_label_1 = lv.label(about2)
about_label_1.set_pos(50, 18)
about_label_1.set_size(137, 21)
about_label_1.set_text("关于本机")
about_label_1.set_long_mode(lv.label.LONG.WRAP)
about_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
about_label_1.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

about_scr_cont_1 = lv.obj(about2)
about_scr_cont_1.set_pos(0, 50)
about_scr_cont_1.set_size(240, 185)
about_cont_style = ContStyle()
about_scr_cont_1.add_style(
    about_cont_style.style_cont(0, lv.color_make(0x2f, 0x2d, 0x2d), lv.color_make(0x2f, 0x2d, 0x2d), 255),
    lv.PART.MAIN | lv.STATE.DEFAULT)

about_label_1 = lv.label(about_scr_cont_1)
about_label_1.set_text("")
about_label_1.set_long_mode(lv.label.LONG.WRAP)
about_label_1.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
about_label_1.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------verion update screen----------------------------------------------------
version_update = lv.obj()

version_update2 = lv.obj(version_update)
# version_update2 = lv.obj()
version_update2.center()
version_update2.set_size(240, 240)
# version_update2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
version_update2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

version_update2_1 = lv.img(version_update2)
version_update2_1.set_pos(0, 0)
version_update2_1.set_size(240, 240)
version_update2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
version_update2_1_img = "U:/static/normal.png"

version_update2_1.set_src(version_update2_1_img)
version_update2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

version_update_label_1 = lv.label(version_update2)
version_update_label_1.set_pos(50, 18)
version_update_label_1.set_size(137, 21)
version_update_label_1.set_text("版本更新")
version_update_label_1.set_long_mode(lv.label.LONG.WRAP)
version_update_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
version_update_label_1.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

version_update_scr_cont_1 = lv.obj(version_update2)
version_update_scr_cont_1.set_pos(0, 50)
version_update_scr_cont_1.set_size(240, 185)
version_update_cont_style = ContStyle()
version_update_scr_cont_1.add_style(
    version_update_cont_style.style_cont(0, lv.color_make(0x2f, 0x2d, 0x2d), lv.color_make(0x2f, 0x2d, 0x2d), 255),
    lv.PART.MAIN | lv.STATE.DEFAULT)

version_update_label_1 = lv.label(version_update_scr_cont_1)
version_update_label_1.set_text("")
version_update_label_1.set_long_mode(lv.label.LONG.WRAP)
version_update_label_1.set_style_text_align(lv.TEXT_ALIGN.LEFT, 0)
version_update_label_1.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------bg_select screen----------------------------------------------------
bg_select = lv.obj()
bg_select2 = lv.obj(bg_select)
# bg_select2 = lv.obj()
bg_select2.center()
bg_select2.set_size(240, 240)
bg_select2_style = ContStyle()
bg_select2.add_style(
    bg_select2_style.style_cont(0, lv.color_make(0x21, 0x95, 0xf6), lv.color_make(0x21, 0x95, 0xf6), 0),
    lv.PART.MAIN | lv.STATE.DEFAULT)

bg_select_img_1 = lv.img(bg_select2)
bg_select_img_1.set_pos(0, 0)
bg_select_img_1.set_size(240, 240)
bg_select_img_1.add_flag(lv.obj.FLAG.CLICKABLE)

bg_select_img_1.set_src("U:/static/mp1467131564.png")
# bg_select_img_1.set_src("U:/static/mp505517547.jpg")
bg_select_img_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

bg_select_imgbtn_1 = lv.img(bg_select2)
bg_select_imgbtn_1.set_pos(95, 173)
bg_select_imgbtn_1.set_size(50, 50)

bg_select_imgbtn_1_imgReleased = "U:/static/mp-1007005535.png"
bg_select_imgbtn_1.set_src(bg_select_imgbtn_1_imgReleased)
bg_select_imgbtn_1.add_flag(lv.obj.FLAG.CLICKABLE)
bg_select_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

bg_select_imgbtn_2 = lv.imgbtn(bg_select2)
bg_select_imgbtn_2.set_pos(195, 100)
bg_select_imgbtn_2.set_size(30, 30)

bg_select_imgbtn_2_imgReleased = "U:/static/mp-171556854.png"
bg_select_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, bg_select_imgbtn_2_imgReleased, None, None)

bg_select_imgbtn_2_imgPressed = "U:/static/mp-171556854.png"
bg_select_imgbtn_2.set_src(lv.imgbtn.STATE.PRESSED, bg_select_imgbtn_2_imgPressed, None, None)

bg_select_imgbtn_2_imgCheckedReleased = "U:/static/mp-171556854.png"
bg_select_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, bg_select_imgbtn_2_imgCheckedReleased, None, None)

bg_select_imgbtn_2_imgCheckedPressed = "U:/static/mp-171556854.png"
bg_select_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, bg_select_imgbtn_2_imgCheckedPressed, None, None)

bg_select_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
bg_select_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
bg_select_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
bg_select_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

bg_select_imgbtn_3 = lv.imgbtn(bg_select2)
bg_select_imgbtn_3.set_pos(15, 100)
bg_select_imgbtn_3.set_size(30, 30)

bg_select_imgbtn_3_imgReleased = "U:/static/mp-593202684.png"
bg_select_imgbtn_3.set_src(lv.imgbtn.STATE.RELEASED, bg_select_imgbtn_3_imgReleased, None, None)

bg_select_imgbtn_3_imgPressed = "U:/static/mp-593202684.png"
bg_select_imgbtn_3.set_src(lv.imgbtn.STATE.PRESSED, bg_select_imgbtn_3_imgPressed, None, None)

bg_select_imgbtn_3_imgCheckedReleased = "U:/static/mp-593202684.png"
bg_select_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, bg_select_imgbtn_3_imgCheckedReleased, None, None)

bg_select_imgbtn_3_imgCheckedPressed = "U:/static/mp-593202684.png"
bg_select_imgbtn_3.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, bg_select_imgbtn_3_imgCheckedPressed, None, None)

bg_select_imgbtn_3.add_flag(lv.obj.FLAG.CHECKABLE)
bg_select_imgbtn_3.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
bg_select_imgbtn_3.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
bg_select_imgbtn_3.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

# --------------------------------------------bg_select screen----------------------------------------------------
power_down = lv.obj()

power_down2 = lv.obj(power_down)
# power_down2 = lv.obj()
power_down2.center()
power_down2.set_size(240, 240)
# power_down2.add_style(style_cont(0,lv.color_make(0x21, 0x95, 0xf6),lv.color_make(0x21, 0x95, 0xf6), 0), lv.PART.MAIN | lv.STATE.DEFAULT)
power_down2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

power_down2_1 = lv.img(power_down2)
power_down2_1.set_pos(0, 0)
power_down2_1.set_size(240, 240)
power_down2_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
power_down2_1_img = "U:/static/normal.png"

power_down2_1.set_src(power_down2_1_img)
power_down2_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

power_down_title = lv.label(power_down2)
power_down_title.set_pos(51, 18)
power_down_title.set_size(137, 21)
power_down_title.set_text("关机")
power_down_title.set_long_mode(lv.label.LONG.WRAP)
power_down_title.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
power_down_title.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

power_down_cont_1 = lv.obj(power_down2)
power_down_cont_1.set_pos(32, 95)
power_down_cont_1.set_size(180, 90)

power_down_imgbtn_1 = lv.imgbtn(power_down_cont_1)
power_down_imgbtn_1.set_pos(26, 10)
power_down_imgbtn_1.set_size(70, 70)

power_down_imgbtn_1_imgReleased = "U:/static/mp1428729994.png"
power_down_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, power_down_imgbtn_1_imgReleased, None, None)

power_down_imgbtn_1_imgPressed = "U:/static/mp1428729994.png"
power_down_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, power_down_imgbtn_1_imgPressed, None, None)

power_down_imgbtn_1_imgCheckedReleased = "U:/static/mp1428729994.png"
power_down_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, power_down_imgbtn_1_imgCheckedReleased, None, None)

power_down_imgbtn_1_imgCheckedPressed = "U:/static/mp1428729994.png"
power_down_imgbtn_1.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, power_down_imgbtn_1_imgCheckedPressed, None, None)

power_down_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
power_down_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
power_down_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
power_down_imgbtn_1.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)

power_down_imgbtn_2 = lv.imgbtn(power_down_cont_1)
power_down_imgbtn_2.set_pos(110, 30)
power_down_imgbtn_2.set_size(38, 33)

power_down_imgbtn_2_imgReleased = "U:/static/mp686806719.png"
power_down_imgbtn_2.set_src(lv.imgbtn.STATE.RELEASED, power_down_imgbtn_2_imgReleased, None, None)

power_down_imgbtn_2_imgPressed = "U:/static/mp686806719.png"
power_down_imgbtn_2.set_src(lv.imgbtn.STATE.PRESSED, power_down_imgbtn_2_imgPressed, None, None)

power_down_imgbtn_2_imgCheckedReleased = "U:/static/mp686806719.png"
power_down_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, power_down_imgbtn_2_imgCheckedReleased, None, None)

power_down_imgbtn_2_imgCheckedPressed = "U:/static/mp686806719.png"
power_down_imgbtn_2.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, power_down_imgbtn_2_imgCheckedPressed, None, None)

power_down_imgbtn_2.add_flag(lv.obj.FLAG.CHECKABLE)
power_down_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)
power_down_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.PRESSED)
power_down_imgbtn_2.add_style(style_img, lv.PART.MAIN | lv.STATE.CHECKED)
power_down_cont_1_style = ContStyle()
power_down_cont_1.add_style(
    power_down_cont_1_style.style_cont(6, lv.color_make(0xff, 0xff, 0xff), lv.color_make(0xff, 0xff, 0xff), 44),
    lv.PART.MAIN | lv.STATE.DEFAULT)

# --------------------------------------------bg_select screen----------------------------------------------------

learn_info = lv.obj()
learn_info2 = lv.obj(learn_info)
# power_down2 = lv.obj()
learn_info2.center()
learn_info2.set_size(240, 240)
learn_info2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)

learn_info_1 = lv.img(learn_info2)
learn_info_1.set_pos(0, 0)
learn_info_1.set_size(240, 240)
learn_info_1.add_flag(lv.obj.FLAG.CLICKABLE)

# 背景图片
learn_info_1_img = "U:/static/normal.png"

learn_info_1.set_src(learn_info_1_img)
learn_info_1.add_style(style_img, lv.PART.MAIN | lv.STATE.DEFAULT)

learn_info_img = lv.img(learn_info2)
learn_info_img.set_pos(65, 20)
learn_info_img.set_size(110, 110)
learn_info_img.set_src('U:/static/headshort.png')

learn_info_lb1 = lv.label(learn_info2)
learn_info_lb1.set_pos(0, 140)
learn_info_lb1.set_size(240, 21)
learn_info_lb1.set_long_mode(lv.label.LONG.WRAP)
learn_info_lb1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
learn_info_lb1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
learn_info_lb1.set_text("合肥一中")
learn_info_lb1.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

learn_info_lb2 = lv.label(learn_info2)
learn_info_lb2.set_pos(0, 165)
learn_info_lb2.set_size(240, 21)
learn_info_lb2.set_long_mode(lv.label.LONG.WRAP)
learn_info_lb2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
learn_info_lb2.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
learn_info_lb2.set_text("姓名: ")
learn_info_lb2.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)

learn_info_lb3 = lv.label(learn_info2)
learn_info_lb3.set_pos(0, 190)
learn_info_lb3.set_size(240, 21)
learn_info_lb3.set_long_mode(lv.label.LONG.WRAP)
learn_info_lb3.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
learn_info_lb3.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
learn_info_lb3.set_text("九年级  10班")
learn_info_lb3.add_style(style_font_regular_18_space_2_default, lv.PART.MAIN | lv.STATE.DEFAULT)
# --------------------------------------------------------------------------------------------------------------
normal = lv.obj()
normal2 = lv.obj(normal)
# power_down2 = lv.obj()
normal2.center()
normal2.set_size(240, 240)
normal2.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)
normal_img = lv.img(normal2)
normal_img.set_size(240, 240)
normal_img.add_style(style_screen, lv.PART.MAIN | lv.STATE.DEFAULT)
normal_img.set_src("U:/static/normal.png")

from usr.common import Abstract


class Screen(Abstract):
    def __init__(self):
        self.meta = None
        self.meta_info = None
        self.last_screen_info = None
        self.bg_img = None

    @staticmethod
    def publish_ope():
        # 主动向后端请求运营商资源
        return EventMesh.publish("screen_get_ope")

    @staticmethod
    def publish_sig():
        # 主动向后端请求信号强度
        return EventMesh.publish("screen_get_sig")

    @staticmethod
    def publish_time():
        # 主动向后端请求时间
        return EventMesh.publish("screen_get_time")

    @staticmethod
    def publish_date():
        # 主动向后端请求时间
        return EventMesh.publish("main_get_date")

    @staticmethod
    def publish_battery():
        # 主动向后端请求电池电量
        return EventMesh.publish("screen_get_battery")

    def deactivate(self):
        pass

    def set_bg_img(self, _fp):
        print("bg _fp = {} NAME = {} bg_img = {}".format(_fp, self.NAME, self.bg_img))
        if self.bg_img:
            self.bg_img.set_src(_fp)

    def load_screen(self, e, msg):
        EventMesh.publish("load_screen", msg)

    def load(self):
        pass

    def get_meta(self):
        return self.meta

    def done_left_to_right(self):
        pass

    def done_right_to_left(self):
        pass

    def done_bottom_to_top(self):
        pass

    def done_top_to_bottom(self):
        pass

    def done_return(self):
        pass

    def done_click(self):
        pass

    def done_error(self):
        pass

    def btn1_press(self):
        pass

    def btn2_press(self):
        pass

    def btn3_press(self):
        pass

    def btn4_press(self):
        pass

    def btn5_press(self):
        pass

    def btn6_press(self):
        pass

    def btn7_press(self):
        pass

    def btn8_press(self):
        pass

    def btn1_release(self):
        pass

    def btn2_release(self):
        pass

    def btn3_release(self):
        pass

    def btn4_release(self):
        pass

    def btn5_release(self):
        pass

    def btn6_release(self):
        pass

    def btn7_release(self):
        pass

    def btn8_release(self):
        pass


class MainScreen(Screen):
    NAME = "main"

    def __init__(self):
        super().__init__()
        self.meta = main
        self.bg_img = main_img_1
        self.main_img_1 = main_img_1
        self.main_time_1 = main_time_1
        self.main_time_2 = main_time_2
        self.main_date_1 = main_date_1
        # 定位标识
        self.main_img_4 = main_img_4
        # 闹钟标识
        self.main_img_3 = main_img_3
        # 电量等级
        self.main_img_2 = main_img_2
        # 充电标识
        self.main_img_11 = main_img_11
        # 4G标识
        self.main_img_7 = main_img_7
        # 运营商标识
        self.main_img_6_img = main_img_6_img
        # 温度
        self.main_temperature_value = main_temperature_value
        # 步数
        self.main_step_value = main_step_value

        self.main_img_11_img = main_img_11_img

    def done_right_to_left(self):
        EventMesh.publish("load_screen", {"screen": "menu"})

    def done_top_to_bottom(self):
        EventMesh.publish("load_screen", {"screen": "drop_down_menu"})

    def done_left_to_right(self):
        EventMesh.publish("load_screen", {"screen": "learn_info"})

    def post_processor_after_initialization(self):
        EventMesh.subscribe("signal", self.__signal_cb)
        EventMesh.subscribe("time", self.__time_cb)
        EventMesh.subscribe("battery", self.__battery_cb)
        EventMesh.subscribe("net_show", self.__net_cb)
        EventMesh.subscribe("topic_push_clock_exist", self.__get_clock_exist)
        EventMesh.subscribe("topic_push_gps_exist", self.__get_gps_exist)
        EventMesh.subscribe("topic_push_temperature_record", self.__temperature_record)
        EventMesh.subscribe("topic_push_step_count", self.__step_count)

    def __get_clock_exist(self, event=None, msg=None):
        if msg == 1:
            _main_img_4_img = "U:/static/mp-1553323012.png"
            self.main_img_4.set_src(_main_img_4_img)
        else:
            _main_img_4_img = "U:/static/mp-1553323012no.png"
            self.main_img_4.set_src(_main_img_4_img)

    def __get_gps_exist(self, event=None, msg=None):
        if msg == 1:
            _main_img_3_img = "U:/static/mp-895447498.png"
            self.main_img_3.set_src(_main_img_3_img)
        else:
            _main_img_3_img = "U:/static/mp-895447498no.png"
            self.main_img_3.set_src(_main_img_3_img)

    def __temperature_record(self, event, msg):
        self.main_temperature_value.set_text(msg)

    def __step_count(self, event, msg):
        self.main_step_value.set_text(msg)

    def __net_cb(self, event, msg):
        self.main_top_net.set_text(msg)

    def __gps_cb(self, event, msg):
        if not msg:
            self.main_top_gps.set_src('gps.png')
        else:
            self.main_top_gps.set_src('B:/static/gps.png')

    def initialization(self):
        signal = self.publish_sig()
        if signal:
            self.__signal_cb(None, signal)
        # 获取电池电量
        battery = self.publish_battery()
        if battery:
            self.__battery_cb(None, battery)
        # 获取运营商
        ope = self.publish_ope()
        if ope:
            self.__ope_show(None, ope)
        # 获取时间
        time = self.publish_time()
        if time:
            self.__time_cb(None, time)

        temperature_record = EventMesh.publish("topic_get_temperature_record")
        if temperature_record:
            self.__temperature_record(None, temperature_record)

        step_count = EventMesh.publish("topic_get_step_count")
        if step_count:
            self.__step_count(None, step_count)

        _clock_exist = EventMesh.publish("get_clock_exist")
        self.__get_clock_exist(msg=_clock_exist)

        _gps_exist = EventMesh.publish("get_gps_exist")
        self.__get_gps_exist(msg=_gps_exist)

    def __signal_cb(self, event, msg):
        # TODO 需要支持信号操作
        pass

    def __ope_show(self, event, msg):
        # 目前只支持中国移动
        pass

    def __battery_cb(self, event, msg):
        if msg[0] == '1':
            self.main_img_11.set_src("U:/static/charge_in.png")
        else:
            self.main_img_11.set_src("U:/static/charge_out.png")

        self.main_img_2.set_src(msg[1])

    def __time_cb(self, event, msg):
        self.main_time_1.set_text(msg[0])
        self.main_time_2.set_text(msg[1])
        self.main_date_1.set_text(msg[2])

    def done_bottom_to_top(self):
        EventMesh.publish("load_screen", {"screen": "health_qrcode"})


class NormalScreen(Screen):
    """通用开机显示界面"""
    NAME = "normal"

    def __init__(self):
        super().__init__()
        self.meta = normal
        self.bg_img = normal_img

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "main"})


class LearnInfoScreen(Screen):
    """学信息界面"""
    NAME = "learn_info"

    def __init__(self):
        super().__init__()
        self.bg_img = learn_info_1
        self.meta = learn_info
        self.learn_info_lb1 = learn_info_lb1
        self.learn_info_lb2 = learn_info_lb2
        self.learn_info_lb3 = learn_info_lb3
        self.learn_info_img = learn_info_img
        self.timer = osTimer()

    def initialization(self):
        student_info = EventMesh.publish("get_student_info")
        self.learn_info_lb1.set_text(student_info[0])
        self.learn_info_lb2.set_text("姓名: " + student_info[1])
        self.learn_info_lb3.set_text(student_info[2] + "  " + student_info[3])
        self.learn_info_img.set_src(student_info[4])

    def timer_stop(self):
        self.timer.stop()

    def timer_reset(self):
        self.timer_stop()
        self.timer_start()

    def timer_start(self):
        self.timer.start(10 * 1000, 0, self.publish_auto_sleep)

    def publish_auto_sleep(self, args):
        EventMesh.publish("start_lcd_sleep_auto_sleep", 1)

    def post_processor_after_initialization(self):
        self.timer_start()

    def done_return(self):
        self.timer_stop()
        EventMesh.publish("load_screen", self.last_screen_info)
        EventMesh.publish("start_lcd_sleep_auto_sleep")

    def done_left_to_right(self):
        self.timer_reset()

    def done_right_to_left(self):
        self.timer_reset()

    def done_bottom_to_top(self):
        self.timer_reset()

    def done_top_to_bottom(self):
        self.timer_reset()

    def done_click(self):
        self.timer_reset()

    def done_error(self):
        self.timer_reset()

    def btn1_press(self):
        self.timer_reset()

    def btn2_press(self):
        self.timer_reset()

    def btn3_press(self):
        self.timer_reset()

    def btn4_press(self):
        self.timer_reset()

    def btn5_press(self):
        self.timer_reset()

    def btn6_press(self):
        self.timer_reset()

    def btn7_press(self):
        self.timer_reset()

    def btn8_press(self):
        self.timer_stop()
        EventMesh.publish("start_lcd_sleep_auto_sleep")
        EventMesh.publish("load_screen", self.last_screen_info)


class IdleScreen(Screen):
    """待机页面"""
    NAME = "idle"

    def __init__(self):
        super().__init__()
        self.meta = idle
        self.bg_img = idle_img

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "main"})


class DropDownMenuScreen(Screen):
    NAME = "drop_down_menu"

    def __init__(self):
        super().__init__()
        self.bg_img = dropdown_img_1
        self.meta = dropdown
        # 显示时间
        self.dropdown_time_1 = dropdown_time_1
        # 上午下午
        self.dropdown_time_2 = dropdown_time_2
        # 显示日期
        self.dropdown_date_1 = dropdown_date_1
        # 界面信号功能
        self.dropdown_img_3 = dropdown_img_3
        # 4G信号
        self.dropdown_label_3 = dropdown_label_3
        # operate 运营商
        self.dropdown_label_2 = dropdown_label_2
        # 时间
        self.dropdown_label_1 = dropdown_label_1
        # 显示充电
        self.dropdown_img_11 = dropdown_img_11
        # 电池电量空间
        self.dropdown_img_4 = dropdown_img_4
        # 电池电量的百分比
        self.dropdown_label_4 = dropdown_label_4
        # 体温
        self.dropdown_temperature_value = dropdown_temperature_value
        # 步数
        self.dropdown_step_value = dropdown_step_value

        dropdown_imgbtn_1.add_event_cb(lambda e: self.load_screen(e, {"screen": "addr_book"}), lv.EVENT.PRESSED, None)
        dropdown_imgbtn_2.add_event_cb(lambda e: self.load_screen(e, {"screen": "msg_detail"}), lv.EVENT.PRESSED, None)
        dropdown_imgbtn_3.add_event_cb(lambda e: self.load_screen(e, {"screen": "cli_list"}), lv.EVENT.PRESSED, None)

    def post_processor_after_initialization(self):
        EventMesh.subscribe("signal", self.__signal_cb)
        EventMesh.subscribe("time", self.__time_cb)
        EventMesh.subscribe("battery", self.__battery_cb)
        EventMesh.subscribe("net_show", self.__net_cb)
        EventMesh.subscribe("topic_push_temperature_record", self.__temperature_record)
        EventMesh.subscribe("topic_push_step_count", self.__step_count)
        pass

    def initialization(self):
        signal = self.publish_sig()
        if signal:
            self.__signal_cb(None, signal)
        # 获取电池电量
        battery = self.publish_battery()
        if battery:
            self.__battery_cb(None, battery)
        # 获取运营商
        ope = self.publish_ope()
        if ope:
            self.__ope_show(None, ope)
        # 获取时间
        time = self.publish_time()
        if time:
            self.__time_cb(None, time)

        temperature_record = EventMesh.publish("topic_get_temperature_record")
        if temperature_record:
            self.__temperature_record(None, temperature_record)

        step_count = EventMesh.publish("topic_get_step_count")
        if step_count:
            self.__step_count(None, step_count)

    def __time_cb(self, event, msg):
        self.dropdown_time_1.set_text(msg[0])
        self.dropdown_time_2.set_text(msg[1])
        self.dropdown_date_1.set_text(msg[2])
        self.dropdown_label_1.set_text(msg[0])

    def __signal_cb(self, event, msg):
        # TODO 需要支持信号操作
        if msg:
            self.dropdown_img_3.set_src("U:/static/mpsignal{}.png".format(msg))

    def __ope_show(self, event, msg):
        # 目前只支持中国移动
        pass

    def __battery_cb(self, event, msg):
        if msg[0] == '1':
            self.dropdown_img_11.set_src("U:/static/charge_in.png")
        else:
            self.dropdown_img_11.set_src("U:/static/charge_in1.png")

        self.dropdown_img_4.set_src(msg[1])

    def __temperature_record(self, event, msg):
        self.dropdown_temperature_value.set_text(msg)

    def __step_count(self, event, msg):
        self.dropdown_step_value.set_text(msg)

    def __net_cb(self, event, msg):
        # TODO callback
        pass
        # self.main_top_net.set_text(msg)

    def src_load(self, e, screen_name):
        EventMesh.publish("load_screen", {"screen": screen_name})

    def done_bottom_to_top(self):
        EventMesh.publish("load_screen", {"screen": "main"})


class MenuScreen(Screen):
    NAME = "menu"

    def __init__(self):
        super().__init__()
        self.meta = menu
        self.bg_img = menu_1
        menu_msg.add_event_cb(lambda e: self.load_screen(e, {"screen": "msg_detail"}), lv.EVENT.LONG_PRESSED, None)
        menu_phone.add_event_cb(lambda e: self.load_screen(e, {"screen": "addr_book"}), lv.EVENT.LONG_PRESSED, None)
        menu_class.add_event_cb(lambda e: self.load_screen(e, {"screen": "class_date"}), lv.EVENT.LONG_PRESSED, None)
        menu_setting.add_event_cb(lambda e: self.load_screen(e, {"screen": "settings"}), lv.EVENT.LONG_PRESSED, None)

    def done_left_to_right(self):
        self.done_return()

    def done_right_to_left(self):
        EventMesh.publish("load_screen", {"screen": "menu2"})

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "main"})

    def btn8_press(self):
        EventMesh.publish("load_screen", {"screen": "main"})


class Menu2Screen(Screen):
    NAME = "menu2"

    def __init__(self):
        super().__init__()
        self.bg_img = menu2_1
        self.meta = menu_2
        menu2_clk.add_event_cb(lambda e: self.load_screen(e, {"screen": "clk_list"}), lv.EVENT.LONG_PRESSED, None)
        menu2_qrcode.add_event_cb(lambda e: self.load_screen(e, {"screen": "qrcode"}), lv.EVENT.LONG_PRESSED, None)
        menu2_shutdown.add_event_cb(lambda e: self.load_screen(e, {"screen": "power_down"}), lv.EVENT.LONG_PRESSED,
                                    None)
        menu2_health_qrcode.add_event_cb(lambda e: self.load_screen(e, {"screen": "health_qrcode"}),
                                         lv.EVENT.LONG_PRESSED,
                                         None)

    def done_left_to_right(self):
        EventMesh.publish("load_screen", {"screen": "menu"})

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "main"})

    def btn8_press(self):
        EventMesh.publish("load_screen", {"screen": "main"})


class AddrBookScreen(Screen):
    NAME = "addr_book"

    def __init__(self):
        super().__init__()
        self.e = None
        self.bg_img = addr_book2_1
        self.meta = addr_book

        self.addr_book_list_1 = addr_book_list_1
        self.group_list = []
        self._btn_list = []
        self.count = 0
        self.e = None

    def post_processor_before_initialization(self):
        EventMesh.subscribe("push_addr_book_list", self.get_addr_book_list)
        self.__content_create()

    def get_addr_book_list(self, event, msg):
        self.group_list = msg

    def initialization(self):
        if not self.group_list:
            group_list = EventMesh.publish("get_addr_book_list")
            self.group_list = group_list
            self.__content_create()

    def __content_create(self):
        if self.count:
            self.addr_book_list_1.delete()
        print("content create {}".format(self.group_list))
        self.addr_book_list_1 = lv.list(addr_book2)
        self.addr_book_list_1.set_pos(15, 54)
        self.addr_book_list_1.set_size(215, 156)
        self.addr_book_list_1.set_style_pad_left(2, 0)
        self.addr_book_list_1.set_style_pad_top(4, 0)
        self.addr_book_list_1.set_style_pad_row(3, 0)
        self.addr_book_list_1.add_style(style_list, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.addr_book_list_1.add_style(style_list_scro, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)
        for i, each in enumerate(self.group_list):
            _btn = lv.btn(self.addr_book_list_1)
            _btn.set_size(205, 45)
            _btn.add_event_cb(lambda e: self.btn_click(e, i),
                              lv.EVENT.LONG_PRESSED,
                              None)
            _btn.add_style(style_list, lv.PART.MAIN | lv.STATE.DEFAULT)
            _btn_img = lv.img(_btn)
            _btn_img.set_pos(0, 5)
            _btn_img.set_size(25, 25)
            _btn_img.set_src('U:/static/mp1480923465.png')
            _btn_label = lv.label(_btn)
            _btn_label.set_pos(25, 5)
            _btn_label.set_size(180, 25)
            _btn_label.set_text(each[0] + " " + each[1])
            _btn_label.set_long_mode(lv.label.LONG.SCROLL_CIRCULAR)
            _btn_label.add_style(style_font_regular_18_space_2_default_anim, lv.PART.MAIN | lv.STATE.DEFAULT)
            self._btn_list.append((_btn, _btn_img, _btn_label))

    def btn_click(self, e, i):
        _msg = e.get_target().get_child(1).get_text()
        EventMesh.publish("load_screen", {"screen": "addr_detail", "meta": _msg.split(" ")})

    def done_right_to_left(self):
        EventMesh.publish("load_screen", {"screen": "call_log"})

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "menu"})

    def btn8_release(self):
        EventMesh.publish("load_screen", {"screen": "menu"})

    def load_screen(self, e, msg):
        self.e = e
        print(e.target)
        # EventMesh.publish("load_screen", msg)


class MsgDetailScreen(Screen):
    NAME = "msg_detail"

    def __init__(self):
        super().__init__()
        self.bg_img = msg_detail2_1
        self.meta = msg_detail
        self.msg_detail_msg = msg_detail_msg

    def initialization(self):
        job_detail = EventMesh.publish("get_class_job_detail")
        if job_detail:
            self.msg_detail_msg.set_text(job_detail)

    def done_return(self):
        EventMesh.publish("load_screen", self.last_screen_info)

    def btn8_press(self):
        self.done_return()


class ClassDetailScreen(Screen):
    """课程详情页面"""
    NAME = "class_detail"

    def __init__(self):
        super().__init__()
        self.bg_img = class_detail2_1
        self.meta = class_detail
        self.class_detail_title = class_detail_title
        self.morn_class = (class_detail_label_3, class_detail_label_4, class_detail_label_5, class_detail_label_6)
        self.after_class = (class_detail_label_8, class_detail_label_9, class_detail_label_10, class_detail_label_11)
        self.night_class = (class_detail_label_13, class_detail_label_14, class_detail_label_15, class_detail_label_16)

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "class_date"})

    def initialization(self):
        if not self.meta_info:
            self.meta_info = 7
        _class_detail = EventMesh.publish("get_class_detail", self.meta_info)
        self.class_detail_title.set_text(_class_detail["name"])
        for _i, _m_c in enumerate(self.morn_class):
            _m_c.set_text(_class_detail["morn"][_i])
        for _i, _a_c in enumerate(self.after_class):
            _a_c.set_text(_class_detail["after"][_i])
        for _i, _n_c in enumerate(self.night_class):
            _n_c.set_text(_class_detail["night"][_i])


class ClassDateScreen(Screen):
    """课程日期"""
    NAME = "class_date"

    class CHOICE_ENUM:
        CHECKED = "U:/static/mp-1897490797.png"
        FREE = "U:/static/mp-814621292.png"

    def __init__(self):
        super().__init__()
        self.meta = class_date
        self.bg_img = class_date2_1
        self.images_list = [
            [class_date_img_7, self.CHOICE_ENUM.FREE],
            [class_date_img_1, self.CHOICE_ENUM.CHECKED],
            [class_date_img_2, self.CHOICE_ENUM.FREE],
            [class_date_img_3, self.CHOICE_ENUM.FREE],
            [class_date_img_4, self.CHOICE_ENUM.FREE],
            [class_date_img_5, self.CHOICE_ENUM.FREE],
            [class_date_img_6, self.CHOICE_ENUM.FREE],
        ]
        class_date_btn_1.add_event_cb(lambda e: self.choice(e, {"screen": "class_detail", "date": "星期一", "meta": 1}),
                                      lv.EVENT.PRESSED, None)
        class_date_btn_2.add_event_cb(lambda e: self.choice(e, {"screen": "class_detail", "date": "星期二", "meta": 2}),
                                      lv.EVENT.PRESSED, None)
        class_date_btn_3.add_event_cb(lambda e: self.choice(e, {"screen": "class_detail", "date": "星期三", "meta": 3}),
                                      lv.EVENT.PRESSED, None)
        class_date_btn_4.add_event_cb(lambda e: self.choice(e, {"screen": "class_detail", "date": "星期四", "meta": 4}),
                                      lv.EVENT.PRESSED, None)
        class_date_btn_5.add_event_cb(lambda e: self.choice(e, {"screen": "class_detail", "date": "星期五", "meta": 5}),
                                      lv.EVENT.PRESSED, None)
        class_date_btn_6.add_event_cb(lambda e: self.choice(e, {"screen": "class_detail", "date": "星期六", "meta": 6}),
                                      lv.EVENT.PRESSED, None)
        class_date_btn_7.add_event_cb(lambda e: self.choice(e, {"screen": "class_detail", "date": "星期日", "meta": 0}),
                                      lv.EVENT.PRESSED, None)

    def choice(self, e, msg):
        """判断是否被选中, 选中, 点击check按键择会进入, 否则赋值ok按键"""
        if self.images_list[msg['meta']][1] == self.CHOICE_ENUM.CHECKED:
            self.load_screen(e, msg)
        _i = 0
        for image_info in self.images_list:
            if image_info[1] == self.CHOICE_ENUM.CHECKED:
                image_info[1] = self.CHOICE_ENUM.FREE
                image_info[0].set_src(self.CHOICE_ENUM.FREE)
            if _i == msg["meta"]:
                image_info[1] = self.CHOICE_ENUM.CHECKED
                image_info[0].set_src(self.CHOICE_ENUM.CHECKED)
            _i += 1

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "menu"})


class MenuQrcodeScreen(Screen):
    NAME = "qrcode"

    def __init__(self):
        super().__init__()
        self.meta = qrcode
        self.bg_img = qrcode2_1

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "menu2"})


class SettingsScreen(Screen):
    NAME = "settings"

    def __init__(self):
        super().__init__()
        self.meta = setting_scr
        self.bg_img = setting_scr2_1
        setting_scr_btn_1.add_event_cb(lambda e: self.load_screen(e, {"screen": "settings_volume"}),
                                       lv.EVENT.LONG_PRESSED, None)
        setting_scr_btn_2.add_event_cb(lambda e: self.load_screen(e, {"screen": "settings_brightness"}),
                                       lv.EVENT.LONG_PRESSED, None)
        setting_scr_btn_3.add_event_cb(lambda e: self.load_screen(e, {"screen": "settings_wallpaper"}),
                                       lv.EVENT.LONG_PRESSED, None)
        setting_scr_btn_4.add_event_cb(lambda e: self.load_screen(e, {"screen": "time_mode"}),
                                       lv.EVENT.LONG_PRESSED, None)
        setting_scr_btn_5.add_event_cb(lambda e: self.load_screen(e, {"screen": "mode"}),
                                       lv.EVENT.LONG_PRESSED, None)
        setting_scr_btn_6.add_event_cb(lambda e: self.load_screen(e, {"screen": "version_update"}),
                                       lv.EVENT.LONG_PRESSED, None)
        setting_scr_btn_7.add_event_cb(lambda e: self.load_screen(e, {"screen": "settings_about"}),
                                       lv.EVENT.LONG_PRESSED, None)
        setting_scr_btn_8.add_event_cb(lambda e: self.load_screen(e, {"screen": "call_record"}),
                                       lv.EVENT.LONG_PRESSED, None)

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "menu"})

    def btn8_press(self):
        self.done_return()


class AboutScreen(Screen):
    NAME = "settings_about"

    def __init__(self):
        super().__init__()
        self.meta = about
        self.bg_img = about2_1
        self.about_label_1 = about_label_1

    def initialization(self):
        info = EventMesh.publish("get_about_info")
        if info:
            self.about_label_1.set_text(info)

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "settings"})


class VersionUpdateScreen(Screen):
    NAME = "version_update"

    def __init__(self):
        super().__init__()
        self.meta = version_update
        self.bg_img = version_update2_1
        self.version_update_label_1 = version_update_label_1

    def initialization(self):
        info = EventMesh.publish("get_version_update_info")
        if info:
            self.version_update_label_1.set_text(info)

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "settings"})


class SettingsVolumeScreen(Screen):
    NAME = "settings_volume"

    def __init__(self):
        super().__init__()
        self.meta = volume
        self.bg_img = volume2_1
        volume_imgbtn_1.add_event_cb(lambda e: self.volume_reduce(e),
                                     lv.EVENT.PRESSED, None)
        volume_imgbtn_2.add_event_cb(lambda e: self.volume_add(e),
                                     lv.EVENT.PRESSED, None)

        self.voice = 0

    def volume_add(self, e):
        EventMesh.publish("push_add_device_voice")
        self.voice = EventMesh.publish("get_device_voice")
        self.show_bar()

    def volume_reduce(self, e):
        EventMesh.publish("push_reduce_device_voice")
        self.voice = EventMesh.publish("get_device_voice")
        self.show_bar()

    def show_bar(self):
        volume_bar_1.set_value((100 // 10) * self.voice, lv.ANIM.OFF)

    def initialization(self):
        self.voice = EventMesh.publish("get_device_voice")
        self.show_bar()

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "settings"})


class SettingBrightNessScreen(Screen):
    NAME = "settings_brightness"

    def __init__(self):
        super().__init__()
        self.meta = brightness
        self.bg_img = brightness2_1
        self.level = 0
        brightness_imgbtn_1.add_event_cb(lambda e: self.reduce_level(e),
                                         lv.EVENT.PRESSED, None)
        brightness_imgbtn_2.add_event_cb(lambda e: self.add_level(e),
                                         lv.EVENT.PRESSED, None)

    def add_level(self, e):
        EventMesh.publish("push_add_brightness_level")
        self.level = EventMesh.publish("get_brightness_level")
        self.show_bar()

    def reduce_level(self, e):
        EventMesh.publish("push_reduce_brightness_level")
        self.level = EventMesh.publish("get_brightness_level")
        self.show_bar()

    def show_bar(self):
        brightness_bar_1.set_value((100 // 4) * self.level, lv.ANIM.OFF)

    def initialization(self):
        self.level = EventMesh.publish("get_brightness_level")
        self.show_bar()

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "settings"})


class SettingWallPaperScreen(Screen):
    NAME = "settings_wallpaper"

    class CHECKED:
        NO = "U:/static/mp-861665386.png"
        YES = "U:/static/mp-1007005535.png"

        @classmethod
        def get(cls, i):
            if i:
                return cls.YES
            else:
                return cls.NO

    def __init__(self):
        super().__init__()
        self.meta = bg_select
        bg_select_imgbtn_1.add_event_cb(lambda e: self.checked(e),
                                        lv.EVENT.PRESSED, None)
        bg_select_imgbtn_2.add_event_cb(lambda e: self.last(e),
                                        lv.EVENT.PRESSED, None)
        bg_select_imgbtn_3.add_event_cb(lambda e: self.next(e),
                                        lv.EVENT.PRESSED, None)
        self.i = 0
        self.bg_img_list = []

    def checked(self, e):
        check = self.bg_img_list[self.i]["checked"] != 1
        if check:
            EventMesh.publish("set_wall_paper_mode", self.i)
            self.bg_img_list = EventMesh.publish("get_bg_img_list")
            self.change_checked(check)

    def change_checked(self, _check):
        bg_select_imgbtn_1.set_src(self.CHECKED.get(_check))

    def next(self, e):
        if self.i < len(self.bg_img_list):
            self.i += 1
        else:
            self.i = 0
        print("next i = {}".format(self.i))
        bg_select_img_1.set_src(self.bg_img_list[self.i]["url"])
        self.change_checked(self.bg_img_list[self.i]["checked"])

    def last(self, e):
        if self.i > 0:
            self.i -= 1
        else:
            self.i = len(self.bg_img_list) - 1
        print("last i = {}".format(self.i))
        bg_select_img_1.set_src(self.bg_img_list[self.i]["url"])
        self.change_checked(self.bg_img_list[self.i]["checked"])

    def get_bg_img(self, topic=None, msg=None):
        self.bg_img_list = EventMesh.publish("get_bg_img_list")
        for i, _bg_img_info in enumerate(self.bg_img_list):
            if _bg_img_info["checked"] == 1:
                print("_bg_img_info[url] = {}".format(_bg_img_info["url"]))
                bg_select_img_1.set_src(_bg_img_info["url"])
                self.i = i
        self.change_checked(1)

    def left(self, e):
        if self.i > 0:
            self.i -= 1
            bg_select_img_1.set_src(self.bg_img_list[self.i])

    def right(self, e):
        if self.i > 0:
            self.i -= 1
            bg_select_img_1.set_src(self.bg_img_list[self.i])

    def done_left_to_right(self):
        self.last(None)

    def done_right_to_left(self):
        self.next(None)

    def push(self, e):
        pass

    def initialization(self):
        self.get_bg_img()

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "settings"})


class SettingTimeModeScreen(Screen):
    NAME = "time_mode"

    class CHECKED:
        NO = "U:/static/mp-861665386.png"
        YES = "U:/static/mp-1364748740.png"

    def __init__(self):
        super().__init__()
        self.meta = time_mode
        self.bg_img = time_mode2_1
        self.mode_select_list = [time_mode_select1, time_mode_select2]
        self.i = 0
        time_mode_select1.add_event_cb(lambda e: self.choice_mode(e, 0),
                                       lv.EVENT.PRESSED, None)
        time_mode_select2.add_event_cb(lambda e: self.choice_mode(e, 1),
                                       lv.EVENT.PRESSED, None)

    def choice_mode(self, e, _i):
        print("choice_mode = {}", _i)
        if _i == self.i:
            return
        else:
            EventMesh.publish("push_time_mode", _i)
            self.show_bar(_i)

    def show_bar(self, _i=None):
        if _i is not None:
            self.i = _i
        for idx, _mode in enumerate(self.mode_select_list):
            if idx == self.i:
                _mode.set_src(self.CHECKED.YES)
            else:
                _mode.set_src(self.CHECKED.NO)

    def initialization(self):
        self.i = EventMesh.publish("get_time_mode")
        self.show_bar()

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "settings"})


class SettingContextualModelModeScreen(Screen):
    NAME = "mode"

    class CHECKED:
        NO = "U:/static/mp-861665386.png"
        YES = "U:/static/mp-1364748740.png"

    def __init__(self):
        super().__init__()
        self.meta = mode
        self.i = 0
        self.bg_img = mode2_1
        self.mode_select_list = [mode_img_1_2, mode_img_2_2, mode_img_3_2, mode_img_4_2]
        mode_img_1_2.add_event_cb(lambda e: self.choice_mode(e, 0),
                                  lv.EVENT.PRESSED, None)
        mode_img_2_2.add_event_cb(lambda e: self.choice_mode(e, 1),
                                  lv.EVENT.PRESSED, None)
        mode_img_3_2.add_event_cb(lambda e: self.choice_mode(e, 2),
                                  lv.EVENT.PRESSED, None)
        mode_img_4_2.add_event_cb(lambda e: self.choice_mode(e, 3),
                                  lv.EVENT.PRESSED, None)

    def choice_mode(self, e, _i):
        print("choice_mode = {}", _i)
        if _i == self.i:
            return
        else:
            EventMesh.publish("push_contextual_model_mode", _i)
            self.show_bar(_i)

    def show_bar(self, _i=None):
        if _i is not None:
            self.i = _i
        for idx, _mode in enumerate(self.mode_select_list):
            if idx == self.i:
                _mode.set_src(self.CHECKED.YES)
            else:
                _mode.set_src(self.CHECKED.NO)

    def initialization(self):
        self.i = EventMesh.publish("get_contextual_model_mode")
        self.show_bar()

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "settings"})


class ClearCallRecordMode(Screen):
    NAME = "call_record"

    def __init__(self):
        super().__init__()
        self.meta = del_log
        self.bg_img = del_log2_1
        del_log_imgbtn_1.add_event_cb(lambda e:
                                      self.load_screen(e, {"screen": "settings"}),
                                      lv.EVENT.PRESSED,
                                      None)
        del_log_imgbtn_2.add_event_cb(lambda e:
                                      self.clear_call_log_history(e),
                                      lv.EVENT.PRESSED,
                                      None)

    def clear_call_log_history(self, e):
        EventMesh.publish("clear_call_log_history")
        EventMesh.publish("load_screen", {"screen": "settings"})

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "settings"})

    def btn8_press(self):
        self.done_return()


class ClkListScreen(Screen):
    NAME = "clk_list"

    def __init__(self):
        super().__init__()
        self.meta = clk_list
        self.bg_img = clk_list2_1
        clk_list_imgbtn_1.add_event_cb(lambda e:
                                       self.load_screen(e, {"screen": "new_edit_clk",
                                                            "meta": {"title": "新建闹钟", "mode": 0}}),
                                       lv.EVENT.PRESSED,
                                       None)
        self.show_date_list = ["日", "一", "二", "三", "四", "五", "六"]
        self.show_ring_tong_list = ["震动", "铃声", "震动加铃声"]
        self.clock_list = []
        self.btn_list = []

    def initialization(self):
        self.clock_list = EventMesh.publish("get_clock_info_list")
        for idx, item in enumerate(self.clock_list):
            clk_list_cont_1 = lv.obj(clk_list_cont)
            clk_list_cont_1.clear_flag(lv.obj.FLAG.SCROLLABLE)
            clk_list_cont_1.set_pos(3, 3 + 60 * idx)
            clk_list_cont_1.set_size(160, 50)
            clk_list_cont_1.add_flag(lv.obj.FLAG.CLICKABLE)
            clk_list_cont_1.add_event_cb(lambda e:
                                         self.handler(e),
                                         lv.EVENT.LONG_PRESSED,
                                         None)
            _clk_list_label = lv.label(clk_list_cont_1)
            _clk_list_label.set_size(0, 0)
            _clk_list_label.set_text(str(idx))
            clk_list_sw_1 = lv.switch(clk_list_cont_1)
            clk_list_sw_1.set_pos(0, 10)
            clk_list_sw_1.set_size(40, 20)
            if item["checked"]:
                print("checked ~~~~~")
                clk_list_sw_1.add_state(lv.STATE.CHECKED)
            else:
                print("unchecked ~~~~~")
                clk_list_sw_1.clear_state(lv.STATE.CHECKED)
            clk_list_sw_1.add_style(sw_style, lv.PART.MAIN | lv.STATE.DEFAULT)
            clk_list_sw_1.add_style(sw_69b7f7_style, lv.PART.INDICATOR | lv.STATE.CHECKED)
            clk_list_sw_1.add_style(sw_black_style, lv.PART.KNOB | lv.STATE.DEFAULT)
            clk_list_sw_1.add_event_cb(lambda e:
                                       self.switch_event_cb(e),
                                       lv.EVENT.VALUE_CHANGED,
                                       None)

            clk_list_label_4 = lv.label(clk_list_cont_1)
            clk_list_label_4.set_pos(50, 10)
            clk_list_label_4.set_size(100, 18)
            _t = "%02d" % item['time']['hour'] + ":%02d" % item['time']['min'] + (
                "AM" if item['time']["hour"] < 12 else "PM")
            print("_t = {}".format(_t))
            clk_list_label_4.set_text(_t)
            clk_list_label_4.set_long_mode(lv.label.LONG.WRAP)
            clk_list_label_4.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
            clk_list_label_4.add_style(style_font_regular_18_space_2_white, lv.PART.MAIN | lv.STATE.DEFAULT)

            clk_list_label_3 = lv.label(clk_list_cont_1)
            clk_list_label_3.set_pos(20, -14)
            clk_list_label_3.set_size(120, 18)
            period_list = item['period_list']
            if period_list:
                period_list = sorted(period_list)
            show_date = ""
            for i in period_list:
                show_date += self.show_date_list[i]
            if not show_date:
                show_date = "无"
            clk_list_label_3.set_text(show_date)
            clk_list_label_3.set_long_mode(lv.label.LONG.WRAP)
            clk_list_label_3.set_style_text_align(lv.TEXT_ALIGN.RIGHT, 0)
            clk_list_label_3.add_style(style_font_regular_18_space_0_white,
                                       lv.PART.MAIN | lv.STATE.DEFAULT)

            clk_list_label_2 = lv.label(clk_list_cont_1)
            clk_list_label_2.set_pos(-8, -10)
            clk_list_label_2.set_text("闹钟{}".format(idx + 1))
            clk_list_label_2.set_long_mode(lv.label.LONG.WRAP)
            clk_list_label_2.add_style(style_font_regular_14_space_0_white,
                                       lv.PART.MAIN | lv.STATE.DEFAULT)

            self.btn_list.append(
                [clk_list_cont_1, _clk_list_label, clk_list_sw_1, clk_list_label_2, clk_list_label_3, clk_list_label_4])

    def deactivate(self):
        self.btn_list = []

    def handler(self, e):
        idx = int(e.get_target().get_child(0).get_text())
        _default = {"title": "修改闹钟", "mode": 1}
        clock_info = self.clock_list[idx]
        clock_info["idx"] = idx
        clock_info.update(_default)
        self.load_screen(e, {"screen": "new_edit_clk",
                             "meta": clock_info}),

    def switch_event_cb(self, e):
        obj = e.get_target()
        idx = int(e.get_target().get_parent().get_child(0).get_text())
        clock_info = self.clock_list[idx]
        clock_info["idx"] = idx
        if obj.has_state(lv.STATE.CHECKED):
            print("ON ~~~")
            clock_info["checked"] = 1
        else:
            print("OFF ~~~")
            clock_info["checked"] = 0
        EventMesh.publish("push_clock_info", clock_info)
        print("sw_event_cb ~~~")

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "menu2"})


class NewEditClk(Screen):
    NAME = "new_edit_clk"

    def __init__(self):
        super().__init__()
        self.meta = new_edit_clk
        self.bg_img = new_edit_clk2_1
        self.show_date_list = ["日", "一", "二", "三", "四", "五", "六"]
        self.show_ring_tong_list = ["震动", "铃声", "震动加铃声"]
        # new_edit_clk_label_4.add_event_cb(lambda e:)
        new_edit_clk_cont_1.add_event_cb(lambda e: self.load_clk_time(e), lv.EVENT.PRESSED, None)
        new_edit_clk_cont_2.add_event_cb(lambda e: self.load_clk_period(e), lv.EVENT.PRESSED, None)
        new_edit_clk_cont_3.add_event_cb(lambda e: self.load_clk_ring_tong(e), lv.EVENT.PRESSED, None)
        new_edit_clk_imgbtn_1.add_event_cb(lambda e: self.add_clock_info(e), lv.EVENT.PRESSED, None)

    def load_clk_time(self, e):
        EventMesh.publish("load_screen", {"screen": "clk_time", "meta": self.meta_info})

    def load_clk_period(self, e):
        EventMesh.publish("load_screen", {"screen": "clk_period", "meta": self.meta_info})

    def load_clk_ring_tong(self, e):
        EventMesh.publish("load_screen", {"screen": "clk_ringtone", "meta": self.meta_info})

    def initialization(self):
        if not self.meta_info["mode"] and not self.meta_info.get("opt"):
            self.meta_info.update({
                "time": {
                    "hour": 0,
                    "min": 0
                },
                "period_list": [],
                "ring_tone_mode": 0,
                "checked": 0
            })
        print("meta_info = {}".format(self.meta_info))
        new_edit_clk_title.set_text(self.meta_info['title'])
        new_edit_clk_label_4.set_text(
            "%02d" % self.meta_info['time']['hour'] + ":%02d" % self.meta_info['time']['min'] + (
                "AM" if self.meta_info['time']["hour"] < 12 else "PM"))
        period_list = self.meta_info.get("period_list")
        if period_list:
            period_list = sorted(period_list)
        show_date = ""
        for i in period_list:
            show_date += self.show_date_list[i]
        if show_date:
            new_edit_clk_label_2_5.set_text(show_date)
        else:
            new_edit_clk_label_2_5.set_text("无")
        new_edit_clk_label_3_5.set_text(self.show_ring_tong_list[self.meta_info["ring_tone_mode"]])

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "clk_list"})

    def add_clock_info(self, e):
        EventMesh.publish("push_clock_info", self.meta_info)
        EventMesh.publish("load_screen", {"screen": "clk_list"})


class CLKTimeScreen(Screen):
    NAME = "clk_time"

    def __init__(self):
        super().__init__()
        self.meta = clk_time
        imgbtn_ok.add_event_cb(lambda e: self.handler(e), lv.EVENT.PRESSED, None)

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "new_edit_clk", "meta": self.meta_info})

    def btn8_press(self):
        EventMesh.publish("load_screen", {"screen": "new_edit_clk", "meta": self.meta_info})

    def handler(self, e):
        option_1 = " " * 10
        option_2 = " " * 10
        clk_time_roller_2.get_selected_str(option_2, len(option_2))
        clk_time_roller_1.get_selected_str(option_1, len(option_1))
        option_1_strip = option_1.strip()[:2]
        option_2_strip = option_2.strip()[:2]
        print("option_1_strip = {} option_2_strip = {}".format(option_1_strip, option_2_strip))
        self.meta_info["time"]["hour"] = int(option_1_strip)
        self.meta_info["time"]["min"] = int(option_2_strip)
        EventMesh.publish("load_screen", {"screen": "new_edit_clk", "meta": self.meta_info})

    def initialization(self):
        roll_1_v = self.meta_info["time"]["hour"]
        roll_2_v = self.meta_info["time"]["min"]
        self.meta_info["opt"] = 1
        clk_time_roller_1.set_selected(int(roll_1_v), lv.ANIM.ON)
        clk_time_roller_2.set_selected(int(roll_2_v), lv.ANIM.ON)


class ClkPeriod(Screen):
    NAME = "clk_period"

    class CHECKED:
        NO = "U:/static/mp-861665386.png"
        YES = "U:/static/mp-1364748740.png"

        @classmethod
        def get(cls, e):
            if e:
                return cls.YES
            else:
                return cls.NO

    def __init__(self):
        super().__init__()
        self.meta = clk_period
        self.bg_img = clk_period2_1
        self.choice_list = []
        self.clk_period_list = [
            clk_period_img_7,
            clk_period_img_1,
            clk_period_img_2,
            clk_period_img_3,
            clk_period_img_4,
            clk_period_img_5,
            clk_period_img_6,

        ]
        clk_period_cont_1.add_event_cb(lambda e: self.choice(e, 1), lv.EVENT.LONG_PRESSED, None)
        clk_period_cont_2.add_event_cb(lambda e: self.choice(e, 2), lv.EVENT.LONG_PRESSED, None)
        clk_period_cont_3.add_event_cb(lambda e: self.choice(e, 3), lv.EVENT.LONG_PRESSED, None)
        clk_period_cont_4.add_event_cb(lambda e: self.choice(e, 4), lv.EVENT.LONG_PRESSED, None)
        clk_period_cont_5.add_event_cb(lambda e: self.choice(e, 5), lv.EVENT.LONG_PRESSED, None)
        clk_period_cont_6.add_event_cb(lambda e: self.choice(e, 6), lv.EVENT.LONG_PRESSED, None)
        clk_period_cont_7.add_event_cb(lambda e: self.choice(e, 0), lv.EVENT.LONG_PRESSED, None)

    def choice_img_init(self):
        for item in self.clk_period_list:
            item.set_src(self.CHECKED.NO)

    def choice(self, e, i, _init=False):
        if i in self.choice_list:
            self.clk_period_list[i].set_src(self.CHECKED.NO)
            self.choice_list.remove(i)
        else:
            self.clk_period_list[i].set_src(self.CHECKED.YES)
            self.choice_list.append(i)
        if not _init:
            self.meta_info["period_list"] = self.choice_list

    def initialization(self):
        self.choice_img_init()
        self.choice_list = self.meta_info["period_list"]
        self.meta_info["opt"] = 1
        for i in self.choice_list:
            self.clk_period_list[i].set_src(self.CHECKED.YES)

    def done_return(self):
        print("done_return load_screen {}".format("new_edit_clk"))
        EventMesh.publish("load_screen", {"screen": "new_edit_clk", "meta": self.meta_info})

    def btn8_press(self):
        self.done_return()


class ClkRingTong(Screen):
    NAME = "clk_ringtone"

    class CHECKED:
        NO = "U:/static/mp-861665386.png"
        YES = "U:/static/mp-1364748740.png"

    def __init__(self):
        super().__init__()
        self.meta = clk_ringtone
        self.bg_img = clk_ringtone2_1
        self.choice_ring_tong_list = [
            clk_ringtone_img_1,
            clk_ringtone_img_2,
            clk_ringtone_img_3,
        ]
        clk_ringtone_cont_1.add_event_cb(lambda e: self.choice(e, 0), lv.EVENT.LONG_PRESSED, None)
        clk_ringtone_cont_2.add_event_cb(lambda e: self.choice(e, 1), lv.EVENT.LONG_PRESSED, None)
        clk_ringtone_cont_3.add_event_cb(lambda e: self.choice(e, 2), lv.EVENT.LONG_PRESSED, None)
        self.ring_tone_mode = 0

    def choice_img_init(self):
        for item in self.choice_ring_tong_list:
            item.set_src(self.CHECKED.NO)

    def choice(self, e, i, _init=False):
        if i == self.ring_tone_mode:
            return
        for idx, rt in enumerate(self.choice_ring_tong_list):
            if i == idx:
                rt.set_src(self.CHECKED.YES)
                self.ring_tone_mode = i
                self.meta_info["ring_tone_mode"] = i
            else:
                rt.set_src(self.CHECKED.NO)

    def initialization(self):
        self.choice_img_init()
        self.meta_info["opt"] = 1
        self.ring_tone_mode = self.meta_info["ring_tone_mode"]
        self.choice_ring_tong_list[self.ring_tone_mode].set_src(self.CHECKED.YES)

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "new_edit_clk", "meta": self.meta_info})

    def btn8_press(self):
        self.done_return()


class AddrDetailScreen(Screen):
    NAME = "addr_detail"

    def __init__(self):
        super().__init__()
        self.meta = addr_detail
        self.bg_img = addr_detail2_1
        self.addr_detail_name = addr_detail_name
        self.addr_detail_phone = addr_detail_phone

    def initialization(self):
        self.addr_detail_name.set_text(self.meta_info[0])
        self.addr_detail_phone.set_text(self.meta_info[1])

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "addr_book"})


class CallScreen(Screen):
    NAME = "call"

    class SPEAK_STATE(object):
        IN = "U:/static/mp2109784762.png"
        OUT = "U:/static/mp2109784762_out.png"

        @classmethod
        def get(cls, msg):
            if msg == 1:
                return cls.IN
            else:
                return cls.OUT

    class DAIL_STATE(object):
        INITIATIVE = "U:/static/mpcallout.png"
        PASV = "U:/static/mpcallin.png"

        @classmethod
        def get(cls, msg):
            if msg == 1:
                return cls.INITIATIVE
            else:
                return cls.PASV

    def __init__(self):
        super().__init__()
        self.meta = call
        self.bg_img = call2_1
        self.call_name = call_name
        self.call_phone = call_phone
        self.call_state = call_state
        call_speaker.add_event_cb(lambda e: self.call_speaker_click(e),
                                  lv.EVENT.PRESSED, None)
        call_answer.add_event_cb(lambda e: self.call_answer_click(e),
                                 lv.EVENT.PRESSED, None)
        self.__speak_state = 0
        self.__dail_state = 0

    def call_speaker_click(self, e=None):
        print("call_speaker_click = {}")
        self.__speak_state = 1 ^ self.__speak_state
        call_speaker.set_src(self.SPEAK_STATE.get(self.__speak_state))

    def call_answer_click(self, e=None):
        print("call_answer_click = {}".format(self.__dail_state))
        self.__dail_state = 1 ^ self.__dail_state
        call_answer.set_src(self.DAIL_STATE.get(self.__dail_state))
        if self.__dail_state == 0:
            self.done_return()
        EventMesh.publish("call_user_answer", self.__dail_state)

    def btn6_press(self):
        self.call_answer_click(None)

    def done_return(self):
        EventMesh.publish("push_cancel_call")
        EventMesh.publish("load_screen", self.last_screen_info)

    def btn8_press(self):
        self.done_return()

    # 姓名 号码 通话状态
    def initialization(self):
        self.call_name.set_text(self.meta_info[0])
        self.call_phone.set_text(self.meta_info[1])
        if self.meta_info[2] == 1:
            self.call_state.set_text("正在呼入")
            self.__speak_state = 1
            self.__dail_state = 1
        else:
            self.__speak_state = 1
            self.__dail_state = 0
            self.call_state.set_text("正在呼出")

        # 开启外放1,关闭0
        EventMesh.publish("call_speaker_out", self.__speak_state)
        call_speaker.set_src(self.SPEAK_STATE.get(self.__speak_state))
        call_answer.set_src(self.DAIL_STATE.get(self.__dail_state))


class HealthQrcodeScreen(Screen):
    NAME = "health_qrcode"

    def __init__(self):
        super().__init__()
        self.meta = health_qrcode
        self.bg_img = health_qrcode2_1

    def power_down_press(self, e):
        pass

    def done_return(self):
        EventMesh.publish("load_screen", self.last_screen_info)

    def done_top_to_bottom(self):
        self.done_return()


class PowerDownScreen(Screen):
    NAME = "power_down"

    def __init__(self):
        super().__init__()
        self.meta = power_down
        self.bg_img = power_down2_1
        power_down_imgbtn_1.add_event_cb(lambda e: self.power_down_press(e),
                                         lv.EVENT.PRESSED, None)
        power_down_imgbtn_2.add_event_cb(lambda e: self.load_screen(e, {"screen": "menu2"}),
                                         lv.EVENT.PRESSED, None)

    def power_down_press(self, e):
        Power.powerDown()

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "menu2"})


class CallLogScreen(Screen):
    NAME = "call_log"

    def __init__(self):
        super().__init__()
        self.meta = call_log
        self.bg_img = call_log_1
        self.call_log_list_1 = call_log_list_1
        self.count = 0
        self.group_list = []
        self._btn_list = []

    def done_left_to_right(self):
        EventMesh.publish("load_screen", {"screen": "addr_book"})

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("push_call_log_list", self.get_call_log_list)

    def get_call_log_list(self, event, msg):
        self.group_list = msg
        self.__content_create()

    def initialization(self):
        self._btn_list = []
        self.group_list = []
        self.group_list = EventMesh.publish("get_call_log_list")
        self.__content_create()

    def __content_create(self):
        if self.count:
            self.call_log_list_1.delete()
        self.call_log_list_1 = lv.list(call_log2)
        self.call_log_list_1.set_pos(10, 54)
        self.call_log_list_1.set_size(225, 156)
        self.call_log_list_1.set_style_pad_left(2, 0)
        self.call_log_list_1.set_style_pad_top(4, 0)
        self.call_log_list_1.set_style_pad_row(3, 0)
        self.call_log_list_1.add_style(style_list, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.call_log_list_1.add_style(style_list_scro, lv.PART.SCROLLBAR | lv.STATE.DEFAULT)
        self._btn_list = []
        for i, each in enumerate(self.group_list):
            _btn = lv.btn(self.call_log_list_1)
            _btn.set_size(220, 45)
            _btn.add_event_cb(lambda e: self.btn_click(e),
                              lv.EVENT.LONG_PRESSED,
                              None)
            _btn.add_style(style_list, lv.PART.MAIN | lv.STATE.DEFAULT)

            _btn_label1 = lv.label(_btn)
            _btn_label1.set_pos(0, 0)
            _btn_label1.set_long_mode(lv.label.LONG.DOT)
            _btn_label1.set_size(0, 0)
            _btn_label1.set_text(str(i))

            _btn_label2 = lv.label(_btn)
            _btn_label2.set_pos(0, 5)
            _btn_label2.set_size(100, 25)
            _btn_label2.set_text(each[0])
            _btn_label2.set_long_mode(lv.label.LONG.DOT)
            _btn_label2.add_style(style_font_regular_18_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)
            #
            _btn_label3 = lv.label(_btn)
            _btn_label3.set_pos(100, 5)
            _btn_label3.set_size(100, 25)
            _btn_label3.set_text("(" + each[1] + ") " + each[2] + " " + each[3])
            _btn_label3.set_long_mode(lv.label.LONG.DOT)
            _btn_label3.add_style(style_font_regular_18_space_0_default, lv.PART.MAIN | lv.STATE.DEFAULT)

            _btn_img = lv.img(_btn)
            _btn_img.set_pos(200, 8)
            _btn_img.set_size(20, 20)
            _btn_img.set_src('U:/static/mp912650106.png')

            self._btn_list.append((_btn, _btn_img, _btn_label1, _btn_label2, _btn_label3))

    def btn_click(self, e):
        l1 = e.get_target().get_child(0).get_text()
        EventMesh.publish("call_user", int(l1))

    def done_return(self):
        EventMesh.publish("load_screen", {"screen": "menu"})


class UI(object):
    def __init__(self, lcd_gpio):
        self.screen = MainScreen()
        self.screen_list = []
        self.lv = lv
        self.main_flag = 0
        self.lcd_gpio = lcd_gpio
        self.__lcd_sleep_timer = osTimer()
        self.__awaiter_timer = osTimer()

    def post_processor_after_instantiation(self):
        EventMesh.subscribe("load_screen", self.load_screen)
        EventMesh.subscribe("btn1_press", self.btn_press)
        EventMesh.subscribe("btn2_press", self.btn_press)
        EventMesh.subscribe("btn3_press", self.btn_press)
        EventMesh.subscribe("btn4_press", self.btn_press)
        EventMesh.subscribe("btn5_press", self.btn_press)
        EventMesh.subscribe("btn6_press", self.btn_press)
        EventMesh.subscribe("btn7_press", self.btn_press)
        EventMesh.subscribe("btn8_press", self.btn_press)
        EventMesh.subscribe("btn8_long_press", self.btn_press)

        EventMesh.subscribe("btn1_release", self.btn_release)
        EventMesh.subscribe("btn2_release", self.btn_release)
        EventMesh.subscribe("btn3_release", self.btn_release)
        EventMesh.subscribe("btn4_release", self.btn_release)
        EventMesh.subscribe("btn5_release", self.btn_release)
        EventMesh.subscribe("btn6_release", self.btn_release)
        EventMesh.subscribe("btn7_release", self.btn_release)

        EventMesh.subscribe("done_left_to_right", self.ui_press)
        EventMesh.subscribe("done_right_to_left", self.ui_press)
        EventMesh.subscribe("done_bottom_to_top", self.ui_press)
        EventMesh.subscribe("done_top_to_bottom", self.ui_press)
        EventMesh.subscribe("done_return", self.ui_press)
        EventMesh.subscribe("done_click", self.ui_press)
        EventMesh.subscribe("done_error", self.ui_press)

        EventMesh.subscribe("call_in", self.publish_call_in)
        EventMesh.subscribe("set_bg_img", self.set_bg_img)

        EventMesh.subscribe("start_lcd_sleep_auto_sleep", self.start_lcd_sleep_auto_sleep)
        for screen in self.screen_list:
            screen.post_processor_after_instantiation()

    def set_bg_img(self, event, msg):
        for sc in self.screen_list:
            sc.set_bg_img(msg)

    def ui_press(self, event, key):
        if not self.__lcd_state():
            return
        self.__awaiter_timer_reset()
        print("ui press {}".format(event))
        if event == "done_left_to_right":
            self.screen.done_left_to_right()
        if event == "done_right_to_left":
            self.screen.done_right_to_left()
        if event == "done_bottom_to_top":
            self.screen.done_bottom_to_top()
        if event == "done_top_to_bottom":
            self.screen.done_top_to_bottom()
        if event == "done_return":
            self.screen.done_return()
        if event == "done_click":
            self.screen.done_click()
            # self.screen.btn6_press()

    def btn_press(self, event, key):
        if not self.__lcd_state():
            if event == "btn8_press":
                self.__lcd_state_manage()
                self.__awaiter_timer_reset()
                return
            else:
                return
        self.__awaiter_timer_reset()
        print("btn_press: {}".format(event))
        if event == "btn1_press":
            self.screen.btn1_press()
        if event == "btn2_press":
            self.screen.btn2_press()
        if event == "btn3_press":
            self.screen.btn3_press()
        if event == "btn4_press":
            self.screen.btn4_press()
        if event == "btn5_press":
            self.screen.btn5_press()
        if event == "btn6_press":
            self.screen.btn6_press()
        if event == "btn7_press":
            self.screen.btn7_press()
        if event == "btn8_press":
            self.screen.btn8_press()
        if event == "btn8_long_press":
            Power.powerDown()

    def btn_release(self, event, msg):
        print("btn_release: {}".format(event))
        if event == "btn1_release":
            self.screen.btn1_release()
        if event == "btn2_release":
            self.screen.btn2_release()
        if event == "btn3_release":
            self.screen.btn3_release()
        if event == "btn4_release":
            self.screen.btn4_release()
        if event == "btn5_release":
            self.screen.btn5_release()
        if event == "btn6_release":
            self.screen.btn6_release()
        if event == "btn7_release":
            self.screen.btn7_release()

    def __lcd_state(self):
        return self.lcd_gpio.read()

    def __lcd_on(self):
        self.lcd_gpio.write(1)
        EventMesh.publish("lower_power", 1)  # 0 进入休眠 1 退出休眠
        self.__lcd_sleep_timer_start()

    def __lcd_off(self):
        self.lcd_gpio.write(0)
        EventMesh.publish("lower_power", 0)  # 0 进入休眠 1 退出休眠
        self.__lcd_sleep_timer_stop()  # 0 关闭息屏定时器 1 开启息屏定时器

    def __lcd_sleep_timer_start(self, event=None, mode=None):
        """开启息屏定时器"""
        lcd_sleep_time = EventMesh.publish("get_lcd_sleep_mode")
        if lcd_sleep_time is None:
            lcd_sleep_time = 15
        self.__lcd_sleep_timer.start(lcd_sleep_time * 1000, 0, self.__auto_lcd_switch)

    def __auto_lcd_switch(self, *args):
        if self.__lcd_state():  # 未息屏状态，熄灭屏幕
            self.__lcd_off()

    def __lcd_sleep_timer_stop(self, event=None, mode=None):
        """息屏"""
        self.__lcd_sleep_timer.stop()

    def __lcd_sleep_timer_restart(self, event=None, mode=None):
        self.__lcd_sleep_timer_stop()
        self.__lcd_sleep_timer_start()

    def __lcd_state_manage(self):
        if self.__lcd_state():
            self.__lcd_sleep_timer_restart()
            return True
        else:
            self.__lcd_on()
            return False

    def start(self):
        self.post_processor_after_instantiation()

    def add_screen(self, screen):
        self.screen_list.append(screen)
        return self

    def __awaiter_timer_start(self):
        self.__awaiter_timer.start(10 * 1000, 0, self.__to_awaiter_screen)
        pass

    def __to_awaiter_screen(self, e):
        if self.screen.NAME == "learn_info":
            self.start_lcd_sleep_auto_sleep(None, None)
        elif self.screen == "call":
            return
        else:
            EventMesh.publish("load_screen", {"screen": "learn_info"})

    def __awaiter_timer_reset(self):
        self.__awaiter_timer_stop()
        self.__awaiter_timer_start()

    def __awaiter_timer_stop(self):
        self.__awaiter_timer.stop()

    def finish(self):
        # self.__lcd_sleep_timer_start()
        self.__awaiter_timer_start()

    def start_lcd_sleep_auto_sleep(self, event, msg):
        if msg:
            self.__lcd_sleep_timer_start()
        else:
            self.__lcd_sleep_timer_stop()
            self.__lcd_state_manage()

    def publish_call_in(self, event, msg):
        EventMesh.publish("load_screen", {"screen": "call", "meta": msg})

    def load_screen(self, topic, msg):
        print("msg={}".format(msg))
        for scr in self.screen_list:
            if scr.NAME == msg["screen"]:
                # 每次屏幕切换开始息屏倒计时
                if scr.NAME != self.screen.NAME and self.screen.NAME not in ["call", ]:
                    scr.last_screen_info = {"screen": self.screen.NAME}
                last_screen = self.screen
                self.screen = scr
                if msg.get("meta"):
                    self.screen.meta_info = msg.get("meta")
                self.screen.post_processor_before_initialization()
                self.screen.initialization()
                self.screen.post_processor_after_initialization()
                self.screen.load()
                self.lv.scr_load(self.screen.get_meta())
                self.__lcd_sleep_timer_stop()
                if self.screen.NAME not in ["call", ]:
                    print("reset ... ")
                    self.__awaiter_timer_reset()
                else:
                    print("stop ....")
                    self.__lcd_on()
                    self.__awaiter_timer_stop()
                    self.__lcd_sleep_timer_stop()
                if last_screen:
                    last_screen.deactivate()
