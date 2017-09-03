#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/8/2 0:18
# @Author  : Hython.com
# @File    : cmd_client.py
# @IDE     : PyCharm
import socket

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.connect(address)

while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))
    result_len = int(str(sk.recv(1024), 'utf-8'))
    sk.send('111') # 隔断
    data = bytes() # 初始化变量

    while len(data) != result_len:
        recv = sk.recv(1024)
        data += recv

    print(len(data))
    # 包含日语字符(cp932)
    print(data.decode('cp932'))

sk.close()
