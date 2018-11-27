import socket
import multiprocessing as mp
import time


class Client:
    address = 'localhost'
    port = 9090

    def __init__(self):
        self.socket = socket.socket()

    def listen_server(self):
        while True:
            data = self.socket.recv(1024)
            print('message : ' + data.decode('UTF-8'))

    def connect(self):
        self.socket.connect((Client.address, Client.port))
        print('connected to server!')
        thread = mp.Process(target=self.listen_server)
        thread.start()
        time.sleep(0.01)
        while True:
            # todo : message with timestamp and name
            text = input('Enter message text:\n')
            self.socket.send(text.encode())


def main():
    client = Client()
    client.connect()


if __name__ == '__main__':
    main()
