#!/usr/bin/env python  
# encoding: utf-8  
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 1.3-deque.py
@time: 2018/4/9 17:56 
@version: v1.0 
"""
from collections import deque


def Search(lines, pattarn, history = 5):
    previous_lines = deque(maxlen = history)

    for line in lines:      # 文件对象可以迭代！！
        if pattarn in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    with open("test_deque.txt", "r") as f:
        for line, previous_lines in Search(f, "python"):
            for pline in previous_lines:
                print(pline)
            print(line)
            print('-' * 36)
