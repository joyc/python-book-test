#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/31/0031 0:21
# @Author  : Hython.com
# @File    : ch6.stack.py
stack = []


def pushit():
    stack.append(raw_input('Enter new string: ').strip())


def popit():
    if len(stack) == 0:
        print
        'cannot pop from an empty stack!'
    else:
        print
        'Removed [', `stack.pop()`, ']'  # 反逗号表示pop后的数值


def viewstack():
    print
    stack


CMDs = {'u': pushit, 'o': popit, 'v': viewstack}


def showmenu():
    pr = """
    p(U)sh
    p(O)p
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
            if choice not in 'uovq':
                print
                'Invalid option, try again.'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()


if __name__ == '__main__':
    showmenu()