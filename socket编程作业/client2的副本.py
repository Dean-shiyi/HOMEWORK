# 写一个socket用来请求百度网页,并把请求下来的报文体部分保存



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