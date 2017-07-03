#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/02 0:40
# @Author  : Hython.com
# @File    : mountain_poll.py - 爬山投票调查联系
# @IDE     : PyCharm
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Result ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")