# 书写一个socket服务器和客户端代码,要求客户端读取一个jpg或者png的媒体文件,
# 然后发送给服务器,服务器接受并保存在磁盘上面(位置随意)

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