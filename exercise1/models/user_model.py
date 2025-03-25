import sqlite3
import os

class UserModel:
    def __init__(self):
        self.db_name = 'users.db'
        self.init_db()
        
    def init_db(self):
        if not os.path.exists(self.db_name):
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute('''
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')
            conn.commit()
            conn.close()
            
    def get_all_users(self): 
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('SELECT * FROM users')
        users = c.fetchall()
        conn.close()
        return users
        
    def add_user(self, name, email):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        conn.close()
        
    def delete_user(self, id):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('DELETE FROM users WHERE id = ?', (id,))
        conn.commit()
        conn.close()
