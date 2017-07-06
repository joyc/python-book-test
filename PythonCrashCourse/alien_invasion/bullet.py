#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/06/07 0:00
# @Author  : Hython.com
# @File    : bullet.py
# @IDE     : PyCharm
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个进行管理子弹发射的类"""
    def __init__(self, ai_settings, screen, ship):
        """在飞船所处位置建一个子弹对象"""
        super(Bullet, self).__init__() # 继承Sprite类 py2.7 写法 3为 super().__init__()
        self.screen = screen

        # 在（0， 0）处创建一个表示子弹的矩形在设置正确位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """让子弹向上移动"""
        # 更新表示子弹位置的小数
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)