# 书写一个类似于qq群聊的聊天室,要求所有人都能收到所有人发送的消息,要求实现客户端和服务端
import socket
from threading import Thread

def cli_recv():
    while 1:
        msg = client.recv(65535)
        msg1 = b''
        msg1 += msg
        print(msg1.decode())

def cli_send():
    while 1:
        try:
            client.send(input('请输入：').encode())
        except Exception:
            break

# client.close()


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ('127.0.0.1', 56122)
    client.connect(server_addr)
    send = Thread(target=cli_send)
    recv = Thread(target=cli_recv)

    send.start()
    recv.start()

    send.join()
    recv.join()

    client.close()