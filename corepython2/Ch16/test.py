#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# from socket import *
# tcpSock = socket(AF_INET, SOCK_STREAM)
# socket.get
#
# ss = socket()                   # 创建服务器套接字
# ss.bind()                       # 把地址绑定到套接字上
# ss.listen()                     # 监听连接
# inf_loop:                       # 服务器无限循环
#     cs = ss.accept()            # 接受客户端连接
# comm_loop:                      # 通信循环
#     cs.recv() / cs.send()       # 对话（接收和发送）
# cs.close()                      # 关闭客户端套接字
# ss.close()                      # 关闭服务器套接字（可选）