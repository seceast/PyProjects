#!/usr/bin/env.python
# -*- coding: utf-8 -*-
# __author__ = yangyd
# Create time: 2019/7/15 23:47


import re

from common_code.operate_excel import DoExcel
from common_code.project_path import CASE_FILE_PATH

data_str = DoExcel(CASE_FILE_PATH, 'register').read_excel(2, end_row=2)
print(data_str[0])

math_res = re.match(r"{'id", str(data_str[0]))
print(math_res.group())

sea_res = re.search(r'\${unreg_phone}', str(data_str[0]))
print(sea_res.group())

sub_res = re.sub(r'\${unreg_phone}', '13333333333', str(data_str[0]))
print(sub_res)
