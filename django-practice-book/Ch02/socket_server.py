#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
socket_server
"""
import socket

EOL1 = '\n\n'
EOL2 = '\n\r\n'
body = '''Hello, world! <h1> from Hython.com <<Django企业开发实战项目>> </h1>'''
response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sat, 10 Feb 2018 01:01:01 GMT',
    'Content-Type: text/plain; charset=utf-8',
    'Content-Length: {}\r\n'.format(len(body)),
    body,
]
response = b'\r\n'.join(response_params)


def handle_connection(conn, addr):
    request = ""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    conn.send(response)
    conn.close()


def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8080))
    serversocket.listen(1)
    print('http://127.0.0.1:8080')

    try:
        while True:
            conn, address = serversocket.accept()
            handle_connection(conn, address)
    finally:
        serversocket.close()


if __name__ == '__main__':
    main()
