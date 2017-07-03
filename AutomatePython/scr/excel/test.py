#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/05/14 12:12
# @Author  : Hython.com
# @File    : test.py
# @IDE     : PyCharm

import openpyxl
workbook = openpyxl.load_workbook('example.xlsx')
print(type(workbook))
sheet = workbook.get_sheet_by_name('sheet1')
print(type(sheet))
workbook.get_sheet_names()
sheet['A1']