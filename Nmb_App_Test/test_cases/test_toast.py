# -*- coding: utf-8 -*-
# @author: yangyd
# @file: test_toast.py
# @time: 2019/9/19 19:12


import pytest

from common.operate_log import my_logger
from datas.nmb_login_data import login_error_data
from pages.login_nmb import LoginNmb
from selenium.common.exceptions import TimeoutException, NoSuchElementException


@pytest.mark.login
class TestToast:

    @pytest.mark.error
    @pytest.mark.parametrize("login_data", login_error_data)
    def test_error_login(self, login_data, init_app):
        driver = init_app
        try:
            login = LoginNmb(driver)
            login.login_nmb(login_data["phone"], login_data["pwd"])
            res_msg = login.get_error_msg(login_data["expect"])
            assert login_data["expect"], res_msg.text
            my_logger.info(res_msg.text)
        except (TimeoutException, NoSuchElementException) as e:
            my_logger.debug(e)
            raise e


if __name__ == "__main__":
    pytest.main(['-m login', '-s'])
