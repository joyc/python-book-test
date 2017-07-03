#!/usr/bin/env python3
# -*-coding:utf-8-*-

import os

totalSize = 0
myDir = 'C:\\Users\\rockb_000'
for filename in os.listdir(myDir):
    if not os.path.isfile(os.path.join(myDir, filename)):
            continue
    totalSize = totalSize + os.path.getsize(os.path.join(myDir,
                                                         filename))

print(totalSize)