# Chapter 5: The OOP Labyrinth
# The Final Chamber: Confronting the Class Chimera
# This program is a system that uses multiple classes
# to be like an RPG game in which characters can
# engage in quests, navigate dungeons, and battle enemies.
# The concepts polymorphism, encapsulation, and inheritance
# are used.

# Step 1: Designing the Foundation Classes
class Character:
    def __init__(self, name, health, strength):
        self._name = name
        self._health = health
        self._strength = strength
        self._inventory = []

    def attack(self, target):
        damage = self._strength
        target._health -= damage
        return f"{self._name} attacks {target._name} for {damage} damage!"

    def defend(self, damage):
        self._health -= damage // 2
        return f"{self._name} defends and takes {damage // 2} damage!"

class Weapon:
    def __init__(self, name, damage_points):
        self._name = name
        self._damage_points = damage_points

class Armor:
    def __init__(self, name, defense_rating):
        self._name = name
        self._defense_rating = defense_rating

# Step 2: Implementing Inheritance and Polymorphism
# Creating subclasses that inherit from Character and
# override the attack() method
class Warrior(Character):
    def attack(self, target):
        damage = self._strength + 5
        target._health -= damage
        return f"{self._name}, the Warrior, strikes {target._name} with a sword for {damage} damage!"

class Mage(Character):
    def attack(self, target):
        damage = self._strength + 3
        target._health -= damage
        return f"{self._name}, the Mage, casts a spell on {target._name} for {damage} damage!"

class Rogue(Character):
    def attack(self, target):
        damage = self._strength + 4
        target._health -= damage
        return f"{self._name}, the Rogue, sneaks behind {target._name} and deals {damage} damage!"

# Step 3: Integrating the System
# Other classes, each with distinct attributes and methods,
# so that characters can undertake quests and navigate dungeons
class Dungeon:
    def __init__(self, name, difficulty_level, enemies):
        self._name = name
        self._difficulty_level = difficulty_level
        self._enemies = enemies

    def enter(self, character):
        for enemy in self._enemies:
            result = character.attack(enemy)
            print(result)
            if enemy._health <= 0:
                print(f"{enemy._name} is defeated!")

class Quest:
    def __init__(self, name, objective):
        self._name = name
        self._objective = objective

    def start(self, character):
        print(f"{character._name} begins the quest: {self._name}")
        print(f"Objective: {self._objective}")
        return f"{character._name} has completed the quest!"

# Step 4: Confronting the Class Chimera
# simulates an RPG game with main-method-like code
if __name__ == "__main__":
    warrior = Warrior("Aragorn", 100, 15)
    mage = Mage("Gandalf", 80, 12)
    rouge = Rogue("Legolas", 90, 14)

    orc = Character("Orc", 50, 10)
    troll = Character("Troll", 70, 12)

    dungeon = Dungeon("Moria", 3, [orc, troll])

    dungeon.enter(warrior)
    dungeon.enter(mage)
    dungeon.enter(rouge)

    quest = Quest("Destroy the One Ring", "Throw the ring into Mount Doom")
    print(quest.start(warrior))