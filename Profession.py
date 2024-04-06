class Profession:
    def __init__(self, health, magicres, phyres, crit, dodge):
        self.health = health
        self.magicres = magicres
        self.phyres = phyres
        self.crit = crit
        self.dodge = dodge
        self.cheal = health
        self.mr = magicres
        self.pmr = phyres
        self.cri = crit
        self.skills = []  # Define the skills attribute

    def current(self, cheal, mr, pr, cri):
        self.cheal = cheal
        self.mr = mr
        self.pr = pr
        self.cri = cri

    def info(self):
        print('{:*^50}'.format('Character Info:'))
        print(f"Health: {self.cheal}/{self.health}\nMagical Resistance: {self.magicres}\nPhysical Resistance: {self.phyres}\nCritical hit chance: {self.crit}%\nSkills:")
        for skill in self.skills:
            print(f"- {skill['sname']}: {skill['typ']}, {skill['dmbase']} base damage")
        print('{:*^50}'.format(''))

    def add_skill(self, sname, typ, dmbase):
        self.skills.append({'sname': sname, 'typ': typ, 'dmbase': dmbase})  # Update keys here
    def __str__(self):
        return self.__class__.__name__

class PlayerCharacter():
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
        self.character = None
    def ChooseProfession(self, profession):
        if profession == "alchemist":
            self.character = Alchemist()
        elif profession == "warrior":
            self.character = Warrior()
        elif profession == "thief":
            self.character = Thief()
        elif profession == "mage":
            self.character = Mage()
    def DisplayInfo(self):
        print(f"Character Name: {self.name}")
        print(f"Profession: {self.profession}")
        if self.character:
            self.character.info()
        else:
            print("No character chosen yet.")

    def current(self, cheal, mr, pr, cri):
        if self.character:
            self.character.current(cheal, mr, pr, cri)
class Warrior(Profession):
    def __init__(self):
        super().__init__(health=80, magicres=20, phyres=20, crit=20, dodge=10)
        self.skills=[]
        self.add_skill("Sword Strike", "Physical", 20)
        self.add_skill("Bloody Sacrifice", "Magical", 15)
        self.add_skill("Crushing Blow", "Physical", 40)

class Thief(Profession):
    def __init__(self):
        super().__init__(health=50, magicres=10, phyres=5, crit=40, dodge=20)
        self.skills=[]
        self.add_skill("Swift Strike", "Physical", 10)
        self.add_skill("Stab in the gut", "Physical", 15)
        self.add_skill("Shadow cloak", "Magial", 10)

class Mage(Profession):
    def __init__(self):
        super().__init__(health=40, magicres=15, phyres=5, crit=5, dodge=5)
        self.skills=[]
        self.add_skill("Fire Blast", "Magical", 20)
        self.add_skill("Stormy Weave", "Magical", 15)
        self.add_skill("Smoothing Rain", "Magical", 40)

class Alchemist(Profession):
    def __init__(self):
        super().__init__(health=50, magicres=10, phyres=10, crit=10, dodge=10)
        self.skills=[]
        self.add_skill("Acidic Potion", "Physical", 20)
        self.add_skill("Explosive Potion", "Physical", 20)
        self.add_skill("Soothin Potion", "Magical", 5)
def UserInput(text, options):
    sense = False
    while not sense:
        res = input(text)
        res = res.strip()
        res = res.lower()
        if res in options:
            sense = True
        else:
            print("Make sure you wrote the correct prompt :D")
    return res


def CreateCharacter():
    check = "no"
    while check == "no":
        name = input("Name your character: ")
        check = UserInput("Are you sure [Yes/No]: ", ["yes", "no"])

    print('{:*^50}'.format('Alchemist:'))
    Alchemist().info()
    print('{:*^50}'.format('Warrior:'))
    Warrior().info()
    print('{:*^50}'.format('Thief:'))
    Thief().info()
    print('{:*^50}'.format('Mage:'))
    Mage().info()

    classes = ["alchemist", "warrior", "thief", "mage"]

    pc = UserInput("Please choose your profession [Alchemist/Warrior/Thief/Mage]: ", classes)

    player = PlayerCharacter(name, pc)
    player.ChooseProfession(pc)
    return player

player=CreateCharacter()
player.DisplayInfo()
