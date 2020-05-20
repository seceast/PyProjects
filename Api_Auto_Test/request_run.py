#!/user/bin/env python
# -*- coding: utf-8 -*-
# __author__ = yangyd 
# Create time: 2019/7/10 0010 11:19


import unittest
import os
from common_code.operate_config import DoConfig
# from test_cases import register_test
# from test_cases import add_test
# from test_cases import login_test
# from test_cases import recharge_test
# from test_cases import bidlodn_test

from libs.HTMLTestRunnerNew import HTMLTestRunner
from common_code.project_path import CASE_PATH, REPORT_FILE_PATH, USER_FILE_PATH, TEST_CASES_PATH
from common_code.project_path import CONFIG_FILE_PATH
from common_code.reg_fixed_account import RegFixeUser

conf = DoConfig(CONFIG_FILE_PATH)

# 判断用户文件是否已创建
if not os.path.exists(USER_FILE_PATH):
    RegFixeUser().crate_config()

# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(register_test))
# suite.addTest(loader.loadTestsFromModule(recharge_test))
# suite.addTest(loader.loadTestsFromModule(login_test))
# suite.addTest(loader.loadTestsFromModule(bidlodn_test))
# suite.addTest(loader.loadTestsFromModule(add_test))

# 自动识别指定文件夹下的测试文件
suite = unittest.defaultTestLoader.discover(TEST_CASES_PATH, pattern='*test.py')

with open(REPORT_FILE_PATH, 'wb') as rep_file:
    runner = HTMLTestRunner(rep_file, verbosity=conf.read_int('Report', 'verbosity'),
                            title=conf.read_info('Report', 'title'),
                            description=conf.read_info('Report', 'description'),
                            tester=conf.read_info('Report', 'tester'))
    runner.run(suite)
