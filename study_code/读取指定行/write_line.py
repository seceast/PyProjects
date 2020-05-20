# -*- coding: utf-8 -*-
# @author: yangyd
# @file: write_line.py
# @time: 2019/9/19 10:02 


with open('test.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    new_lines = [str(line).rstrip()+'#' + str(index) + '\n' for index, line in enumerate(lines)]
    # f.writelines(new_lines)
    # print(new_lines)

with open('test.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
