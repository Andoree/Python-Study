import random


class Listener:

    def __init__(self, server, connection, address, hp):
        self.server = server
        self.connection = connection
        self.address = address
        self.hp = hp
        data = self.connection.recv(1024)
        self.username = data.decode('UTF-8')

    def check_game_end(self):
        if self.hp.value <= 0:
            self.connection.send('you lost!'.encode)
            # todo: notify server and on server notify another player

    def get_damage(self, damage):
        if damage:
            self.hp.value -= damage
            self.check_game_end()
            s = 'you got {} damage\nyour current hp is {}' \
                .format(damage, self.hp.value)
            self.connection.send(s.encode())
            return self.hp.value
        else:
            self.connection.send('enemy missed!\n'
                                 'your current hp is {:d}'
                                 .format(self.hp.value).encode())

    def process_hit(self, hit_power):
        value = random.random()
        return value < 1 / hit_power

    def player_iteration(self):
        data = self.connection.recv(1024)
        hit_power = Listener.validate(data)
        if hit_power != -1:
            if self.process_hit(hit_power):
                return int(hit_power)
            else:
                self.connection.send('Miss!'.encode())
        return False

    @staticmethod
    def validate(data):
        if not data.isdigit():
            return None
        data = int(data)
        if 0 < data < 10:
            return data
