"""
-*- coding: utf-8 -*-
@author: yangyd
@file: private_page.py
@time: 2019/9/30 0030 11:42
"""


import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators.private_locator import PrivateLocator


class PrivatePage(BasePage):
