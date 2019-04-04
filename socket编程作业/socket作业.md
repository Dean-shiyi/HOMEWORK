#### 1、 书写一个socket服务器和客户端代码,要求客户端读取一个jpg或者png的媒体文件,然后发送给服务器,服务器接受并保存在磁盘上面(位置随意)

```
 import os
dir_name = os.path.dirname(__file__)
jpg_name = os.path.join(dir_name, 'os.png')
with open(jpg_name, 'rb') as f:
    b_file = f.read()

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_addr = ('127.0.0.1', 35563)
client.connect(client_addr)

while True:
    try:

        # msg1 = open('/Users/admin/Desktop/my_homework/socket编程作业/1.png')
        # client.send(msg1.encode())
        client.sendall(b_file)

        msg = client.recv(65535)
        print('收到服务器消息：' + msg.decode())

    except Exception:
        break

client.close()

```
```
# 服务器代码
import os
import socket
dir_name = os.path.dirname(__file__)
jpg_name = os.path.join(dir_name, 'os_copy1.png')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 35563)
server.bind(server_addr)
server.listen()
print('服务器已启动')

while True:
    client, client_addr = server.accept()
    msg1 = b''
    try:
        msg = client.recv(65535)
        if msg:
            msg1 += msg
        else:
            break
    except Exception:
        break

with open(jpg_name, 'wb') as f:
    f.write(msg1)
print('收到{}发来的文件'.format(client_addr))
return_msg = '文件已保存'
client.send(return_msg.encode())

client.close()
server.close()
```
#### 2、 写一个socket用来请求百度网页,并把请求下来的报文体部分保存
```
import socket


def get(name):
    client = socket.socket()
    addr = ('blog.jobbole.com', 80)
    client.connect(addr)

    headers = b"GET /114633/ HTTP/1.1\r\nHost: blog.jobbole.com\r\nConnection: closed\r\n" \
              b"Cache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: " \
              b"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) " \
              b"Chrome/73.0.3683.86 Safari/537.36\r\nAccept: text/html,application/xhtml+xml," \
              b"application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\n\r\n"

    client.send(headers)
    print('send ok')
    res = b""
    while 1:
        msg = client.recv(65535)
        # print(len(msg) / 8)
        print('recv ok')
        if not msg:
            break
        res += msg

    # print(res.decode())
    res = res.decode()
    res_list = res.split('\r\n\r\n', 1)

    html = res_list[1]

    import os
    dir_name = os.path.dirname(__file__)
    root_dir = os.path.dirname(dir_name)
    download_dir = os.path.join(root_dir, 'download')
    # jpg_name = dir_name + '/' + '3_1.jpeg'

    jpg_name = os.path.join(download_dir, '{}.html'.format(name))
    with open(jpg_name, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    for i in range(10):
        i = str(i)
        get(i)

```
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