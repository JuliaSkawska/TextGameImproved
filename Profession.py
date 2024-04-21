import random
def DodgeChance(min_to_hit,max_to_hit):
    result=random.randint(0,max_to_hit)
    if result>min_to_hit:
        return True
    else:
        return False
def user_input(prompt, options):
    '''
    :param prompt: text that is supposed to be displayed
    :param options: inputs that are considered correct
    :return: user input if correct
    '''
    while True:
        user_input = input(prompt)
        user_input = user_input.strip().lower()
        if user_input in options:
            break
        else:
            print("Make sure you wrote the correct prompt :D")
    return user_input

class Profession:
    def __init__(self, health, magical_resistance, physical_resistance, crit_chance, dodge):
        self.max_health = self.current_health = health
        self.magical_resistance = magical_resistance
        self.physical_resistance = physical_resistance
        self.critical_hit_chance = crit_chance
        self.dodge_chance = dodge
        self.skills = []

    def current(self, current_health):
        self.current_health = current_health

    def info(self):
        '''
        Print character information.
        '''
        print('{:*^50}'.format('Character Info:'))
        print(f"Health: {self.current_health}/{self.max_health}\nMagical Resistance: {self.magical_resistance}\nPhysical Resistance: {self.physical_resistance}\nCritical hit chance: {self.critical_hit_chance}%\nSkills:")
        for skill in self.skills:
            print(f"- {skill['name']}: {skill['type']}, {skill['base_damage']} base damage")
        print('{:*^50}'.format(''))

    def add_skill(self, name, skill_type, base_damage):
        '''
        Add a new skill to the character.
        :param name: Name of the skill
        :param skill_type: Type of the skill
        :param base_damage: Base damage of the skill
        '''
        self.skills.append({'name': name, 'type': skill_type, 'base_damage': base_damage})

    def __str__(self):
        '''
        Return class name.
        '''
        return self.__class__.__name__


class PlayerCharacter:
    def __init__(self, name, profession):
        '''
        Initialize a new PlayerCharacter object.
        :param name: Name of the player character.
        :param profession: Chosen profession of the player character.
        '''
        self.name = name
        self.character = None
        self.choose_profession(profession)

    def choose_profession(self, profession):
        '''
        Choose the profession for the player character.
        :param profession: Chosen profession of the player character.
        '''
        if profession == "alchemist":
            self.character = Alchemist()
        elif profession == "warrior":
            self.character = Warrior()
        elif profession == "thief":
            self.character = Thief()
        elif profession == "mage":
            self.character = Mage()

    def display_info(self):
        '''
        Display the information about the player character.
        '''
        print(f"Character Name: {self.name}")
        if self.character:
            self.character.info()
        else:
            print("No character chosen yet.")

    def current(self, current_health):
        '''
        Update the current health of the player character.
        '''
        if self.character:
            self.character.current(current_health)

class Warrior(Profession):
    def __init__(self):
        super().__init__(health=80, magical_resistance=20, physical_resistance=20, crit_chance=20, dodge=10)
        self.skills = []
        self.add_skill("Sword Strike", "Physical", 20)
        self.add_skill("Bloody Sacrifice", "Magical", 15)
        self.add_skill("Crushing Blow", "Physical", 40)

class Thief(Profession):
    def __init__(self):
        super().__init__(health=50, magical_resistance=10, physical_resistance=5, crit_chance=40, dodge=20)
        self.skills = []
        self.add_skill("Swift Strike", "Physical", 10)
        self.add_skill("Stab in the gut", "Physical", 15)
        self.add_skill("Shadow cloak", "Magical", 10)

class Mage(Profession):
    def __init__(self):
        super().__init__(health=40, magical_resistance=15, physical_resistance=5, crit_chance=5, dodge=5)
        self.skills = []
        self.add_skill("Fire Blast", "Magical", 20)
        self.add_skill("Stormy Weave", "Magical", 15)
        self.add_skill("Smoothing Rain", "Magical", 40)

class Alchemist(Profession):
    def __init__(self):
        super().__init__(health=50, magical_resistance=10, physical_resistance=10, crit_chance=10, dodge=10)
        self.skills = []
        self.add_skill("Acidic Potion", "Physical", 20)
        self.add_skill("Explosive Potion", "Physical", 20)
        self.add_skill("Soothing Potion", "Magical", 5)

def create_character():
    '''
    Creates a new PlayerCharacter object.

    Returns:
    PlayerCharacter: A new PlayerCharacter object.
    '''
    while True:
        name = input("Name your character: ")
        if user_input("Are you sure [Yes/No]: ", ["yes", "no"]) == "yes":
            break

    classes = ["alchemist", "warrior", "thief", "mage"]
    pc = user_input("Please choose your profession [Alchemist/Warrior/Thief/Mage]: ", classes)

    player = PlayerCharacter(name, pc)
    player.choose_profession(pc)
    return player

class Enemy():
    active_enemies = []
    def __init__(self, name, health, magicres, phyres, dodge, atype, actions):
        self.name = name
        self.health = health
        self.magicres = magicres
        self.phyres = phyres
        self.dodge = dodge
        self.atype = atype
        self.actions = actions
        Enemy.active_enemies.append(self)
    def status(self):
        print(f"{self.name} currently has {self.health} health left")
    def take_damage(self,damage,chance):
        if DodgeChance(self.dodge,chance)==True:
            self.health -= damage
            print(f"{self.name} has taken damage!\n{self.name} is now at {self.health} hp")
            if self.health <= 0:
                print(f"{self.name} has been defeated!")
                self.remove()
        else:
            print(f"{self.name} managed to dodge your attack")
    def take_action(self):#chooses one of x action for enemy to take
        threshold = len(self.actions)-1
        choice_index = random.randint(0, threshold)
        choice_function = self.actions[choice_index]
        choice_function()
    def remove(self):
        Enemy.active_enemies.remove(self)

#Example of Enemy subclass for testing
class Brute(Enemy):
    def __init__(self, name, health, magicres, phyres, dodge):
        actions = [self.attack, self.charge_attack, self.block]
        super().__init__(name, health, magicres, phyres, dodge, "Brute", actions)

    def attack(self):
        print(f"{self.name} attacks!")

    def charge_attack(self):
        print(f"{self.name} is preparing a charged attack!!!")

    def block(self):
        print(f"{self.name} is hiding behind a shield!")

# Testing
'''
brute1 = Brute("Goblin Warrior",20,5,5,5)
brute1.take_action()
brute1.take_damage(2,10)
'''

p1=create_character()
p1.display_info()

