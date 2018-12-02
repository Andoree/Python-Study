import socket
import multiprocessing as mp


from task_2.listener import Listener


class Server:
    def __init__(self, manager):
        self.server_socket = socket.socket()
        self.server_socket.bind(('localhost', 9090))
        self.server_socket.listen(2)
        self.listeners = manager.list()
        self.game_is_going

    def create_listener(self, server, listeners, conn, address, hp):
        listener = Listener(server, conn, address, hp)
        listeners.append(listener)

    def start(self, manager):
        hp1 = manager.Value('hp1', 100)
        hp2 = manager.Value('hp2', 100)
        # todo: remove code duplicate
        conn, address = self.server_socket.accept()
        print('user connected')
        thread = mp.Process(target=self.create_listener,
                            args=(self, self.listeners, conn, address, hp1))
        thread.start()
        conn, address = self.server_socket.accept()
        thread.join()
        print('user connected')
        thread = mp.Process(target=self.create_listener,
                            args=(self, self.listeners, conn, address, hp2))
        thread.start()
        thread.join()
        for i in range(len(self.listeners)):
            self.listeners[i].connection.send(str(i).encode())
        while self.game_is_going:
            for i in range(len(self.listeners)):
                damage = self.listeners[i].player_iteration()
                hp = self.listeners[(i + 1) % 2].get_damage(damage)
                if hp:
                    self.listeners[i].connection.send('Nice shot!\nEnemy hp is {}'.format(hp).encode())


def main():
    manager = mp.Manager()
    # listeners = manager.list()
    server = Server(manager)
    server.start(manager)


if __name__ == '__main__':
    main()
