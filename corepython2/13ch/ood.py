#! python2
# -*- coding:utf-8 -*-
# @Time    : 2017/9/30 20:24
# @Author  : Hython.com
# @File    : ood.py.py
# @IDE     : PyCharm
import os

filename = __file__
stat_info = os.stat(filename)
print(stat_info.st)
