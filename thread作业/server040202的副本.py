# 书写一个类似于qq群聊的聊天室,要求所有人都能收到所有人发送的消息,要求实现客户端和服务端

import socket
from threading import Thread


def conn_recv(conn, conn_addr, conn_list):
    while 1:
        msg = conn.recv(65535)
        return_msg = '{}发来消息'.format(conn_addr) + msg.decode()
        for conn in conn_list:
            conn.send(return_msg.encode())

def conn_server(server_addr):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(server_addr)
    server.listen(10)
    print('服务器已启动')

    while 1:

        try:
            conn_list = []
            conn, conn_addr = server.accept()
            conn_list.append(conn)
            print('新来链接{}'.format(conn_addr))
            t = Thread(target=conn_recv, args=(conn, conn_addr, conn_list))
            t.start()

        except Exception:
            break


if __name__ == '__main__':
    server_addr = ('127.0.0.1', 56122)
    conn_server(server_addr)

    # server.close()