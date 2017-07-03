#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/04 23:10
# @Author  : Hython.com
# @File    : guest_list.py
# @IDE     : PyCharm
filename = 'guest_list.txt'

while True:
    guest_name = input("请输入你的名字？ ：")
    if guest_name == "q":
        break

    print("Hello %s welcome back %s" % (guest_name, guest_name))
    with open(filename, 'a') as file_object:
        file_object.write(guest_name + '\n')
