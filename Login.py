import mysql.connector

class LoginRegister:
    '''
        Allows user to login or register, as well as add that user to a database
    '''
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="UserLogin"
        )

        while True:
            choice = input("Would you like to login or register?: ").strip().lower()
            if choice == "login":
                self.username = self.login()
                if self.username:
                    break
            elif choice == "register":
                self.username = self.register()
                break

    def login(self):
        print("\nWelcome, let's try to log you in :D\n")

        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            cursor = self.conn.cursor()
            cursor.execute("SELECT username FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            if user:
                print("User found... logging in")
                return username
            else:
                print("Login or password incorrect, please try again:")
        return None

    def register(self):
        print("\nWelcome, let's create your new account\n")
        new_username = input("Enter a new username: ")
        new_password = input("Enter a new password: ")

        while True:
            new_password_confirmation = input("Enter your new password again: ")

            if new_password == new_password_confirmation:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (new_username, new_password))
                self.conn.commit()
                print("Your account has been created!\n")
                return self.login()
            else:
                print("Whoops, looks like something went wrong. Make sure your password matches.\n")
        return None

p=LoginRegister()
print(p.username)