import string
class Login:
    def logis(self, username, ty):
        while any(char in string.whitespace for char in username):
            print("Whitespace characters are not allowed, please choose a different name:")
            if ty == 'l':
                username = input("Enter your username:")
            else:
                username = input("Enter your password:")
        return username

    def __init__(self):
        logcheck = False

        while logcheck == False:
            check = input("Login[L]/Create new account[C]:")
            check = check.replace(" ", "")
            if check == "L" or check == "l":
                self.login()
                logcheck = True
            elif check == "C" or check == "c":
                self.create()
                logcheck = True
            else:
                print("please input correct values")

    def login(self):
        found = False
        print("\nWelcome, lets try to log you in :D\n")

        while not found:
            logusr = input("Enter your username: ")
            passusr = input("Enter your password: ")

            with open("userdata.txt", 'r') as usr:
                for line in usr:
                    log = line.strip().split('\t')
                    if log[0] == logusr and log[1] == passusr:
                        found = True
                        print("User found... logging in")
                        break
                if not found:
                    print("Login or password incorrect, please try again:")

    def create(self):
        exist = False
        loginc = input("Enter your username: ")
        passwordc = input("Enter your password: ")
        passcheck = input("Enter your password again: ")
        loginc = self.logis(loginc, 'l')
        passwordc = self.logis(passwordc, 'p')

        while passwordc != passcheck:
            passcheck = input("Passwords do not match, try again: ")

        with open("userdata.txt", "r") as f:
            for line in f:
                usrexists = line.strip().split('\t')
                if usrexists[0] == loginc:
                    print("This username is already taken, please choose another one")
                    exist = True

        if not exist:
            with open("userdata.txt", "a") as f:
                f.write(f"{loginc}\t{passwordc}\n")
                print("Account created successfully!")
            self.login()
        else:
            self.create()
p1 = Login()
