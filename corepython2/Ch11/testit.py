#!/usr/bin/env python
"""
testit()用其参数地调用了一个给定的函数,成功的话，
返回一个和那函数返回值打包的True的返回值，或者False和失败的原因。
"""


def testit(func, *nkwargs, **kwargs):

    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception, diag:
        result = (False, str(diag))
    return result


def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '_' * 20
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            if retval[0]:
                print '%s(%s)= ' %(eachFunc.__name__, 'eachVal'), retval[1]
            else:
                print '%s(%s)= FAILED:' %(eachFunc.__name__, 'eachVal'), retval[1]


if __name__ == '__main__':
    test()