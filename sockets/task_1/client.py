import socket
import multiprocessing as mp


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

    def connect(self):
        self.socket.connect((Client.address, Client.port))
        print('connected to server!')
        thread = mp.Process(target=self.listen_server)
        thread.start()
        username = input('Enter username:\n')
        self.socket.send(username.encode())
        while True:
            text = input()
            self.socket.send(text.encode())


def main():
    client = Client()
    client.connect()


if __name__ == '__main__':
    main()
