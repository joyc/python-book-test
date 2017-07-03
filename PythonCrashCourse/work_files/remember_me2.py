#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/05 0:16
# @Author  : Hython.com
# @File    : remember_me2.py
# @IDE     : PyCharm
import json

def greet_user():
    """问候用户"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name ? ")
        with open(filename, 'w', encoding='utf-8') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()