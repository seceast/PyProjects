#!/user/bin/env python
# -*- coding: utf-8 -*-
# __author__ = yangyd 
# Create time: 2019/7/8 0008 14:34


import unittest
from libs.ddt import ddt, data
from common_code.operate_http_requests import HttpRequest
from common_code import project_path
from common_code.operate_config import DoConfig
from common_code.operate_log import my_logger
from common_code.operate_excel import DoExcel
from common_code.parameterization import Parameter

register_data = DoExcel(project_path.CASE_FILE_PATH, 'register').read_excel(2)

login_success = DoExcel(project_path.CASE_FILE_PATH, 'loginsuccess').read_excel(2)

succeed = DoConfig(project_path.CONFIG_FILE_PATH).read_info('test_result', 'succeed')
failed = DoConfig(project_path.CONFIG_FILE_PATH).read_info('test_result', 'failed')


@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = HttpRequest()
        cls.session_request = cls.request.request_session

    @data(*register_data)
    def test_register(self, register):
        print("测试的用例是：{}".format(register['description']))

        param = Parameter.register_parameter(register['param'])

        print("测试的数据是：{}".format(param))

        res = self.request.http_request(register['url'], register['method'], datas=param)
        test_result = None

        write_res = DoExcel(project_path.CASE_FILE_PATH, 'register')

        try:
            # self.assertEqual(str(res.json()['code']), str(register['except_code']))
            self.assertIn(str(register['except_code']), res.text)
            my_logger.info(res.text)
            test_result = succeed
        except AssertionError as e:
            my_logger.error(e)
            test_result = failed
            raise e
        finally:
            print("测试结果是：", res.text)
            write_res.write_result(register['id'] + 1, res.json()['code'], test_result)
