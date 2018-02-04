#!/usr/bin/env python
# from random import randint
from operator import add, mul
from functools import partial


add1 = partial(add, 1)
mul100 = partial(mul, 100)

print add1(1)
print mul100(10)

baseTwo = partial(int, base=2)
baseTwo.__doc__ = 'Convert base 2 string to an int.'
print baseTwo('10010')