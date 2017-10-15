#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/14 10:36
# @Author  : Hython.com
# @File    : hoteltax.py


# 代码的主要目的是来帮助某人计算出每日旅馆租房费用，包括所有州销售税和房税。缺省为旧金山附近的普通区域，它有8.5%销售税及10%的房间税。
# 每日租房费用没有缺省值，因此在任何实例被创建时，都需要这个参数。
# __init__()构造器对一些实例属性进行初始化。calcTotal()方法用来决定是计算每日总的租房费用还是计算全部的租房费。
class HotelRoomCalc(object):
    """hotel room rate calculator"""

    def __init__(self, rt, sales=0.085, rm=0.1):
        """hotelroomcalc default arguments:"""
            salesTax == 8.5% and roomTax == 10
            self.salesTax = sales
            self.roomTax = rm
            self.roomRate = rt

    def calcTotal(self, days=1):
        """Calculate total; default to daily rate"""
        daily = round((self.roomRate *
            (1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily
