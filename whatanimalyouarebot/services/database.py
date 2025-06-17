import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('data/bot.db')
        self.create_tables()
    
    def create_tables(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            animal TEXT
        )""")
        self.conn.commit()
    
    def user_exists(self, user_id):
        pass
    
    def add_user(self, user_id, name):
        pass
    
    def get_user_animal(self, user_id):
        pass
