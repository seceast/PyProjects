# -*- coding: utf-8 -*-
# @author: yangyd
# @file: learn_yaml.py
# @time: 2019/9/25 0025 上午 11:26


import yaml

# yaml.dump()
with open('demo.yaml', 'r', encoding='utf8')as f:
    caps = yaml.load(f, Loader=yaml.FullLoader)

print(type(caps['phone_list'][0]))
print(caps['phone1'])

