# -*- coding: utf-8 -*-
# @author: yangyd
# @file: userinfo_locator.py
# @time: 2019/8/30 14:20


from selenium.webdriver.common.by import By


class UserInfoLocator:
    user_balance_locator = (By.XPATH, "//li[@class='color_sub']")
