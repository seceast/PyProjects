"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 选择排序.py
@time: 2019/10/18 0018 11:08
"""

a = [1, 25, 33, 51, 21, 20, 15, 16, 22, 10, 19]


def select_sort(a_list):
    n = len(a_list)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a_list[min_index] > a_list[j]:
                min_index = j
        if min_index != i:
            a_list[i], a_list[min_index] = a_list[min_index], a_list[i]
    return a_list


print(select_sort(a))
