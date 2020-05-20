# -*- coding: utf-8 -*-
# @author: yangyd
# @file: login_locator.py
# @time: 2019/8/30 10:06


from selenium.webdriver.common.by import By


class LoginLocator:
    phone_locator = (By.NAME, "phone")
    pwd_locator = (By.NAME, "password")
    login_btn_locator = (By.XPATH, "//button[@class='btn btn-special']")
    error_msg_locator = (By.XPATH, '//div[@class="form-error-info"]')
    login_success_locator = (By.XPATH, "//a[text()='退出']")
    unauthorized_locator = (By.XPATH, "//div[@class = 'layui-layer-content']")
