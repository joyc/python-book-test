#!/usr/bin/env python

# from random import randint
#
#
# def randGen(aList):
#     while len(aList) > 0:
#         yield aList.pop(randint(0, len(aList)))
#
#
# for item in randGen(['rock', 'paper', 'scissors']):
#     print item


# counter
import time
def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1


count = counter(5)
count.next()
time.sleep(1)
count.next()
time.sleep(1)
count.send(9)
time.sleep(1)
count.next()
count.close()
time.sleep(1)
count.next()