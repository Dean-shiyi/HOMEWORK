

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