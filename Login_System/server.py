"""
Server for login database
Libraries needed "pip install <>"
- sql
- hashlib
- socket
- Threading

Author - Anderson Jolly
"""
import hashlib
import socket
import threading
from LoginSystem import Database


def establishConnection(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    return server


host = establishConnection("localhost", 9999)
db = Database()


def handleConnection(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()  # decodes and retrieves the username
    c.send("Password: ".encode())
    password = c.recv(1024).decode()  # decodes and retrieves the password
    #password = hashlib.sha256(password).hexdigest()  # hash password

    c.send(("SERVER: hashed password" + username + " " + password + " ").encode())
    # connection, cursor = db.establishConnection()  # get connection to database
    c.send("SERVER: ESTABLISHED CONNECTION".encode())
    if db.authenticateUser(username, password):
        c.send("login successfully".encode())
    else:
        c.send("login failed".encode())


while True:
    client, addr = host.accept()
    threading.Thread(target=handleConnection, args=(client,)).start()
