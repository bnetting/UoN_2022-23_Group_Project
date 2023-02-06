"""
Client for login database
Libraries needed "pip install <>"
- sql
- hashlib
- socket
- Threading

Author - Anderson Jolly
"""
import sqlite3
import hashlib
import socket
import threading


class Client:
    def __init__(self, ip: str, port: int):
        self.name = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.name, self.port))

    def login(self, username: str, password: str, access: int):
        self.client.send("0".encode())  # Signal to server that you are logging in
        print(self.client.recv(1024).decode())

        self.client.send(username.encode())  # send username

        print(self.client.recv(1024).decode())
        self.client.send(password.encode())  # send password
        message = int(self.client.recv(1024).decode())
        if message == 0:
            print("Login Success")
            return True
        else:
            print("login Failed")
            return False

    def createUser(self, username: str, password: str, access: str):
        self.client.send("1".encode())  # signal to server you want to create a user
        print(self.client.recv(1024).decode())

        self.client.send(username.encode())  # sends the username
        print(self.client.recv(1024).decode())  # wants for feedback

        self.client.send(password.encode())  # send password
        print(self.client.recv(1024).decode())  # waits for feedback

        self.client.send(access.encode())  # send access level
        print(self.client.recv(1024).decode())  # wait for feedback

        message = int(self.client.recv(1024).decode())  # gets final response
        print(message)
        if message == 0:
            print("Added user")  # success
            return True
        else:
            print("Adding Failed")  # fail
            return False

    def close(self): #Sends a message to the server to gracefully close the connection
        exitMessage=""
        self.client.send("99".encode()) #Sends exit code
        exitMessage=(self.client.recv(1024).decode())
        while(exitMessage!="GOODBYE"): #Waits for server to respond with exit message
            exitMessage=(self.client.recv(1024).decode())
        print(exitMessage)#Prints correct exit message sent by the server
        self.client.close()#closes socket connection to the server

client = Client("localhost", 9999)
# client.login('psyaj3', "password", 1)
# client.login('psyaj3', "password", 1)
client.createUser('bob', 'bob1', "2")
client.createUser('bob2','bob12',"2")
client.close()

