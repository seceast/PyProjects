"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 插入排序.py
@time: 2019/10/18 0018 13:49
"""


def insert_sort(a_list):
    n = len(a_list)
    for j in range(1, n):
        i = j
        while i > 0:  # 和有序列表内的每个元素进行比较（最后一个开始）
            if a_list[i] < a_list[i - 1]:  # 当前元素比前一个元素小，则进行交换
                a_list[i], a_list[i - 1] = a_list[i - 1], a_list[i]
            else:
                break
            i -= 1
    return a_list


a = [1, 25, 33, 51, 21, 20, 15, 16, 22, 10, 19]
print(insert_sort(a))
