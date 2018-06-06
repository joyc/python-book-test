from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5005

class ChatS(object):
    """docstring for ChatS"""
    def __init__(self, arg):
        super(ChatS, self).__init__()
        self.arg = arg
        