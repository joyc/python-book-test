#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/8/3 23:52
# @Author  : Hython.com
# @File    : ftp_client.py
# @IDE     : PyCharm
import socket
import os
sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    inp = input('>>>').strip() # post|lmz.jpg

    cmd, path = inp.split('|')
    path = os.path.join(BASE_DIR, path)
    # 要传输文件的属性
    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size
    # 打包传输给server端
    file_info = 'post|%s|%s' %(file_name, file_size)
    sk.sendall(bytes(file_info, 'utf-8'))

    f = open(path, 'rb')
    has_sent = 0
    while has_sent != file_size:
        data = f.read(1024)
        sk.sendall(data)
        has_sent += len(data)
    f.close()

sk.close()
