# 写一个socket用来请求百度网页,并把请求下来的报文体部分保存

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


