#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/31/0031 0:25
# @Author  : Hython.com
# @File    : easyMath.py
from operator import add, sub, mul, floordiv
from random import randint, choice

ops = {'+': add, '-': sub, 'x': mul, '/': floordiv}
MAXTRIES = 2


def doprob():
    op = choice('+-x/')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print
                'correct'
                break
            if oops == MAXTRIES:
                print
                'answer\n%s%d' % (pr, ans)
            else:
                print
                'incorrect...try again'
                oops += 1
        except (KeyboardInterrupt, \
                EOFError, ValueError):
            print
            'invalid input...try again'


def main():
    while True:
        doprob()

        try:
            opt = raw_input('Again ? [y] ').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()