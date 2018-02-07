#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/14 10:36
# @Author  : Hython.com
# @File    : hoteltax.py
# 代码的主要目的是来帮助某人计算出每日旅馆租房费用，包括所有州销售税和房税。缺省为旧金山附近的普通区域，
# 它有8.5%销售税及10%的房间税。每日租房费用没有缺省值，因此在任何实例被创建时，都需要这个参数。
# __init__()构造器对一些实例属性进行初始化。calcTotal()方法用来决定是计算每日总的租房费用还是计算全部的租房费。


class HotelRoomCalc(object):
    """hotel room rate calculator"""

    def __init__(self, rt, sales=0.085, rm=0.1):
        '''HotelRoomCalc default arguments:
        salesTax == 8.5% and roomTax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        'alculate total; default to daily rate'
        daily = round((self.roomRate *
            (1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily


sfo = HotelRoomCalc(299)                    # 新的实例
print 'one day fee:', sfo.calcTotal()       # 日租金
print 'Two days fee:', sfo.calcTotal(2)     # 2天的租金
sea = HotelRoomCalc(189, 0.086, 0.058)      # 新的实例
print '1天的费用:', sea.calcTotal()
print '4天的费用:', sea.calcTotal(4)
wasWkDay = HotelRoomCalc(169, 0.045, 0.02)  # 新实例
wasWkEnd = HotelRoomCalc(119, 0.045, 0.02)  # 新实例
fee = wasWkDay.calcTotal(5) + wasWkEnd.calcTotal()    # 7天的租金
print '平日+周六一共:', fee