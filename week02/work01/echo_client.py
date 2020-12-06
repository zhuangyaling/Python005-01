import socket
import os
from pathlib import *
HOST = 'localhost'
PORT = 9999
p = Path(__file__)
BASE_DIR = p.resolve().parent

def echo_client():
    '''Echo Server 的Client端'''
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    while True:
        inp = input('>>>').strip() 
        path = os.path.join(BASE_DIR,inp)    #路径拼接
        filename = os.path.basename(path)
        file_size = os.stat(path).st_size
        file_info = '%s|%s'%(filename,file_size)
        s.sendall(bytes(file_info,'utf8'))
        f = open(path, 'rb')
        has_sent = 0
        while has_sent != file_size:
            data = f.read(1024)
            s.sendall(data)
            has_sent +=len(data)
        f.close()
        print('上传成功！！！！')
    s.close()

if __name__ == '__main__':
    echo_client()