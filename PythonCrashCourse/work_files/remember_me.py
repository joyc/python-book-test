#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/05 0:04
# @Author  : Hython.com
# @File    : remember_me.py
# @IDE     : PyCharm
import json

# 如果之前存储了用户名就加载
# 否则就提示用户输入并存储它

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("Please input your name : ")
    with open('username.json', 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + " !")
else:
    print("Welcome back " + username + " !")
