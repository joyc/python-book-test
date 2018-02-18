#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

# m = re.match('foo', 'seafood')      # 使用match() 查不到
# if m is not None: m.group()
# print m.group()

n = re.search('foo', 'seafood')     # 改用search()
if n is not None: n.group()
print n.group()
