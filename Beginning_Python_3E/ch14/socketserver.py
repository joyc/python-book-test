import socket


s = socket.socket()

host = socket.gethostname()
prot = 1234
s.bind((host, prot))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting')
    c.close()
