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
        self.connection = sqlite3.connect(DATABASE_NAME, check_same_thread=False)
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

    def createUser(self, username: str, password: str, clearance: int):  # register a user
        password = hashlib.sha256(password).hexdigest()  # hashes password for storage
        self.cursor.execute("SELECT * FROM userdata WHERE username=? AND clearance =?",
                            (username, clearance))  # Checking if user exists

        # cant a user with the same name and access level
        self.connection.commit()
        result = self.cursor.fetchone()  # fetches the next row from the database
        if result is not None:
            # person exists so fail
            return False
        else:  # Add user to DB
            self.cursor.execute("INSERT INTO userdata (username, password, clearance) VALUES (?, ?, ?)",
                                (username, password, clearance))
            self.connection.commit()
            return True

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
        message = "SELECT * FROM userdata WHERE username=? AND password =?", (
            username, password)  # redundant variable now
        self.cursor.execute("SELECT * FROM userdata WHERE username=? AND password =?",
                            (username, password))  # sends SQL query
        self.connection.commit()
        result = self.cursor.fetchone()  # fetches the next row from the database
        if result != None:
            print(result)
            return True
        else:
            print("ERROR: NOT FOUND")
            print(username, password)  # debugging print statement
            return False

# db = Database()
# db.createUser(1", "psyaj3", "password")
# db.createUser("LEVEL 1","psyaj3","password".encode())
# print(db.authenticateUser("psyaj3", "password".encode()))
# print(db.getAll())
