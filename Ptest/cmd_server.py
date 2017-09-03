#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/8/2 0:21
# @Author  : Hython.com
# @File    : cmd_server.py
# @IDE     : PyCharm
import socket
import subprocess
sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.bind(address)
sk.listen(3)
print('waiting......')

while 1:
    conn, addr = sk.accept()
    print(addr)
    while 1:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        if not data: break
        print('......', str(data, 'utf8'))

        obj = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)
        cmd_result = obj.stdout.read()
        # 先传结果的长度,socket只能传送byte类型
        result_len = bytes(str(len(cmd_result)), 'utf8')
        print('>>>>>', result_len)
        conn.sendall(result_len)
        # 连续两个send时防止黏包
        conn.recv(1024)
        conn.sendall(cmd_result)

sk.close()