# -*- coding: utf-8 -*-
# @author: yangyd
# @file: app_driver.py
# @time: 2019/9/9 20:29
import time

from appium.webdriver import Remote

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

# 获取手机的尺寸
phone_size = android_driver.get_window_size()

# 等待启动
time.sleep(2)
for i in range(4):
    android_driver.swipe(phone_size['width'] * 0.9, phone_size['width'] * 0.5,
                         phone_size['width'] * 0.1, phone_size['width'] * 0.5)
    time.sleep(1)

# 点击立即体检进入首页
# android_driver.find_element_by_id("com.xxzb.fenwoo:id/btn_start").click()
android_driver.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("com.xxzb.fenwoo:id/btn_start")').click()
time.sleep(2)

android_driver.quit()
