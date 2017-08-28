#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/11 17:11
# @Author  : Hython.com
# @File    : test.py
# @IDE     : PyCharm
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要处于活动状态，就不断模拟随机漫步
while True:
    # 创建一个 RandomWalk 实例并将其包含点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=40)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=40)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break