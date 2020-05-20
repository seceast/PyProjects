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
from common_code.operate_mysql import OperateMysql

recharge_data = DoExcel(project_path.CASE_FILE_PATH, 'recharge').read_excel(2)
login_success = DoExcel(project_path.CASE_FILE_PATH, 'loginsuccess').read_excel(2, end_row=2)

succeed = DoConfig(project_path.CONFIG_FILE_PATH).read_info('test_result', 'succeed')
failed = DoConfig(project_path.CONFIG_FILE_PATH).read_info('test_result', 'failed')


@ddt
class TestRecharge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = HttpRequest()
        cls.session_request = cls.request.request_session
        cls.check_sql = OperateMysql()

    @classmethod
    def tearDownClass(cls):
        cls.check_sql.mysql_close()

    @data(*recharge_data)
    def test_recharge(self, recharge):
        # 在测试报告中显示测试用例名称
        print("测试的用例是：{}".format(recharge['description']))
        login_data = eval(Parameter.recharge_parameter(login_success[0]['param']))
        self.session_request.request(login_success[0]['method'], login_success[0]['url'],
                                     login_data)

        param = eval(Parameter.recharge_parameter(recharge['param']))
        print("测试的数据是：{}".format(param))

        # 查询数据库余额数据进行数据校验
        seek_sql = recharge['seek_sql']

        if seek_sql:
            seek_sql = Parameter.recharge_parameter(seek_sql)
            before_seek_res = self.check_sql.run_sql(seek_sql, site=1)
            # seek_res = json.loads(seek_res)
            # 将返回数据进行数据转换，数据库查询出数据为decimal.Decimal类型，并保留两位小数
            before_amount = round(float(before_seek_res['LeaveAmount']), 2)

        # 调用充值接口
        res = self.session_request.request(recharge['method'], recharge['url'], data=param)

        test_result = None
        write_res = DoExcel(project_path.CASE_FILE_PATH, 'recharge')

        try:
            # self.assertEqual(str(res.json()['code']), str(recharge['except_code']))
            self.assertIn(str(recharge['except_code']), res.text)
            if seek_sql:
                # 前一个sql已经完成参数化
                # seek_sql = Parameter.recharge_parameter(seek_sql)
                after_seek_res = self.check_sql.run_sql(seek_sql, site=1)
                after_amount = round(float(after_seek_res['LeaveAmount']), 2)

                # 判断充值前后账户金额的变化是否正确
                self.assertEqual(after_amount, before_amount + param['amount'])

            my_logger.info(res.text)
            test_result = succeed
        except AssertionError as e:
            my_logger.error(e)
            test_result = failed
            raise e
        finally:
            print("测试结果是：", res.text)
            write_res.write_result(recharge['id'] + 1, res.json()['code'], test_result)
