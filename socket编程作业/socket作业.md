####1、 书写一个socket服务器和客户端代码,要求客户端读取一个jpg或者png的媒体文件,然后发送给服务器,服务器接受并保存在磁盘上面(位置随意)

```
 客户端代码
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_addr = ('127.0.0.1', 35562)
client.connect(client_addr)

while True:
    try:

        msg1 = open('/Users/admin/Desktop/homework/socket编程作业/1.png')
        client.send(msg1.encode())

        msg = client.recv(65535)
        print('收到服务器消息：' + msg.decode())

    except Exception:
        break

client.close()

```
```
# 服务器代码
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 35562)
server.bind(server_addr)
server.listen(2)
client, client_addr = server.accept()
while True:
    try:
        msg = client.recv(65535)
        msg1 = b''
        if msg:
            msg1 += msg
        else:
            break

        print('收到{}发来的文件'.format(client_addr))
        file = open()
        file.write(msg1)

        return_msg = '文件已保存'
        client.send(return_msg.encode())
    except Exception:
        break

client.close()
server.close()
```
####2、 写一个socket用来请求百度网页,并把请求下来的报文体部分保存

```
import socket
from urllib.parse import urlparse


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
domain = "https://www.baidu.com"
url = urlparse(domain)
host = url.netloc
path = url.path
if path == "":
    path = "/"
client.connect((host, 80))

data = "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n" \
       "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) " \
       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36\r\n\r\n"\
    .format(path, host).encode('utf8')
client.send(data)
res = b""

while True:
    d = client.recv(1024)
    if d:
        res += d
    else:
        break
file = open('/Users/admin/Desktop/1.docx')
file.write(res.decode('utf8'))

client.close()
```