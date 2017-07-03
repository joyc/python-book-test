#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/04 14:18
# @Author  : Hython.com
# @File    : my_electric_car.py
# @IDE     : PyCharm
from car import Car, ElectricCar

my_beetle = Car('Volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())


my_tesla = ElectricCar('Tesla', 'Model S', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
