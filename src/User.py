class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add(self, db):
        users = db.get_usernames()
        if self.username not in users:
            db.add_user(self.username, self.password)
        else:
            raise TypeError('User already exists')
