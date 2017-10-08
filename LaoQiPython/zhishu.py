#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/8 13:46
# @Author  : Hython.com
# @File    : zhishu.py
"""
找质数
"""
import math


def is_prime(n):
    """判断是否是质数"""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    primes = [i for i in range(2, 100) if is_prime(i)] # 从2开始判断
    print primes