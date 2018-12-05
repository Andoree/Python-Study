class Listener:
    def __init__(self, server, conn, address, listener_number):
        self.server = server
        self.connection = conn
        self.address = address
        self.listener_number = listener_number
        self.username = ''

    def listen(self):
        data = self.connection.recv(1024)
        self.username = data.decode('UTF-8')
        while True:
            data = self.connection.recv(1024)
            self.server.process_message(self, self.username, data.decode('UTF-8'))
            if not data:
                break
        self.connection.close()

    def receive_message(self, username, text, message_time):
        self.connection.send(str(username + '\n' + text + '\n' + message_time).encode())

    def __eq__(self, other):
        return self.listener_number == other.listener_number
