#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/29/0029 23:48
# @Author  : Hython.com
# @File    : ex1.py
"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
"""

# 1
# num=[1,2,3,4]
# i=0
# for a in num:
#     for b in num:
#         for c in num:
#             if (a!=b) and (b!=c) and (c!=a):
#                 i+=1
#                 print(a,b,c)
# print('总数是：',i)

# 2 用集合去除重复元素
# import pprint

# list_num=['1','2','3','4']
# list_result=[]
# for i in list_num:
#     for j in list_num:
#         for k in list_num:
#             if len(set(i+j+k))==3:
#                 list_result+=[int(i+j+k)]
# print("能组成%d个互不相同且无重复数字的三位数: "%len(list_result))
# pprint.pprint(list_result)

# 3 自带函数permutations
# from itertools import permutations

# for i in permutations([1, 2, 3, 4], 3):
#     k = ''
#     for j in range(0, 3):
#         k += str(i[j])
#     print (k)

# 3.2
# from itertools import permutations
# t = 0
# for i in permutations('1234',3):
#     print(''.join(i))
#     t += 1

# print("不重复的数量有:%s"%t)

# 4 位运算
#从 00 01 10  到  11 10 01
# for num in range(6,58):
#     a = num >> 4 & 3
#     b = num >> 2 & 3
#     c = num & 3
#     if( (a^b) and (b^c) and (c^a) ):
#         print(a+1,b+1,c+1)

# 5 列表解析
# list_num = [1,2,3,4]
# list = [i*100 + j*10 + k for i in list_num for j in list_num for k in list_num if ( i != j and i != k and j != k)]
# d = len(list)
# print('1,2,3,4能组成 %d 个互不相同且无重复数字的三位数。' % d)
# print('他们各是:%s' % list)

# 5.2 列表解析式
list = [(x,y,z) for x in range(1,5) for y in range(1,5) for z in range(1,5) if(x!=y)and(x!=z)and(y!=z)]
print(list)
