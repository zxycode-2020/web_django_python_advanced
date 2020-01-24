
import sys
import time
import socket
import threading
from random import randrange


class Client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None

    def connect(self):
        '''连接'''
        if self.sock is None:
            self.sock = socket.socket()  # 创建 socket 对象
            addr = (self.host, self.port)
            self.sock.connect(addr)      # 向服务器发起连接

    def disconnect(self):
        '''断开连接'''
        if self.sock is not None:
            self.sock.close()

    def send(self, msg):
        if not isinstance(msg, bytes):
            msg = str(msg).encode('utf8')
        self.sock.send(msg)


    def __enter__(self):
        '''
        1. 建立连接
        2. 向服务器发送 "Hello"
        3. 返回实例本身
        '''
        self.connect()
        self.send('hello')
        return self

    def __exit__(self, type, value, traceback):
        '''
        1. 向服务器发送 'bye'
        2. 断开连接
        '''
        self.send( "bye")
        self.disconnect()


if __name__ == '__main__':
    # name = sys.argv[1]
    with Client('127.0.0.1', 10000) as c:   # 创建客户端并连接服务器
        while True:
            line = input('>>>')
            if line == 'exit':
                break
            c.send(line)
