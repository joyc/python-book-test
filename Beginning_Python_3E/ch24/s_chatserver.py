from asyncore import dispatcher
import socket, asyncore


class ChatServer(dispatcher):
    def handle_accept(self):
        conn, addr = self.accept()
        print('Connection attempt from', addr[0])


s = ChatServer()
s.create_socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5005)) # 空字符串，意味着localhost，即当前机器的所有接口
s.listen(5)
asyncore.loop()
