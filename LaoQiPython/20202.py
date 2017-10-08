#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/7 17:21
# @Author  : Hython.com
# @File    : functest.py


# def fibs(n):
#     result = [0, 1]
#     for i in range(n-2):
#         result.append(result[-2] + result[-1])
#     return result
#
#
# if __name__ == '__main__':
#     lst = fibs(10)
#     print(lst)

# 递归版
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# if __name__ == "__main__":
#     f = fib(10)
#     print(f)


# 递归版优化版
meno = {0:0, 1:1}

def fib(n):
    if not n in meno:
        meno[n] = fib(n-1) + fib(n-2)
    return meno[n]


if __name__ == "__main__":
    f = fib(10)
    print(f)