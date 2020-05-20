#!/user/bin/env python
# -*- coding: utf-8 -*-
# __author__ = yangyd 
# Create time: 2019/7/16 0016 15:08


import unittest
from libs.ddt import ddt, data
from common_code.operate_http_requests import HttpRequest
from common_code import project_path
from common_code.operate_config import DoConfig
from common_code.operate_log import my_logger
from common_code.operate_excel import DoExcel
from common_code.parameterization import Parameter

login_data = DoExcel(project_path.CASE_FILE_PATH, 'login').read_excel(2)

succeed = DoConfig(project_path.CONFIG_FILE_PATH).read_info('test_result', 'succeed')
failed = DoConfig(project_path.CONFIG_FILE_PATH).read_info('test_result', 'failed')


@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.request = HttpRequest()
        cls.session_request = cls.request.request_session

    @data(*login_data)
    def test_login(self, login):
        print("测试的用例是：{}".format(login['description']))
        param = Parameter.register_parameter(login['param'])

        print("测试的数据是：{}".format(param))

        res = self.request.http_request(login['url'], login['method'], param)
        test_result = None

        write_res = DoExcel(project_path.CASE_FILE_PATH, 'login')

        try:
            # self.assertEqual(str(res.json()['code']), str(login['except_code']))
            self.assertIn(str(login['except_code']), res.text)
            my_logger.info(res.text)
            test_result = succeed
        except AssertionError as e:
            my_logger.error(e)
            test_result = failed
            raise e
        finally:
            print("测试结果是：", res.text)
            write_res.write_result(login['id'] + 1, res.json()['code'], test_result)
