import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('users.db')
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY ASC,
        username varchar(250) NOT NULL,
        password varchar(250) NOT NULL)
        """)

    def add_user(self, username, password):
        self.cur.execute('INSERT INTO users VALUES(NULL, ?, ?)', (username, password))
        self.con.commit()

    def get_usernames(self):
        self.cur.execute('SELECT username from users')
        users = self.cur.fetchall()
        usernames = set()
        for user in users:
            usernames.add(user['username'])
        return usernames
