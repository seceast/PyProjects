# -*- coding: utf-8 -*-
# @author: yangyd
# @file: conftest.py
# @time: 2019/9/3 17:15
import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.task_page import TaskPage


@pytest.fixture(scope="class")
def init_web_task():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    login_page = LoginPage(driver)
    login_page.login(19915986907, 'yyd19915986907')
    task_page = TaskPage(driver)

    yield driver, task_page

    driver.quit()


@pytest.fixture(scope="class")
def init_web_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    login_page = LoginPage(driver)

    yield driver, login_page

    driver.quit()
