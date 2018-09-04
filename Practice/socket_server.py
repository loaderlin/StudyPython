from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def start_server():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('127.0.0.1', 6789)) # 同一时间在同一个端口上只能绑定一个服务否则报错
    server.listen(521) # 连接队列的大小
    print('服务器启动开始监听')
    while True:
        Client, addr = server.accept()
        print(str(addr) + '连接到了服务器')
        Client.send(str(datetime.now()).encode('utf-8'))
        Client.close()

if __name__ == '__main__':
    start_server()
