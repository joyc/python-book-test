#!/usr/bin/env python
# -*- coding:utf-8 -*-
# addinterest3.py

def addInterest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rate)

def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    amount = addInterest(amounts, rate)
    print(amounts)


test()
