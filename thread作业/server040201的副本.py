# 书写一个类似于百度的网站服务器,能够使用普通浏览器访问,只用返回简单的hello world即可

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('0.0.0.0', 35642)    # 0.0.0.0 表示内网可以访问
server.bind(server_addr)
server.listen(10)



while 1:
    conn, conn_addr = server.accept()
    msg = conn.recv(65535)

    return_msg = '''
    HTTP/1.1 200 OK\r\n
    \r\n
    Helloworld
    '''
    conn.send(return_msg.encode())


# server.close()





