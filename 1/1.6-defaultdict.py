#!/usr/bin/env python  
# encoding: utf-8  
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 1.6-defaultdict.py 
@time: 2018/4/12 19:25 
@version: v1.0 
"""
from collections import defaultdict

d = defaultdict(list)  # 设置d的value为list
d[1].append(1)
d[1].append(1)
d[2].append(3)

print(d)

s = defaultdict(set)  # 设置s的value为set
s[1].add(1)
s[1].add(1)
s[2].add(3)

print(s)

d = dict()
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', {}).update({2: 3})

print(d)

from collections import OrderedDict

