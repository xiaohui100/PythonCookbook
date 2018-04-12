#!/usr/bin/env python  
# encoding: utf-8  
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 1.5-heappush.py 
@time: 2018/4/12 19:12 
@version: v1.0 
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self.__queue = []
        self.__index = 0

    def push(self, item, priority):
        heapq.heappush(self.__queue, (-priority, self.__index, item))
        self.__index += 1

    def pop(self):
        return heapq.heappop(self.__queue)[-1]  # -1为item对象


class Item:
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return "Item({!r})".format(self.__name)


q = PriorityQueue()
q.push(Item("foo"), 1)
q.push(Item("bar"), 5)
q.push(Item("cao"), 3)
q.push(Item("hig"), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
