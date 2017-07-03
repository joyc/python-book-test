#!/usr/bin/env python3
# -*-coding:utf-8-*-

import shelve

shelveFile = shelve.open('mydata')
shelveFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelveFile.close()
