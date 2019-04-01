# 书写一个socket服务器和客户端代码,要求客户端读取一个jpg或者png的媒体文件,
# 然后发送给服务器,服务器接受并保存在磁盘上面(位置随意)


# 客户端代码
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




