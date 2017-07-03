#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/01 0:29
# @Author  : Hython.com
# @File    : threadtest.py
# @IDE     : PyCharm
import threading, time
print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake Up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')