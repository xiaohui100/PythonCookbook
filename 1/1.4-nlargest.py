#!/usr/bin/env python  
# encoding: utf-8  
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 1.4-nlargest.py 
@time: 2018/4/9 18:07 
@version: v1.0 
"""
import heapq

nums = [32, 12, -1, 23, -4, 213, 22, 0]

max_third = heapq.nlargest(3, nums)
min_third = heapq.nsmallest(3, nums)

portinfo = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'apple', 'shares': 101, 'price': 678.1},
    {'name': 'google', 'shares': 99, 'price': 391.1},
    {'name': 'microsoft', 'shares': 1000, 'price': 921.1},
    {'name': 'amzone', 'shares': 199, 'price': 241.1}, ]

cheap_third = heapq.nsmallest(3, portinfo, key = lambda z: z['price'])
pass
