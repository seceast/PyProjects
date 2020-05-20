# -*- coding: utf-8 -*-
# @author: yangyd
# @file: app_driver.py
# @time: 2019/9/9 20:29
import time

from appium.webdriver import Remote


def app_driver_qcd():
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

    return android_driver


def app_driver_nmb():
    caps = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "Android Emulator",
        "automationName": "UIAutomator2",
        "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",
        "appPackage": "com.lemon.lemonban",
        "noReset": "False"
    }

    android_driver = Remote(desired_capabilities=caps)

    android_driver.implicitly_wait(10)

    return android_driver
