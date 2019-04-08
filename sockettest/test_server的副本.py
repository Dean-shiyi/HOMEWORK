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
from threading import RLock
from concurrent.futures import ThreadPoolExecutor

pools = ThreadPoolExecutor(max_workers=20)
pools_list = []

lock = RLock()
conn_list = []

def recv_conn():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(server_addr)
    server.listen()

    while 1:
        lock.acquire()
        conn, conn_addr = server.accept()
        conn_list.append(conn)
        print('欢迎{}地址的用户'.format(conn_addr))
        lock.release()   # 防止某些用户进来后有些消息没收到
        # t = Thread(target=send, args=(conn, conn_addr))
        # t.start()

        from functools import partial
        pools.submit(partial(send, conn, conn_addr))

def send(conn, conn_addr):
    while 1:
        try:
            msg1 = b''
            msg = conn.recv(65535)
            if msg:
                msg1 += msg
            else:
                break
            # print('收到来自{}的消息{}'.format(conn_addr, msg1.decode()))
            return_msg = '地址{}的用户发来{}'.format(conn_addr, msg1.decode())
            for conn in conn_list:
                conn.send(return_msg.encode())

        except Exception:
            break


if __name__ == '__main__':

    server_addr = ('127.0.0.1', 12345)
    recv_conn()

