#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/31/0031 0:24
# @Author  : Hython.com
# @File    : errortest.py
def safe_float(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = 'could not conver non-number to float'
    return retval
