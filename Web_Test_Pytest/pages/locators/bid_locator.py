# -*- coding: utf-8 -*-
# @author: yangyd
# @file: bid_locator.py
# @time: 2019/8/30 11:47


from selenium.webdriver.common.by import By


class BidLocator:

    bid_locator = (By.XPATH, "//a[@class = 'btn btn-special']")
    bid_input_locator = (By.XPATH,
                         "//div[@class='clearfix left']//input")
    # bid_btn_locator = (By.XPATH, "//button[@class='btn btn-special height_style']")
    bid_btn_locator = (By.CSS_SELECTOR, ".btn-special")
    bid_success_locator = (By.XPATH, "//div[text()='投标成功！']")
    activate_btn_locator = (By.XPATH,
                            "//div[@class='layui-layer-content']//button")


