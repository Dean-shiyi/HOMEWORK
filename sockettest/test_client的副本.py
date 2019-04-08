# P1901socket编程试题(考试时间2小时):
# 题目: 实现一个多人聊天室
# 要求:
# 1.至少实现一个服务端客户端(C / S模式)的聊天室服务端和客户端代码(0 - 40分)
# 2.能够进行多人同时和服务器收发消息的服务端和客户端代码(40 - 60分)
# 3.能够实现多人同时和服务器收发消息, 并且服务器会广播消息的服务端和客户端代码(60 - 70分)
# 4.能够使用线程池来实现上面功能(70 - 80分)
# 5.能够在完成4要求的情况下考虑到多线程切换的问题, 并且对合适的地方上锁, 并说明为什么要上锁(80 - 90分)
# 6.能够在完成5的要求下实现客户端能顺利关闭退出,
# 并且其他客户端能收到有客户端退出的消息, 并且整体代码无bug(90 - 100分)


import socket
from threading import Thread

client = socket.socket()
addr = ('127.0.0.1', 12345)
client.connect(addr)


def recv_msg():
    while 1:
        try:
            msg = client.recv(65535)
            msg1 = b''
            if msg:
                msg1 += msg
            else:
                break
            print(msg1.decode())

        except Exception:
            break

def send_msg():
    while 1:
        try:
            client.send(input('请输入消息：').encode())
        except Exception:
            break

t1 = Thread(target=send_msg)
t2 = Thread(target=recv_msg)
t1.start()
t2.start()

t1.join()
t2.join()






