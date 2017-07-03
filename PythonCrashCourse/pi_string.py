#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/04 18:26
# @Author  : Hython.com
# @File    : pi_string.py
# @IDE     : PyCharm


filename = 'work_files\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))