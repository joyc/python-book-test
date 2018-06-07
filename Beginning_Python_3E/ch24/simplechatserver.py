from asyncore import dispatcher
from asynchat import async_chat
import asyncore, socket


PORT = 5005


class ChatSession(async_chat):

    def __inin__(self, sock):
        async_chat.__init__(self, sock)
        self.set_terminator("\r\n") # 设置行结束符为网络协议中常用结束符
        self.data = []

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data) # 合并这些字符串
        self.data = []
        # use line to do sth
        print(line)


class ChatServer(dispatcher):

    def __init__(self, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.sessions = []

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(conn))
        # print('Connection attempt from', addr[0])


if __name__ == '__main__':
    s = ChatServer(PORT)
    try: asyncore.loop()
    except KeyboardInterrupt: print()
