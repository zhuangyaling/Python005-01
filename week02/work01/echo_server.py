import socket
import os
from pathlib import *

HOST = 'localhost'
PORT = 9999
p = Path(__file__)
BASE_DIR = p.resolve().parent
def echo_server():
    '''Echo Server 的 Server'''
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #对象s绑定到指定的主机和端口上
    s.bind((HOST,PORT))
    #只接受1个连接
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print(addr)
        while True:
            data = conn.recv(1024)       #开始接收
            filename,file_size = str(data,'utf8').split('|')
            ya = BASE_DIR.joinpath('ya')
            if not ya.is_dir():
                Path.mkdir(ya)
            path = os.path.join(ya,filename)
            file_size = int(file_size)

            f = open(path,'ab')
            has_receive = 0
            while has_receive != file_size:
                data = conn.recv(1024)
                f.write(data)
                has_receive +=len(data)
            f.close()
    conn.close()
    s.close()
if __name__ == '__main__':
    echo_server()