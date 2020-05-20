# -*- coding: utf-8 -*-
# @author: yangyd
# @file: login_page.py
# @time: 2019/8/27 15:20


import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators.login_locator import LoginLocator


class LoginPage(BasePage):
    login_url = 'http://120.78.128.25:8765/Index/login.html'
    login_locator = LoginLocator()

    def get_actual_error_result(self):
        error_msg_element = self.wait_presence_element(
            self.login_locator.error_msg_locator)
        return error_msg_element

    def get_actual_success_result(self):
        success_msg_element = self.wait_presence_element(
            self.login_locator.login_success_locator)
        return success_msg_element

    def login(self, username, pwd):
        self.driver.get(self.login_url)

        self.user_elem.send_keys(username)

        self.pwd_elem.send_keys(pwd)

        login_btn = self.wait_click_element(self.login_locator.login_btn_locator)
        login_btn.click()

        time.sleep(1)
        # self.refresh_page()

    @property
    def get_unauthorized_msg(self) -> WebElement:
        return self.wait_presence_element(self.login_locator.unauthorized_locator)


if __name__ == '__main__':
    test_driver = webdriver.Chrome()
    login_driver = LoginPage(test_driver)
    login_driver.login('11', '22')
    login_driver.get_screenshot('test.png')
    time.sleep(0.5)
    login_driver.close_chrome()
