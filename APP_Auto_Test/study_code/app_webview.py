# -*- coding: utf-8 -*-
# @author: yangyd
# @file: app_webview.py
# @time: 2019/9/17 23:50


import time

from appium.webdriver import Remote

from study_code.app_keycode import KeyCode

caps = {
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "Android Emulator",
    "appActivity": ".BrowserActivity",
    "appPackage": "com.android.browser",
    "noReset": "False"
}

android_driver = Remote(desired_capabilities=caps)

android_driver.implicitly_wait(10)

# 浏览器中输入网址并点击回车
address_input_e = android_driver.find_element_by_id('com.android.browser:id/url')
address_input_e.send_keys('www.baidu.com')
android_driver.press_keycode(KeyCode.ENTER)
# 获取上下文环境，并进行切换app和H5环境
contexts = android_driver.contexts
for ctx in contexts:
    if "WEBVIEW" in ctx:
        android_driver.switch_to.context(ctx)
time.sleep(0.5)
input_e = android_driver.find_element_by_id('index-kw')
input_e.send_keys('柠檬班')
android_driver.find_element_by_id('index-bn').click()

time.sleep(1)
android_driver.quit()
