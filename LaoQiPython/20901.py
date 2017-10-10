#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/9 0:08
# @Author  : Hython.com
# @File    : 20901.py

__metaclass__ = type # 有这句相当于旧式类不需要显示声明继承Object类


class Person:
    def speak(self):
        print "I love you."

    def setHeight(self):
        print "The height is: 1.60m."

    def breast(self, n):
        print "My breast is:", n


class Girl(Person):
    def setHeight(self):
        print "The height is:1.70m."


if __name__ == "__main__":
    cang = Girl()
    cang.setHeight()
    cang.speak()
    cang.breast(90)