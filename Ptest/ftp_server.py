#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/8/3 23:52
# @Author  : Hython.com
# @File    : ftp_server.py
# @IDE     : PyCharm
import socket
import os
sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.bind(address)
sk.listen(3)
print('waiting......')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while 1:
    conn, addr = sk.accept()
    while 1:
        data = conn.recv(1024)
        cmd, file_name, file_size = str(data, 'utf-8').split('|')
        path = os.path.join(BASE_DIR, 'ftp', file_name)
        file_size = int(file_size)

        f = open(path, 'ab')
        has_receive = 0
        while has_receive != file_size:
            data = conn.recv(1024)
            f.write(data)
            has_receive += len(data)
        f.close()

sk.close()