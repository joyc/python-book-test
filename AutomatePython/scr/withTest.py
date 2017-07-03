#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# os.walk循环列出目录文件，返回三个值
for folderName, subfolders, filenames in os.walk('c:\\Python\\MyScripts'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')




