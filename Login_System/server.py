"""
Server for login database
Libraries needed "pip install <>"
- sql
- hashlib
- socket
- Threading

Author - Anderson Jolly
"""
import socket
import threading
from LoginSystem import Database

# SERVER ACTIONS
LOGIN = 0
ADD_USER = 1


class Server:
    def __init__(self, name: str, port: int):
        self.name = name
        self.port = port
        self.db = Database()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((name, port))
        self.server.listen()

    # TODO is there a better way to do this????
    def handleConnection(self, client):  # Takes in the first command the client and decides what to do
        action = int(client.recv(1024).decode())
        client.send("Action Received".encode())
        if action == LOGIN:
            self.login(client)
        elif action == ADD_USER:
            self.addUser(client)

    def login(self, client):
        username = client.recv(1024).decode()  # decodes and retrieves the username

        client.send("Recv username".encode())

        password = client.recv(1024).decode()  # decodes and retrieves the password
        if self.db.authenticateUser(username, password.encode()):
            client.send("0".encode())  # Login successful
        else:
            client.send("1".encode())  # Login Failed

    def acceptConnection(self):  # Thread to accept connections
        while True:
            client, addr = self.server.accept()
            threading.Thread(target=self.handleConnection, args=(client,)).start()

    def addUser(self, client):
        username = client.recv(1024).decode()  # decodes and retrieves the username
        client.send("Recv username".encode())

        password = client.recv(1024).decode()  # decodes and retrieves the password
        client.send("Recv password".encode())

        access = int(client.recv(1024).decode())  # decodes and retrieves the access level
        client.send("Recv access level".encode())

        #  Hanging HERE ----------------------------------

        if self.db.createUser(username, password.encode(), access):  # calls database to add user
            client.send("0".encode())   # success
        else:
            client.send("1".encode())  # fail


server = Server("localhost", 9999)
server.acceptConnection()
