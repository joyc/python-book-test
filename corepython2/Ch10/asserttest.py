#!/usr/bin/env python
# -*- coding:utf-8 -*-

try:
    assert 1 == 0, 'One dose not equal zero silly!'
except AssertionError, args:
    print '%s: %s' % (args.__class__.__name__, args)


def asserttest(expr, args=None):
    if __debug__ and not expr:
        raise AssertionError, args
