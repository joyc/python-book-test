#!/usr/bin/env python
# -*- coding:utf-8 -*-


class P:    # 父类
    'P class'
    def __init__(self):
        print 'create an instance of', \
            self.__class__.__name__


class C(P):  # 子类
    pass


p = P()         # 父类实例
print p.__class__     # 显示p所属的类名
print P.__bases__     # 父类的父类
print P.__doc__       # 父类的文档字符串
