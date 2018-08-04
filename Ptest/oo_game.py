#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/4/0004 18:22
# @Author  : Hython.com
# @File    : oo_game.py
import random

class Sprite:

    step = [-2, +2, -3, +3]

    def __init__(self, gm, point=None):
        self.gm = gm
        if point is None:
            self.point = random.randint(0, 20)
        else:
            self.point = point

    def jump(self):
        astep = random.choice(self.step)
        if 0 <= self.point + astep <= 20:
            self.point += astep

class Ant(Sprite):

    def __init__(self):
        super().__init__(gm, point)
        self.gm.set_point('ant', self.point)

    def jump(self):
        super(Ant, self).jump()
        self.gm.set_point('ant', self.point)


class Worm(Sprite):

    def __init__(self, gm, point=None):
        super(Worm, self).__init__(gm, point)
        self.gm.set_point('worm', self.point)

    def jump(self):
        super().jump()
        self.gm.set_point('Worm', self.point)






