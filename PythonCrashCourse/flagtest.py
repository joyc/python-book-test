#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/02 0:20
# @Author  : Hython.com
# @File    : flagtest.py
# @IDE     : PyCharm
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)