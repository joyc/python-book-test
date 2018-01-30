#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/31/0031 0:20
# @Author  : Hython.com
# @File    : ch6.queue.py

queue = []

def enQ():
    queue.append(raw_input('Enter new string: ').strip())

def deQ():
    if len(queue) == 0:
        print
        'cannot pop from an empty stack!'
    else:
        print
        'Removed [', `queue.pop(0)`, ']'  # 反逗号表示pop后的数值 pop掉第一个索引的值

def viewQ():
    print
    queue

CMDs = {'e': enQ, 'd': deQ, 'v': viewQ}

def showmenu():
    pr = """
    (E)nqueue
    (D)equeue
    (V)iew
    (Q)uit

    Enter choice: """

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print
            '\nYou picked: [%s]' % choice
            if choice not in 'devq':
                print
                'Invalid option, try again.'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()


if __name__ == '__main__':
    showmenu()