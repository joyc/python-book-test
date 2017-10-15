#! python2
# -*- coding:utf-8 -*-
# @Time    : 2017/9/30 20:24
# @Author  : Hython.com
# @File    : ood.py.py
# @IDE     : PyCharm


class AddrBookEntry(object):  # 类定义
    """address book entry class"""

    def __init__(self, nm, ph):  # 定义构造器
        self.name = nm  # 设置name
        self.phone = ph  # 设置phone
        print 'Created instance for:', self.name

    def update_phone(self, newph):  # 定义方法
        self.phone = newph
        print 'Updated phone# for:', self.name


class EmplAddrBookEntry(AddrBookEntry):
    """Employee Address Book Entry class"""  # 员工地址簿类

    def __init__(self, nm, ph, id, em):
        '重新构造子类构造器时，父类的构造器需显示写出↓'
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em

    def update_email(self, newem):
        self.email = newem
        print 'Updated e-mail address for:', self.name
