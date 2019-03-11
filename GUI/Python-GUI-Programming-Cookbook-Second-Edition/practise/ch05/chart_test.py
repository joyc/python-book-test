#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/11/0011 17:37
# @Author  : Hython.com
# @File    : chart_test.py
import numpy as np
import matplotlib.pyplot as plt
from pylab import show

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)

show()
