# -*- coding: utf-8 -*-
# @author: yangyd
# @file: app_sudoku.py
# @time: 2019/9/17 22:25


import time

from appium.webdriver import Remote
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from common.app_operate import AppOperate

caps = {
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "Android Emulator",
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
    "appPackage": "com.xxzb.fenwoo",
    "noReset": "False"
}

android_driver = Remote(desired_capabilities=caps)

android_driver.implicitly_wait(10)

app_action = TouchAction(android_driver)
app_opre = AppOperate(android_driver)

#
# time.sleep(2)
# for i in range(4):
#     app_opre.swipe_left()
#     time.sleep(1)
#
# # 点击立即体检进入首页
# # android_driver.find_element_by_id("com.xxzb.fenwoo:id/btn_start").click()
#
# android_driver.find_element_by_android_uiautomator(
#     'new UiSelector().resourceId("com.xxzb.fenwoo:id/btn_start")').click()
#
# android_driver.find_element_by_android_uiautomator(
#     'new UiSelector().text("我")').click()
#
# # 进入登陆界面
# # android_driver.start_activity("com.xxzb.fenwoo", ".activity.addition.LoginActivity")
# time.sleep(1)
#
# # 输入手机号码
# app_opre.wait_find_element((MobileBy.ID, "com.xxzb.fenwoo:id/et_phone")).send_keys("18684720553")
# time.sleep(0.5)
# # 点击下一步
# app_opre.wait_find_element((MobileBy.ID, "com.xxzb.fenwoo:id/btn_next_step")).click()
# # 输入密码
# app_opre.wait_find_element((MobileBy.ID, "com.xxzb.fenwoo:id/et_pwd")).send_keys("python")
# # 点击确定
# app_opre.wait_find_element((MobileBy.ID, "com.xxzb.fenwoo:id/btn_next_step")).click()
#
# # 马上设置按钮"com.xxzb.fenwoo:id/btn_confirm"
# app_opre.wait_find_element((MobileBy.ID, "com.xxzb.fenwoo:id/btn_confirm")).click()
#
# # 创建手势按钮"com.xxzb.fenwoo:id/btn_gesturepwd_guide"
# app_opre.wait_find_element((MobileBy.ID, "com.xxzb.fenwoo:id/btn_gesturepwd_guide")).click()
# # 确定按钮"com.xxzb.fenwoo:id/right_btn"
# time.sleep(0.5)
# app_opre.wait_find_element((MobileBy.ID, "com.xxzb.fenwoo:id/right_btn")).click()
# 图案绘制区"com.xxzb.fenwoo:id/gesturepwd_create_lockview"
"""
九宫格思路：
1、先获取绘制区的元素区域
2、根据判断对区域坐标进行划分，常用都是长宽都6等分
3、根据坐标切割，获取九个点的位置
4、根据点数连线绘制
"""
# draw_el = android_driver.find_element_by_id("com.xxzb.fenwoo:id/gesturepwd_create_lockview")

# 进入绘制界面
android_driver.start_activity("com.xxzb.fenwoo", ".activity.user.CreateGesturePwdActivity")

# app_opre.wait_find_element((MobileBy.ID, "com.xxzb.fenwoo:id/right_btn")).click()

draw_el = app_opre.wait_visibility_element((MobileBy.ID, "com.xxzb.fenwoo:id/gesturepwd_create_lockview"))
# # rect能同时回获取元素的x、y、width、height，并以字典存储
# start_x = draw_el.rect['x']
# start_y = draw_el.rect['y']
# width = draw_el.rect['width']
# height = draw_el.rect['height']
#
# # 设置点的坐标位置
# point1 = {'x': start_x + width * 1 / 6, 'y': start_y + height * 1 / 6}
# point2 = {'x': start_x + width * 3 / 6, 'y': start_y + height * 1 / 6}
# point3 = {'x': start_x + width * 5 / 6, 'y': start_y + height * 1 / 6}
# point4 = {'x': start_x + width * 1 / 6, 'y': start_y + height * 3 / 6}
# point5 = {'x': start_x + width * 3 / 6, 'y': start_y + height * 3 / 6}
# point6 = {'x': start_x + width * 5 / 6, 'y': start_y + height * 3 / 6}
# point7 = {'x': start_x + width * 1 / 6, 'y': start_y + height * 5 / 6}
# point8 = {'x': start_x + width * 3 / 6, 'y': start_y + height * 5 / 6}
# point9 = {'x': start_x + width * 5 / 6, 'y': start_y + height * 5 / 6}
#
# app_action.press(**point1).wait(200).move_to(**point2).wait(200).move_to(
#     **point3).wait(200).move_to(**point6).release().perform()


app_opre.sudoku(draw_el, [1, 2, 3, 6])

time.sleep(2)
# 继续按钮"com.xxzb.fenwoo:id/right_btn"
app_opre.wait_visibility_element((MobileBy.ID, "com.xxzb.fenwoo:id/right_btn")).click()
time.sleep(1)

app_opre.app_quit()
