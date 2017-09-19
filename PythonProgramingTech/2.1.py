#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/8/28 23:09
# @Author  : Hython.com
# @File    : 2.1.py
# @IDE     : PyCharm

# 在列表中根据条件筛选数据
from random import randint
data = [randint(-10, 10) for _ in range(10)]

# 1. 使用filter()过滤负数
filter(lambda x: x > 0, data)
