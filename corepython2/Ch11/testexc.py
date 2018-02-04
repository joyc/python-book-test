#!/usr/bin/env python
j, k = 1, 2


def proc1():

    j, k = 3, 4
    print "j == %d and k == %d" %(j, k) # 3,4
    k = 5


def proc2():

    j = 6
    proc1()
    print "j == %d and k == %d" %(j, k) # 6,5


k = 7
proc1()
print "j == %d and k == %d" %(j, k) # 3,7

j = 8
proc2()
print "j == %d and k == %d" %(j, k) # 8,5
