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

    
    def add_user(self,data):
        return f"add user logic{data}"

    # def update_user(self,id,data):
    #     try:
    #         username = data.get('username')
    #         email = data.get('email')
    #         self.cursor.execute(f"UPDATE users SET username={username}, email={email} WHERE id={data['id']}")
    
    #         if self.cursor.rowcount > 0:
    #             return "user updated successfully"
    #         else :
    #             return "Nothing to update"
        
    #     except Exception as e:
    #         return f"updating fails {e}"
