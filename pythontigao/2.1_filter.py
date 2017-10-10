#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/10 23:18
# @Author  : Hython.com
# @File    : 2.1_filter.py
from random import randint

""" 
过滤掉列表[3,9,-1,10,20,-2...]中的负数
"""
data = [randint(-10, 10) for _ in range(10)]
print(data)
# 用filter函数过滤负数
filter(lambda x: x>= 0, data)

# 用列表解析式过滤负数
[x for x in data if x >= 0]

# 使用timeit测试运行时间,列表解析更快。
timeit filter(lambda x: x>= 0, data)
timeit [x for x in data if x >= 0]

"""
筛出字典{'LiLei':79,'Jim':88,'Lucy':92...}中值高于90的项
"""
# 生成随机字典
d = {x: randint(60, 100) for x in range(1, 21)}

{k: v for k, v in d.iteritems() if v > 90}

"""
筛出集合{77,89,32,20...}中能被3整除的元素
"""
s = set(data)

{x for x in s if x % 3 == 0}
