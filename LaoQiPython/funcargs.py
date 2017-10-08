#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/7 22:55
# @Author  : Hython.com
# @File    : funcargs.py


def func(x, *arg):
    print(x)
    result = x
    print(arg)
    for i in arg:
        result += i
    return result


print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))


def foo(**kargs):
    print(kargs)


foo(a=1, b=2, c=3)


def foos(x, y, z, *args, **kargs):
    print(x)
    print(y)
    print(z)
    print(args)
    print(kargs)


foos('li', 2, 3, "python", id='five', name='chuang')
