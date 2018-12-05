import multiprocessing as mp
import socket
from ctypes import c_int
from time import gmtime, strftime

from task_1.listener import Listener


class Server:
    def __init__(self, manager):
        self.server_socket = socket.socket()
        self.server_socket.bind(('', 9090))
        self.server_socket.listen(2)
        self.listeners = manager.list()
        self.counter = 0

    def launch_listener(self, conn, address, listener_number):
        listener = Listener(self, conn, address, listener_number)
        self.listeners.append(listener)
        listener.listen()

    def start(self):

        while True:
            conn, address = self.server_socket.accept()
            listener_number = mp.Value(c_int)
            listener_number = self.counter
            self.counter += 1
            thread = mp.Process(target=self.launch_listener,
                                args=(conn, address, listener_number))
            thread.start()

    def process_message(self, sender, username, text):
        message_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        for listener in self.listeners:
            if listener != sender:
                listener.receive_message(username, text, message_time)


def main():
    manager = mp.Manager()
    server = Server(manager)
    server.start()


if __name__ == '__main__':
    main()
