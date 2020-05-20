#!/user/bin/env python
# -*- coding: utf-8 -*-
# __author__ = yangyd 
# Create time: 2019/6/27 0027 11:07


import os
from common.operate_config import DoConfig
from datetime import datetime

# 项目路径  两种方法效果一样
# PROJECT_PATH = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试用例文件路径
CASE_PATH = os.path.join(PROJECT_PATH, 'test_datas')
CASE_FILE_PATH = os.path.join(CASE_PATH, 'test_cases.xlsx')

# 配置文件路径
CONFIG_PATH = os.path.join(PROJECT_PATH, 'config_file')
CONFIG_FILE_PATH = os.path.join(CONFIG_PATH, 'config.conf')

USER_FILE_PATH = os.path.join(CONFIG_PATH, 'user.conf')

# 日志路径
LOG_PATH = os.path.join(PROJECT_PATH, 'logs')
LOG_FILE_PATH = os.path.join(LOG_PATH, 'app_test_log.txt')

# 测试报告路径
path_conf = DoConfig(CONFIG_FILE_PATH)

# 报告结尾添加时间戳
timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
html = path_conf.read_info('Report', 'html_name')
report_name = html+'_'+timestamp

REPORT_PATH = os.path.join(PROJECT_PATH, 'reports')
REPORT_FILE_PATH = os.path.join(REPORT_PATH, report_name+'.html')

# 测试类文件路径
TEST_CASES_PATH = os.path.join(PROJECT_PATH, 'test_cases')

if __name__ == '__main__':
    print(PROJECT_PATH)
    print(CASE_PATH)
    print(CONFIG_FILE_PATH)
    print(LOG_FILE_PATH)
    print(REPORT_FILE_PATH)
