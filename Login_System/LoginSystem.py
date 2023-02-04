"""
Username and Password Database
Libraries needed "pip install <>"
- sql
- hashlib

Author - Anderson Jolly
"""
import sqlite3
import hashlib

DATABASE_NAME = "userdata.db"


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS userdata (
id INTEGER PRIMARY KEY,
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL,
clearance INTEGER NOT NULL)
""")

    def establishConnection(self):
        return self.connection, self.cursor

    def createUser(self, clearance: str, username: str, password: str):
        password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute("INSERT INTO userdata (username, password, email) VALUES (?, ?, ?)",
                            (username, password, clearance))
        self.connection.commit()

    def getAll(self):
        return self.cursor.execute("""SELECT * FROM userdata""").fetchall()

    def removeUser(self, id: int):
        self.cursor.execute("DELETE FROM userdata WHERE id= '%d'" % id)
        self.connection.commit()

    def deleteAll(self):
        self.cursor.execute("""DELETE FROM userdata""")
        self.connection.commit()

    def authenticateUser(self, username, password):
        password = hashlib.sha256(password).hexdigest()
        #print(username, password)
        message = "SELECT * FROM userdata WHERE username = '"+username+"' AND password = '"+password+"'"
        #print(message)
        self.cursor.execute(message)
        self.connection.commit()
        result = self.cursor.fetchall()
        if result:
            print(result[0])
            return True
        else:
            print("fucked")
            return False

db = Database()
#db.createUser(1", "psyaj3", "password")
db.authenticateUser("psyaj3", "password".encode())
print(db.getAll())
