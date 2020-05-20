# -*- coding: utf-8 -*-
# @author: yangyd
# @file: bid_page.py
# @time: 2019/8/30 11:46
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators.bid_locator import BidLocator


class BidPage(BasePage):
    bid_locator = BidLocator()

    @property
    def bid_select_click(self):
        return self.wait_presence_elements(self.bid_locator.bid_locator)

    @property
    def bid_input(self) -> WebElement:
        return self.wait_presence_element(self.bid_locator.bid_input_locator)

    def bid_success(self, money):
        elem = self.bid_input
        elem.send_keys(money)
        after_money = elem.get_attribute('data-amount')
        self.bid_btn_click.click()
        return after_money

    @property
    def bid_btn_click(self) -> WebElement:
        return self.wait_presence_element(self.bid_locator.bid_btn_locator)

    def get_success_msg(self):
        return self.wait_presence_element(self.bid_locator.bid_success_locator)

    @property
    def activate_btn(self) -> WebElement:
        return self.wait_click_element(self.bid_locator.activate_btn_locator)
