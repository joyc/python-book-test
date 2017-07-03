#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/03 15:33
# @Author  : Hython.com
# @File    : Restaurant.py
# @IDE     : PyCharm
class Restaurant():
    def __init__(self, restaurant_name, describe_type):
        """Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.describe_type = describe_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + "\n" +
              self.describe_type)

    def open_restaurant(self):
        print("The restaurant of " + self.restaurant_name + " is openning now...")

r1 = Restaurant('Zhong Hua', 'Chinese Food')
r2 = Restaurant('Ramen', 'JP Mian')

r1.describe_restaurant()
r1.open_restaurant()
r2.describe_restaurant()
r2.open_restaurant()