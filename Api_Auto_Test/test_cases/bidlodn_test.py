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

bidloan_data = DoExcel(project_path.CASE_FILE_PATH, 'bidLoan').read_excel(2)

# login_success = DoExcel(project_path.CASE_FILE_PATH, 'loginsuccess').read_excel(4, end_row=4)

succeed = DoConfig(project_path.CONFIG_FILE_PATH).read_info('test_result', 'succeed')
failed = DoConfig(project_path.CONFIG_FILE_PATH).read_info('test_result', 'failed')


@ddt
class TestBidlodn(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = HttpRequest()
        cls.session_request = cls.request.request_session
        cls.do_mysql = OperateMysql()

    @classmethod
    def tearDownClass(cls):
        cls.do_mysql.mysql_close()

    @data(*bidloan_data)
    def test_bidloan(self, bidloan):
        print("测试的用例是：{}".format(bidloan['description']))

        # login_data = eval(Parameter.lodn_parameter(login_success[0]['param']))
        # self.session_request.request(login_success[0]['method'], login_success[0]['url'],
        #                              login_data)

        loan_param = eval(Parameter.loan_parameter(bidloan['param']))
        # self.session_request.request(bidloan['method'], bidloan['url'],bidloan)

        print("测试的数据是：{}".format(loan_param))
        res = self.session_request.request(bidloan['method'], bidloan['url'], loan_param)

        # 获取成功加标的id
        if "加标成功" in res.text:
            check_sql = bidloan['seek_sql']
            if check_sql:
                check_sql = Parameter.loan_parameter(check_sql)
                check_data = self.do_mysql.run_sql(check_sql, site=1)
                loan_id = check_data['Id']  # 取出加标ID
                print(loan_id)
                # 动态创建属性
                setattr(Parameter, "loan_id", loan_id)

        test_result = None
        write_res = DoExcel(project_path.CASE_FILE_PATH, 'bidLoan')

        try:
            # self.assertEqual(str(res.json()['code']), str(bidloan['except_code']))
            self.assertIn(str(bidloan['except_code']), res.text)
            my_logger.info(res.text)
            test_result = succeed
        except AssertionError as e:
            my_logger.error(e)
            test_result = failed
            raise e
        finally:
            print("测试结果是：", res.text)
            write_res.write_result(bidloan['id'] + 1, res.json()['code'], test_result)
