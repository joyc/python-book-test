#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/03 14:47
# @Author  : Hython.com
# @File    : pizza.py
# @IDE     : PyCharm
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppongs:")
    for topping in toppings:
        print("- " + topping)
