import sqlite3

from werkzeug.security import check_password_hash, generate_password_hash


class User_model:

    # constructur to connect to db, so when ever object is created, db get connect with backend

    def __init__(self):
        try:
            self.conn = sqlite3.connect("demo.db")
            self.cursor = self.conn.cursor()
        except Exception as e:
            return f" db not connect {e}"

    def user_signup_logic(self, data):
        print("user signup logic", data)
        try:
            self.cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        name TEXT
                        password TEXT
                    )
                """
            )

            username = data.get("username")
            email = data.get("email")
            name = data.get("name")
            password = data.get("password")
            if not all([username, email, password]):
                return "Missing required fields (username, email, or password)"

            hashed_password = generate_password_hash(password, method="scrypt")

            self.cursor.execute(
                """
                    INSERT INTO users (username, email, name, password)
                    VALUES (?, ?, ?, ?)
                """,
                (username, email, name, hashed_password),
            )

            self.conn.commit()
            self.conn.close()

            return (
                f"signup successfully of username is {username} and email is {email} "
            )

        except sqlite3.IntegrityError as e:
            return f"user already exists {e}"

        except Exception as e:
            return f"signup error {e}"
        finally:
            self.conn.close()

    # login logic and funtion data except data as arguments

    def user_login_logic(self, data):
        try:
            # get the username and password from the data and store in variables

            username = data.get("username")
            password = data.get("password")

            # execute the query to select the password for the given username

            self.cursor.execute(
                "SELECT password FROM users WHERE username = ? ", (username,)
            )

            # store query result in result variable

            result = self.cursor.fetchone()
            print("result", result, username, password)

            # if result is not empty then check the password with the stored password else return user not found

            if result:
                stored_hash = result[0]

                # check the password with the stored hash though check_password_hash method

                if check_password_hash(stored_hash, password):
                    return f"Login successful for {username}"
                else:
                    return "Invalid password"
            else:
                return "User not found"

        # if any exception occurs then return the error message

        except Exception as e:
            return f"login user error {e}"
        finally:
            self.conn.close()

    def user_getall_logic(self, data):
        try:
            username = data.get("username")

            # password = data.get('password')

            self.cursor.execute("SELECT * FROM users WHERE username = ? ", (username,))
            row = self.cursor.fetchone()
            print("row", row, username)
            if row:
                user_data = {
                    "id": row[0],
                    "username": row[1],
                    "email": row[2],
                    "name": row[3],
                    "password": row[4],
                }
            return user_data
        except Exception as e:
            return f"get_users() failed: {e}"
        finally:
            self.conn.close()

    # update logic

    def user_update_logic(self, data):
        try:
            # fetch all data from front-end

            id = data.get("id")
            username = data.get("username")
            email = data.get("email")
            name = data.get("name")
            password = data.get("password")

            # store in hash using method scrypt

            hashed_password = generate_password_hash(password, method="scrypt")

            # query to update users field

            self.cursor.execute(
                """
                UPDATE users 
                SET username = ?, email = ?, name = ?, password = ?
                WHERE id = ?
            """,
                (username, email, name, hashed_password, id),
            )

            # save commit

            self.conn.commit()

            # if some changes occur then the return successfull message

            if self.cursor.rowcount > 0:
                return f"User with id {id} updated successfully "

            # if nothing change then no filed change

            else:
                return f"No field changes"

        # Exception handler for many sqlite exception like dublicate username, username not exits

        except sqlite3.IntegrityError as e:
            return f"user already exit {e}"
        except:
            return "user update error"
        finally:
            self.conn.close()

    # user delete :- get api call from front-end through route and run query

    def user_delete_logic(self, id):
        try:
            # Exceute query to delete user

            self.cursor.execute(f"DELETE from users WHERE id = ?", (id,))

            self.conn.commit()

            # if user deleted successfully from db then return this success message
            if self.cursor.rowcount > 0:
                return "User deleted successfully"
            else:
                return "User not exists"

        # To handle exception occuring while delete user
        except Exception as e:
            return f"Delete user error {e}"
        # Close the db connection
        finally:
            self.conn.close()

    # fetch_all logic to for testing purpose , can view all user in postman

    def fetch_all(self):
        try:
            # fetcha all user from users table

            self.cursor.execute("SELECT * FROM users")
            rows = self.cursor.fetchall()
            return rows

        # handle exception while fetching users

        except Exception as e:
            return f"get_users() failed: {e}"

        # close the db connection

        finally:
            self.conn.close()
