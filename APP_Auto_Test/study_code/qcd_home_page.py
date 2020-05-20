# -*- coding: utf-8 -*-
# @author: yangyd
# @file: qcd_home_page.py
# @time: 2019/9/11 21:57


import time
from appium.webdriver import Remote
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

do_app = AppOperate(android_driver)

# 获取手机的尺寸
# phone_size = android_driver.get_window_size()

# 等待启动
time.sleep(2)
for i in range(4):
    do_app.swipe_left()
    time.sleep(1)

# 点击立即体检进入首页
# android_driver.find_element_by_id("com.xxzb.fenwoo:id/btn_start").click()

android_driver.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("com.xxzb.fenwoo:id/btn_start")').click()

android_driver.find_element_by_android_uiautomator(
    'new UiSelector().text("项目")').click()
# 进入登陆界面
# android_driver.start_activity("com.xxzb.fenwoo", ".activity.addition.LoginActivity")
time.sleep(1)
do_app.get_screenshot(r'test.png')
time.sleep(1)

do_app.app_quit()
