import mysql.connector

class Login:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="UserLogin"
        )
        correct=False
        while not correct:
            choice=input("Would you like to login or register?: ")
            choice=choice.strip().lower()
            if choice=="login":
                self.login()
                correct=True
            elif choice=="register":
                self.register()
                correct=True

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
    def register(self):
        checkpass=False
        print("\nWelcome, let's create your new account\n")
        new_usr = input("Enter a new username: ")
        new_pass = input("Enter a new password: ")

        while not checkpass:
            new_pass2 = input("Enter your new password again: ")

            if new_pass==new_pass2:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (new_usr, new_pass))
                self.conn.commit()
                print("Your account has been added!")
                checkpass=True
            else:
                print("Whoops, looks like something went wrong, make sure your password matches")
        self.login()

p1 = Login()