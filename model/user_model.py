import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


class User_model():
    def __init__(self):
        try:
            self.conn=sqlite3.connect('demo.db')
            self.cursor=self.conn.cursor()
        except Exception as e:
            return f" db not connect {e}"
    
    def user_signup_logic(self,data):
        try:
            self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        name TEXT
                        password TEXT
                    )
                """)

            username = data.get('username')
            email = data.get('email')
            name = data.get('name')
            password = data.get('password')

            hashed_password = generate_password_hash(password, method='scrypt')
            

            self.cursor.execute("""
                    INSERT INTO users (username, email, name, password)
                    VALUES (?, ?, ?, ?)
                """, (username, email, name, hashed_password))

            self.conn.commit()
            self.conn.close()


            return f"signup successfully of username is {username} and email is {email} "
        
        except sqlite3.IntegrityError as e:
            return f"user already exists {e}"

        except Exception as e:
            return f"signup error {e}"


    def user_login_logic(self,data):
        try:
            username = data.get('username')
            password = data.get('password')

            self.cursor.execute("SELECT password FROM users WHERE username = ? ", (username,))
            result = self.cursor.fetchone()

            if result:
                stored_hash = result[0]
                if check_password_hash(stored_hash, password):
                    return f"Login successful for {username}"
                else:
                    return "Invalid password"
            else:
                return "User not found"
        except Exception as e:
            return f"login user error {e}"
             


    def user_getall_logic(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            rows = self.cursor.fetchall()
            self.conn.close()
            return rows
        except Exception as e:
            return f"get_users() failed: {e}"
        
    def user_update_logic(self,data):
        try:
            
            id = data.get('id')
            username = data.get('username')
            email = data.get('email')
            name = data.get('name')
            password = data.get('password')

            hashed_password = generate_password_hash(password, method='scrypt')

            self.cursor.execute("""
                UPDATE users 
                SET username = ?, email = ?, name = ?, password = ?
                WHERE id = ?
            """, ( username, email,name, hashed_password, id
               
            ))

            self.conn.commit()

            if self.cursor.rowcount > 0:
                return f"User with id {id} updated successfully "


            return f"update logic id = {id}"
        
        except sqlite3.IntegrityError as e:
            return f"user already exit {e}"
        except:
            return "user update error"
    
    def user_delete_logic(self,id):
        try:
            self.cursor.execute(f"DELETE from users WHERE id = ?",(id,))

            self.conn.commit()

            if self.cursor.rowcount > 0:
                return "User deleted successfully"
            else:
                return "User not exists"

        except Exception as e:
            return f"Delete user error {e}"
