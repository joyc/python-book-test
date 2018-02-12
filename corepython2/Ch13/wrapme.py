#!/usr/bin/env python
# -*- coding:utf-8 -*-


class WrapMe(object):
    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __repr__(self):
        return 'self.__data'

    def __str__(self):
        return str(self.__data)

    def __getattr__(self, attr):
        return getattr(self.__data, attr)


wrappedComplex = WrapMe(3.5 + 4.2j)
print wrappedComplex                # 包装的对象：repr()
print wrappedComplex.real, wrappedComplex.imag  # 实部属性， 虚部属性
print wrappedComplex.conjugate()  # conjugate()方法
print wrappedComplex.get()  # 实际对象