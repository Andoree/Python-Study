import socket
import multiprocessing as mp
from time import gmtime, strftime
from task_1.listener import Listener


class Server:

    def __init__(self, listeners):
        self.server_socket = socket.socket()
        self.server_socket.bind(('', 9090))
        self.server_socket.listen(2)
        #   self.manager = Manager()
        self.listeners = listeners

    def create_connection(self, conn, address):
        listener = Listener(self, conn, address)
        self.listeners.append(listener)
        listener.listen()

    def start(self):
        while True:
            conn, address = self.server_socket.accept()
            thread = mp.Process(target=self.create_connection,
                                args=(conn, address,))
            thread.start()

    def process_message(self, sender, username, text):
        message_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        for listener in self.listeners:
            if listener != sender:
                listener.receive_message(username, text, message_time)


def main():
    manager = mp.Manager()
    listeners = manager.list()
    server = Server(listeners)
    server.start()


if __name__ == '__main__':
    main()
