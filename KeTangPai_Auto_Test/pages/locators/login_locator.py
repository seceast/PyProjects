# -*- coding: utf-8 -*-
# @author: yangyd
# @file: login_locator.py
# @time: 2019/8/30 10:06


from selenium.webdriver.common.by import By


class LoginLocator:
    login_page_btn = (By.CLASS_NAME, "login")
    account_locator = (By.NAME, "account")
    pwd_locator = (By.XPATH, "//input[@name='pass']")
    login_btn_locator = (By.XPATH,
                         "//div[@class='padding-cont pt-login']//a[@class='btn-btn']")

    error_msg_locator = (By.CLASS_NAME, "error-tips")

    login_success_locator = (By.XPATH, "//div[@class='ktcon1l fr']")
    py_19_locator = (By.XPATH, "//a[@class='jumptoclass']")
