#!/usr/bin/env python
# coding: utf-8

import socket
import threading

def cli_recv(cli_sock):
    '''接受客户端数据'''
    while True:
        msg = cli_sock.recv(1024)
        print(msg)
        if msg == b'bye' or not msg:
            return


def main():
    '''Server 端主函数'''
    addr = ('127.0.0.1', 10000)
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(addr) # 端口绑定
    server_sock.listen(1024)
    client_socks = []

    while True:
        print('[server] i am listening')
        cli_sock, cli_addr = server_sock.accept() # 等待客户端连接
        t = threading.Thread(target=cli_recv, args=(cli_sock,))
        client_socks.append(t)
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()
