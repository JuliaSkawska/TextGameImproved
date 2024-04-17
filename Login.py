import mysql.connector

class Login:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="UserLogin"
        )
        self.login()

    def login(self):
        found = False
        print("\nWelcome, let's try to log you in :D\n")

        while not found:
            logusr = input("Enter your username: ")
            passusr = input("Enter your password: ")

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (logusr, passusr))
            row = cursor.fetchone()

            if row:
                found = True
                print("User found... logging in")
            else:
                print("Login or password incorrect, please try again:")

p1 = Login()
