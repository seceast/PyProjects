# -*- coding: utf-8 -*-
# @author: yangyd
# @file: base_page.py
# @time: 2019/8/30 10:01 


from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    phone_locator = (By.NAME, "phone")
    pwd_locator = (By.NAME, "password")

    def __init__(self, driver):
        self.driver = driver
        self.driver_wait = WebDriverWait(self.driver, 30)

    def wait_presence_element(self, locator):
        return self.driver_wait.until(EC.presence_of_element_located(locator))

    def wait_presence_elements(self, locator):
        return self.driver_wait.until(EC.presence_of_all_elements_located(locator))

    def wait_click_element(self, locator):
        return self.driver_wait.until(EC.element_to_be_clickable(locator))

    def wait_invisibility_element(self, locator):
        return self.driver_wait.until(EC.invisibility_of_element_located(locator))

    def get_screenshot(self, filename):
        return self.driver.get_screenshot_as_file(filename)

    def close_page(self):
        self.driver.close()

    def close_chrome(self):
        self.driver.quit()

    def refresh_page(self):
        self.driver.refresh()

    @property
    def user_elem(self) -> WebElement:
        return self.wait_presence_element(self.phone_locator)

    @property
    def pwd_elem(self) -> WebElement:
        return self.wait_presence_element(self.pwd_locator)

