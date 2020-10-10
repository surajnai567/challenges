import socket
import json
import pickle
import time
from threading import Thread

buffer_size = 10
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('localhost', 2222))

def send():
    while True:
        print('enter mess', end='\n')
        send_message = input()
        mess = f'{len(send_message)}'.ljust(buffer_size) + send_message
        soc.send(mess.encode())


def recieve():
    message = ''
    mes_len = ''

    new_msg = True
    while True:
        data = soc.recv(10)
        if new_msg:
            mes_len = int(data)
            new_msg = False

        message += data.decode(encoding='utf-8')
        if abs(len(message) - 10) == mes_len:
            print(message[buffer_size:], end='\n')
            new_msg = True
            mes_len = 0
            message = ''


s = Thread(target=send)
r = Thread(target=recieve)
s.start()
r.start()











