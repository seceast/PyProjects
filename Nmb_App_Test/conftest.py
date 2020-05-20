# -*- coding: utf-8 -*-
# @author: yangyd
# @file: conftest.py
# @time: 2019/9/19 19:58


import pytest
from appium.webdriver import Remote


@pytest.fixture()
def init_app():
    caps = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "Android Emulator",
        "automationName": "uiautomator2",
        "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",
        "appPackage": "com.lemon.lemonban",
        "noReset": True
    }

    app_driver = Remote(desired_capabilities=caps)
    yield app_driver
    app_driver.quit()

