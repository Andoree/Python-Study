import socket
import multiprocessing as mp
from time import strftime, gmtime

import pytest


class Client:
    address = 'localhost'
    port = 9090

    def __init__(self):
        self.socket = socket.socket()

    def listen_server(self):
        while True:
            data = self.socket.recv(1024)
            parts = data.decode('UTF-8').split('\n')
            print('author : ' + parts[0] + '\n' + parts[1] + '\n' + parts[2])
            print('enter message text')

    def connect(self):
        self.socket.connect((Client.address, Client.port))
        print('after connect:', self.socket)
        print('connected to server!')
        thread = mp.Process(target=self.listen_server)
        thread.start()
        username = input('Enter username:\n')
        self.socket.send(username.encode())
        while True:
            self.input_message()

    def input_message(self):
        message_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        text = input('enter message text\n')
        print('Вы :\n%s\n%s' % (text, message_time))
        self.socket.send(text.encode())


def main():
    client = Client()
    client.connect()


if __name__ == '__main__':
    main()
