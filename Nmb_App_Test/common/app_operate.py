# -*- coding: utf-8 -*-
# @author: yangyd
# @file: app_operate.py
# @time: 2019/9/12 22:06


from appium.webdriver import Remote
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.app_keycode import KeyCode


class AppOperate:

    def __init__(self, driver: Remote):
        self.driver = driver

    def wait_visibility_element(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

    def wait_presence_element(self, locator):
        return WebDriverWait(self.driver, 20, poll_frequency=0.1).until(EC.presence_of_element_located(locator))

    def wait_click(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    def find_uiautomator(self, UiSelector):
        self.driver.find_element_by_android_uiautomator(UiSelector)

    def get_phone_size(self):
        phone_size = self.driver.get_window_size()
        return phone_size

    @property
    def get_phone_width(self):
        return self.get_phone_size().get('width')

    @property
    def get_phone_height(self):
        return self.get_phone_size().get('height')

    def swipe_left(self, duration=200):
        self.driver.swipe(self.get_phone_width * 0.9, self.get_phone_height * 0.5,
                          self.get_phone_width * 0.1, self.get_phone_height * 0.5, duration=duration)

    def swipe_right(self, duration=200):
        self.driver.swipe(self.get_phone_width * 0.1, self.get_phone_height * 0.5,
                          self.get_phone_width * 0.9, self.get_phone_height * 0.5, duration=duration)

    def swipe_up(self, duration=200):
        self.driver.swipe(self.get_phone_width * 0.5, self.get_phone_height * 0.9,
                          self.get_phone_width * 0.5, self.get_phone_height * 0.1, duration=duration)

    def swipe_down(self, duration=200):
        self.driver.swipe(self.get_phone_width * 0.5, self.get_phone_height * 0.1,
                          self.get_phone_width * 0.5, self.get_phone_height * 0.9, duration=duration)

    def get_screenshot(self, filepath):
        self.driver.get_screenshot_as_file(filepath)

    def volume_up(self):
        """音量加"""
        return self.driver.press_keycode(KeyCode.VOLUME_UP)

    def volume_down(self):
        """音量减"""
        return self.driver.press_keycode(KeyCode.VOLUME_DOWN)

    def enter(self):
        return self.driver.press_keycode(KeyCode.ENTER)

    def app_quit(self):
        self.driver.quit()

    def sudoku(self, draw_el, points: list, duration=200):
        """
        绘制九宫格
        :param duration: 滑动事件
        :param draw_el: 九宫格的绘制区域的元素
        :param points: 绘制的点列表的形式传入
        :return: None
        """
        app_action = TouchAction(self.driver)
        # rect能同时回获取元素的x、y、width、height，并以字典存储
        start_x = draw_el.rect['x']
        start_y = draw_el.rect['y']
        width = draw_el.rect['width']
        height = draw_el.rect['height']
        # 设置点的坐标位置
        static_point = [
            {'x': start_x + width * 1 / 6, 'y': start_y + height * 1 / 6},
            {'x': start_x + width * 3 / 6, 'y': start_y + height * 1 / 6},
            {'x': start_x + width * 5 / 6, 'y': start_y + height * 1 / 6},
            {'x': start_x + width * 1 / 6, 'y': start_y + height * 3 / 6},
            {'x': start_x + width * 3 / 6, 'y': start_y + height * 3 / 6},
            {'x': start_x + width * 5 / 6, 'y': start_y + height * 3 / 6},
            {'x': start_x + width * 1 / 6, 'y': start_y + height * 5 / 6},
            {'x': start_x + width * 3 / 6, 'y': start_y + height * 5 / 6},
            {'x': start_x + width * 5 / 6, 'y': start_y + height * 5 / 6}
        ]
        app_action.press(**static_point[points[0] - 1]).wait(duration)
        for p in points[1:]:
            app_action.move_to(**static_point[p - 1]).wait(duration)
        app_action.release().perform()

    def switch_to_webviem(self, ctx_name=None):
        """ctx_name,需要写换的web页面名"""
        if ctx_name is None:
            return self.driver.switch_to.context("NATIVE_APP")
        else:
            return self.driver.switch_to.context(ctx_name)

    def locate_toast(self, toast_text):
        """toast弹窗提示定位"""
        return self.wait_presence_element((MobileBy.XPATH, f"//*[contains(@text,'{toast_text}')]"))

    def app_press(self, x, y):
        action = TouchAction(self.driver)
        return action.press(x, y).perform()

    def app_move_to(self, x, y):
        action = TouchAction(self.driver)
        return action.move_to(x, y).perform()
