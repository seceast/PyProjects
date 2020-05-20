'''
@Author: yangyd
@Date: 2019-09-23 10:09:32
@LastEditors: yangyd
@LastEditTime: 2019-09-23 10:09:32
'''
# -*- coding: utf-8 -*-
# @author: yangyd
# @file: test_login.py
# @time: 2019/8/29 15:39 


import time
import pytest

from datas.login_data import login_error_data, login_success_data
from selenium.common.exceptions import TimeoutException, NoSuchElementException


@pytest.mark.login  # 类打标签的方法1
class TestLogin:
    # 固定用法  类打标签的方法2 可以打多个
    # pytestmark = [pytest.mark.login, pytest.mark.other]

    @pytest.mark.error
    @pytest.mark.parametrize('login_data', login_error_data)
    def test_error_login(self, login_data, init_web_login):
        driver, login_page = init_web_login
        try:
            login_page.login(login_data['phone'], login_data['pwd'])
            error_msg_element = login_page.get_actual_error_result()
            assert login_data['expect'], error_msg_element.text
        except (TimeoutException, NoSuchElementException) as e:
            raise e

    @pytest.mark.success
    @pytest.mark.parametrize('login_data', login_success_data)
    def test_success_login(self, login_data, init_web_login):
        driver, login_page = init_web_login
        try:
            login_page.login(login_data['phone'], login_data['pwd'])
            time.sleep(1)
            success_msg_element = login_page.get_actual_success_result()
            assert login_data['expect'], success_msg_element.text
        except (TimeoutException, NoSuchElementException) as e:
            raise e


if __name__ == '__main__':
    pytest.main(['-m login and success'])

