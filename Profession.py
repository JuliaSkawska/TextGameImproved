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
        print('{:*^50}'.format('END'))

    def add_skill(self, sname, typ, dmbase):
        self.skills.append({'sname': sname, 'typ': typ, 'dmbase': dmbase})  # Update keys here

class Warrior(Profession):
    def __init__(self):
        super().__init__(health=80, magicres=20, phyres=20, crit=20, dodge=10)
        self.skills=[]
        self.add_skill("Sword Strike", "Physical", 20)
        self.add_skill("Bloody Sacrifice", "Magical", 15)
        self.add_skill("Crushing Blow", "Physical", 40)

class Temp(Profession):
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

x = Alchemist()
x.info()
