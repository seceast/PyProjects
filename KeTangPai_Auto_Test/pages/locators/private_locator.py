"""
-*- coding: utf-8 -*-
@author: yangyd
@file: private_locator.py
@time: 2019/9/30 11:35
"""

from selenium.webdriver.common.by import By


class PrivateLocator:
    login_page_btn = (By.CLASS_NAME, "login")
    search_locator = (By.XPATH, "//input[@type='text']")
