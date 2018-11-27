class Listener:
    def __init__(self, server, conn, address):
        self.server = server
        self.connection = conn
        self.address = address

    def listen(self):
        while True:
            data = self.connection.recv(1024)
            self.server.process_message(self, data.decode('UTF-8'))
            print(data.decode('UTF-8'))
            if not data:
                break
        self.connection.close()

    # todo: timestamp, user, ??message entity??
    def receive_message(self, text):
        print('sending data')
        self.connection.send(str(text).encode())
