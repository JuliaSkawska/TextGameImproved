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

    def current(self, cheal, mr, pr, cri):
        self.cheal = cheal
        self.mr = mr
        self.pr = pr
        self.cri = cri

    def info(self):
        print('{:*^50}'.format('Character Info:'))
        print(f"Health: {self.cheal}/{self.health}\nMagical Resistance: {self.magicres}\nPhysical Resistance: {self.phyres}\nCritical hit chance: {self.crit}%")
        print('{:*^50}'.format('END'))


class Warrior(Profession):
    def __init__(self):
        super().__init__(health=80, magicres=20, phyres=20, crit=20, dodge=0)

x = Warrior()
x.info()

x.current(10, 50, 30, 10)
x.info()