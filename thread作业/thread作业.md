#### 1、书写一个类似于百度的网站服务器,能够使用普通浏览器访问,只用返回简单的hello world即可
```
import socket
from threading import Thread


def conn_recv(conn, conn_addr):
    while True:
        try:
            msg = conn.recv(65535)
            print('收到{}的{}'.format(conn_addr, msg))
            return_msg = 'hello world'
            conn.send(return_msg.encode())
        except Exception:
            break
    conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 35642)
server.bind(server_addr)
server.listen(10)

while 1:
    try:
        conn, conn_addr = server.accept()
    except Exception:
        break
    t = Thread(target=conn_recv, args=(conn, conn_addr))
    t.start()

server.close()

```
#### 2、书写一个类似于qq群聊的聊天室,要求所有人都能收到所有人发送的消息,要求实现客户端和服务端
```
客户端
import socket
from threading import Thread

def recv():
    msg1 = b''
    msg1 += msg
    print(msg1.decode())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 56123)
client.connect(server_addr)

while 1:

    try:
        client.send(input('请输入：').encode())
        msg = client.recv(65535)
        if msg:
            t = Thread(target=recv)
            t.start()
        else:
            continue
    except Exception:
        break

client.close()
```
```
服务端
import socket
from threading import Thread


def conn_recv(conn, conn_addr):
    msg = conn.recv(65535)
    return_msg = '{}发来消息'.format(conn_addr) + msg.decode()
    conn.send(return_msg.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 56123)
server.bind(server_addr)
server.listen(10)

while 1:
    try:
        conn, conn_addr = server.accept()
    except Exception:
        break

    t = Thread(target=conn_recv, args=(conn, conn_addr))
    t.start()

server.close()
```