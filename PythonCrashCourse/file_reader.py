#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/04 18:00
# @Author  : Hython.com
# @File    : file_reader.py
# @IDE     : PyCharm

# with open('work_files\pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

file_name = 'work_files\pi_digits.txt'

# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.rstrip())

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())