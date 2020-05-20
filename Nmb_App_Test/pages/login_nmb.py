# -*- coding: utf-8 -*-
# @author: yangyd
# @file: login_nmb.py
# @time: 2019/9/24 22:05
import time

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy

from common.app_driver import app_driver_nmb
from pages.home_nmb import HomeNmb


class LoginNmb(HomeNmb):
    login_page_locator = (MobileBy.ID, "com.lemon.lemonban:id/fragment_my_lemon_avatar_title")
    mobile_locator = (MobileBy.ID, "com.lemon.lemonban:id/et_mobile")
    pwd_locator = (MobileBy.ID, "com.lemon.lemonban:id/et_password")
    login_btn_locator = (MobileBy.ID, "com.lemon.lemonban:id/btn_login")

    @property
    def login_page_btn(self) -> WebElement:
        return self.do_app.wait_visibility_element(self.login_page_locator)

    @property
    def mobile_input(self) -> WebElement:
        return self.do_app.wait_visibility_element(self.mobile_locator)

    @property
    def pwd_input(self) -> WebElement:
        return self.do_app.wait_visibility_element(self.pwd_locator)

    @property
    def login_btn(self) -> WebElement:
        return self.do_app.wait_presence_element(self.login_btn_locator)

    def login_nmb(self, phone_num, pwd):
        self.my_nmb_btn.click()
        self.login_page_btn.click()
        time.sleep(0.5)
        self.mobile_input.send_keys(phone_num)
        self.pwd_input.send_keys(pwd)
        self.login_btn.click()

    def get_error_msg(self, text):
        return self.do_app.locate_toast(text)


if __name__ == "__main__":
    log_p = LoginNmb(app_driver_nmb())
    log_p.login_nmb("11", "")
    print(log_p.do_app.locate_toast("手机号码或密码不能为空"))
