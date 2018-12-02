class Listener:
    def __init__(self, server, conn, address):
        self.server = server
        self.connection = conn
        self.address = address

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
        print('sending data')
        self.connection.send(str(username + '\n' + text + '\n' + message_time).encode())
