class Login:
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
                    log = line.strip().split(',')
                    if log[0] == logusr and log[1] == passusr:
                        found = True
                        print("User found... logging in")
                        break
                if not found:
                    print("Login or password incorrect, please try again:")

    def create(self):
        loginc = input("Enter your username: ")
        passwordc = input("Enter your password: ")
        passcheck = input("Enter your password again: ")
        while passwordc != passcheck:
            passcheck = input("Username does not match, try again:")
        with open("userdata.txt", "a") as f:
            f.write(f"{loginc},{passwordc}\n")
        self.login()
p1 = Login()