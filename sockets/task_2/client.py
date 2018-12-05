import socket


class Client:
    address = 'localhost'
    port = 9090

    def __init__(self):
        self.socket = socket.socket()

    @staticmethod
    def validate_hit_power(hit_power):
        if not hit_power.isdigit():
            print('power must be number!\nFor example, 4')
            return False
        hit_power = int(hit_power)
        if hit_power < 1 or hit_power > 9:
            print('power must be greater than 0\n'
                  'and less than 10')
            return False
        return True

    def connect(self):
        self.socket.connect((Client.address, Client.port))
        username = input('Enter your username please\n')
        self.socket.send(username.encode())
        priority = self.socket.recv(64).decode('UTF-8')
        if priority == '1':
            game_state = self.socket.recv(2048).decode('UTF-8')
            print(game_state)
        while True:
            hit_power = input('enter hit power\n')
            if Client.validate_hit_power(hit_power):
                self.socket.send(hit_power.encode())
                result = self.socket.recv(2048).decode('UTF-8')
                print(result+ '\n-----------')
                result = self.socket.recv(2048).decode('UTF-8')
                print(result+ '\n------------')


def main():
    client = Client()
    client.connect()


if __name__ == '__main__':
    main()
