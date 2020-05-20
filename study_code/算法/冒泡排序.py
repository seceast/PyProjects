"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 冒泡排序.py
@time: 2019/10/18 0018 10:40
"""


def bubble_sort(a_list):
    n = len(a_list)
    for k in range(n - 1):
        for i in range(n - 1 - k):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
    return a_list


def bubble_sort2(a_list):
    """算法优化，如果传入的列表是有序的，则检查一轮，如果不需要进行交换，则退出循环"""
    n = len(a_list)
    for k in range(n - 1):
        count = 0
        for i in range(n - 1 - k):
            if a_list[i] > a_list[i + 1]:
                count += 1
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        if count == 0:
            break
    return a_list


a = [1, 25, 33, 51, 21, 20, 15, 16, 22, 10, 19]
print(bubble_sort(a))
print(bubble_sort2(a))
