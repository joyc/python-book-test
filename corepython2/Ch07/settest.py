#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/31/0031 0:22
# @Author  : Hython.com
# @File    : settest.py
s = set('bookshop')
print s
t = frozenset('cheeseshop')
print t

print type(s), type(t)