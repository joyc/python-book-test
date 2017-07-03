#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/03 13:52
# @Author  : Hython.com
# @File    : sandwitch.py
# @IDE     : PyCharm
def make_car(maker, mode, **info):
    cars = {}
    cars['maker'] = maker
    cars['mode'] = mode
    for key, value in info.items():
        cars[key] = value
    return cars

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)