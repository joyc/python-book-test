#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/04 23:34
# @Author  : Hython.com
# @File    : word_count.py
# @IDE     : PyCharm
def count_words(filename):
    """计算字数"""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 计算字数
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has aout " + str(num_words) + " words.")

# filename = 'alice.txt'
# count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt']
for filename in filenames:
    count_words(filename)