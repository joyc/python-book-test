#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/04 13:59
# @Author  : Hython.com
# @File    : my_car.py
# @IDE     : PyCharm
from car import Car

my_new_car = Car('Audi', 'A4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


