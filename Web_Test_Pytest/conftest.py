# -*- coding: utf-8 -*-
# @author: yangyd
# @file: conftest.py
# @time: 2019/9/3 17:15
import pytest
from selenium import webdriver

from pages.bid_page import BidPage
from pages.login_page import LoginPage
from pages.userinfo_page import UserInfoPage


@pytest.fixture(scope="class")
def init_web_bid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    login_page = LoginPage(driver)
    login_page.login(18684720553, 'python')
    user_page = UserInfoPage(driver)
    bid_page = BidPage(driver)

    yield driver, user_page, bid_page

    driver.quit()


@pytest.fixture(scope="class")
def init_web_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    login_page = LoginPage(driver)

    yield driver, login_page

    driver.quit()
