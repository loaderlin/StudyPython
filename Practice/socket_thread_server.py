
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

# 自定义线程类
class FileTransferHandler(Thread):
    def __init__(self, client, data):
        super().__init__()
        self.client = client
        self.data = data
    
    def run(self):
        my_dict = {}
        my_dict['filename'] = 'data.jpg'
        # JSON 是纯文本不能携带二进制数据
        # 所以图片的二进制数据要处理成base64编码
        my_dict['filedata'] = self.data
        json_str = dumps(my_dict)
        self.client.send(json_str.encode('utf-8'))
        self.client.close()

def start_server():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('127.0.0.1', 6789))
    server.listen(521)
    print('服务器启动开始监听')
    with open('data.jpg', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        FileTransferHandler(client, data).start()

if __name__ == '__main__':
    start_server()

