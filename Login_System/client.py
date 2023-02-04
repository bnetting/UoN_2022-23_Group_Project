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


def establishClient(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    message = client.recv(1024).decode()  ## recieve username
    username = input(message)
    client.send(username.encode())  # send username

    message = client.recv(1024).decode()  # recieve password
    password = input(message)
    client.send(password.encode())  # send password

    message = client.recv(1024).decode()  ##get answer
    print(message)
    message = client.recv(1024).decode()  ##get answer
    print(message)

    print(username, password)

    message = client.recv(1024).decode()  ##get answer
    print(message)


establishClient("localhost", 9999)
