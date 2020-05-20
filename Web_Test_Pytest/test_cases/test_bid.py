# -*- coding: utf-8 -*-
# @author: yangyd
# @file: test_bid.py
# @time: 2019/8/30 14:49 


import time
import pytest

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from decimal import Decimal
from datas.bid_data import bid_right_data, bid_error_data, bid_error_data_10


@pytest.mark.bid
class TestBid:

    @pytest.mark.parametrize("error_data", bid_error_data)
    def test_error_bid(self, error_data, init_web_bid):
        driver, user_page, bid_page = init_web_bid
        try:
            bid_page.bid_select_click[1].click()
            bid_page.bid_input.send_keys(error_data['money'])

            assert (error_data['expect'], bid_page.bid_btn_click.text)
        except (TimeoutException, NoSuchElementException) as e:
            raise e

    @pytest.mark.parametrize("error_data", bid_error_data_10)
    def test_error_bid_10(self, error_data, init_web_bid):
        driver, user_page, bid_page = init_web_bid
        try:
            bid_page.bid_select_click[1].click()
            bid_page.bid_input.send_keys(error_data['money'])

            assert (error_data['expect'], bid_page.bid_btn_click.text)
        except (TimeoutException, NoSuchElementException) as e:
            raise e

    @pytest.mark.parametrize("bid_data", bid_right_data)
    def test_success_bid(self, bid_data, init_web_bid):
        driver, user_page, bid_page = init_web_bid
        try:
            bid_page.bid_select_click[1].click()

            before_money = bid_page.bid_success(bid_data['money'])
            assert (bid_data['expect'], bid_page.get_success_msg().text)

            time.sleep(3)
            bid_page.activate_btn.click()
            balance = user_page.get_balance.text
            assert (Decimal(str(balance[:-1])) + Decimal(str(bid_data['money'])) == Decimal(str(before_money)))

        except (TimeoutException, NoSuchElementException) as e:
            raise e


if __name__ == '__main__':
    pytest.main()
