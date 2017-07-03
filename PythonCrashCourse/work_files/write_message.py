#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/04 23:01
# @Author  : Hython.com
# @File    : write_message.py
# @IDE     : PyCharm
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming by Python Language. 日本語だいじょうぶかな")