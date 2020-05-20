#!/user/bin/env python
# -*- coding: utf-8 -*-
# __author__ = yangyd 
# Create time: 2019/7/16 0016 15:09


import unittest
from libs.ddt import ddt, data
from common_code.operate_http_requests import HttpRequest
from common_code import project_path
from common_code.operate_config import DoConfig
from common_code.operate_log import my_logger
from common_code.operate_excel import DoExcel
from common_code.parameterization import Parameter

add_data = DoExcel(project_path.CASE_FILE_PATH, 'add').read_excel(2)

login_success = DoExcel(project_path.CASE_FILE_PATH, 'loginsuccess').read_excel(3, end_row=3)

succeed = DoConfig(project_path.CONFIG_FILE_PATH).read_info('test_result', 'succeed')
failed = DoConfig(project_path.CONFIG_FILE_PATH).read_info('test_result', 'failed')


@ddt
class TestAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = HttpRequest()
        cls.session_request = cls.request.request_session

    @data(*add_data)
    def test_add(self, add):
        print("测试的用例是：{}".format(add['description']))
        login_data = Parameter.add_parameter(login_success[0]['param'])
        self.session_request.request(login_success[0]['method'], login_success[0]['url'],
                                     eval(login_data))

        add_param = eval(Parameter.add_parameter(add['param']))
        print("测试的数据是：{}".format(add_param))

        res = self.session_request.request(add['method'], add['url'], data=add_param)

        test_result = None
        write_res = DoExcel(project_path.CASE_FILE_PATH, 'add')

        try:
            # self.assertEqual(str(res.json()['code']), str(add['except_code']))
            self.assertIn(str(add['except_code']), res.text)
            my_logger.info(res.text)
            test_result = succeed
        except AssertionError as e:
            my_logger.error(e)
            test_result = failed
            raise e
        finally:
            print("测试结果是：", res.text)
            write_res.write_result(add['id'] + 1, res.json()['code'], test_result)
