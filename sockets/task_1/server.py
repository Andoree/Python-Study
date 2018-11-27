import socket
import threading as td
from task_1.listener import Listener


class Server:

    def __init__(self):
        self.server_socket = socket.socket()
        self.server_socket.bind(('', 9090))
        self.server_socket.listen(2)
        #   self.manager = Manager()
        self.listeners = []

    def create_connection(self, conn, address, listeners):
        print(len(listeners))
        listener = Listener(self, conn, address)
        print('adding listener:')
        print(listener)
        listeners.append(listener)
        print(len(listeners))
        listener.listen()

    def start(self):
        print('au')
        while True:
            conn, address = self.server_socket.accept()
            print('accepted!')
            print(conn, address)
            thread = td.Thread(target=self.create_connection,
                               args=(conn, address, self.listeners))
            thread.start()

    # todo: timestamp and user
    def process_message(self, sender, text):
        for listener in self.listeners:
            if listener != sender:
                listener.receive_message(text)


def main():
    server = Server()
    server.start()


if __name__ == '__main__':
    main()
