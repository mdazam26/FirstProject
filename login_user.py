import sqlite3


class Fetch():
    def __init__(self):
        try:

            self.conn=sqlite3.connect('demo.db')
            self.cursor=self.conn.cursor()
        except Exception as e:
           return f" db not connect {e}"
        

    def get_users(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            rows = self.cursor.fetchall()
            self.conn.close()
            return rows
        except Exception as e:
            return f"get_users() failed: {e}"
