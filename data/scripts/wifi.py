import socket


class Server(socket.socket):
    def __init__(self):
        super().__init__()
        self.bind(("", 9090))
        self.listen(1)
        self.connect, self.addres = self.accept()
        self.pos_x = 0
        self.pos_y = 0
        self.blocks = []
        self.data = ""

    def update_connect(self):
        self.data = self.recv(1024)
        self.send(bytes(f"{self.data}", encoding="utf-8"))


class Connect(socket.socket):
    pass
