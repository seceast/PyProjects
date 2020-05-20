"""
-*- coding: utf-8 -*-
@author: yangyd
@file: learn_code2.py
@time: 2019/10/24 0024 10:14
"""

# 使用装饰器，不修改func源码，添加输出日志信息
import time


def func1():
    print(111)


def func2():
    print(222)


def write_log(func):
    try:
        file = open('log.txt', 'a', encoding='utf-8')
        file.write("访问")
        file.write(func.__name__)
        file.write('\t')
        file.write(time.asctime() + '\n')
    except Exception as e:
        print(e.args)
    finally:
        file.close()


# 使用闭包
def func_out(func):
    def func_in():
        write_log(func)
        func()

    return func_in


# 闭包调用
f = func_out(func1)
f()


# 使用装饰器 等同于闭包的调用
@func_out
def func1_1():
    print(111)


@func_out
def func2_2():
    print(222)


func1_1()
func2_2()
