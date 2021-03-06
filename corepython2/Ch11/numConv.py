#!/usr/bin/env python
# -*- coding:utf-8 -*-


def convert(func, seq):
    'conv. sequence of number to same type'
    return [func(eachNum) for eachNum in seq]


myseq = (123, 45.67, -6.2e8, 999999999L)
print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)