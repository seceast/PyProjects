# -*- coding: utf-8 -*-
# @author: yangyd
# @file: home_nmb.py
# @time: 2019/9/24 22:37


from appium.webdriver.common.mobileby import MobileBy

from common.app_operate import AppOperate


class HomeNmb:
    home_btn_locator = (MobileBy.ID, "com.lemon.lemonban:id/navigation_home")
    tiku_btn_locator = (MobileBy.ID, "com.lemon.lemonban:id/navigation_tiku")
    my_nm_locator = (MobileBy.ID, "com.lemon.lemonban:id/navigation_my")

    def __init__(self, driver):
        self.driver = driver
        self.do_app = AppOperate(self.driver)

    @property
    def my_nmb_btn(self):
        return self.do_app.wait_visibility_element(self.my_nm_locator)

    @property
    def tiku_btn(self):
        return self.do_app.wait_visibility_element(self.tiku_btn_locator)

    @property
    def home_btn(self):
        return self.do_app.wait_visibility_element(self.home_btn_locator)

