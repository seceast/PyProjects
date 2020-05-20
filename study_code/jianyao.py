"""
-*- coding: utf-8 -*-
@author: yangyd
@file: jianyao.py
@time: 2019/10/9 0009 14:36
"""


#
# def res_compare(a: dict, b: dict):
#     result = None
#     key_list = list(a.keys())
#     for i in key_list[1:]:
#         if a[i] == b[i]:
#             result = "成功"
#         else:
#             result = "失败"
#     return result
#
#
# res = res_compare({"a": 1, "b": 2}, {"a": 2, "b": 2})
# print(res)
#
#
# # a = {"a": 1, "b": 2, "c": 3}
# # i = list(a.keys())
# # i = i[1:]
# # print(i)


class Test:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)


test1 = Test('yyd')
test1.get_name()
