#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/29/0029 23:49
# @Author  : Hython.com
# @File    : ex1.2.py
"""
获取 100 以内的质数/素数
"""
# 1
num = [];
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        num.append(i)
print(num)

# 2
import math


def func_get_prime(n):
    return filter(lambda x: not [x % i for i in range(2, int(math.sqrt(x)) + 1) if x % i == 0], range(2, n + 1))


print(list(func_get_prime(100)))

# 2.2
import math

N = 100
print([p for p in range(2, N) if 0 not in [p % i for i in range(2, int(math.sqrt(p)) + 1)]])

# 2.3 列表解析
u = [n for n in range(2, 100) if not [m for m in range(2, n) if n % m == 0]]
print(u)