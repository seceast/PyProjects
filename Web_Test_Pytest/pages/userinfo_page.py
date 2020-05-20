# -*- coding: utf-8 -*-
# @author: yangyd
# @file: userinfo_page.py
# @time: 2019/8/30 14:18
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators.userinfo_locator import UserInfoLocator


class UserInfoPage(BasePage):
    user_locator = UserInfoLocator()

    @property
    def get_balance(self) -> WebElement:
        return self.wait_presence_element(self.user_locator.user_balance_locator)
