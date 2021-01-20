import random

class Item:
    def __init__(self, weigth, worth, name):
        self.weight = weigth
        self.worth = worth
        self.name = name


class Potion(Item):
    def __init__(self, weight, worth, name):
        Item.__init__(self, weight, worth, name)

class HealthPotion(Potion):
    def __init__(self, weight, worth, regenerated_health, name):
        Potion.__init__(self, weight, worth, name)
        self.regenerated_health = regenerated_health

class Weapon(Item):
    def __init__(self, weight, worth, damage, name):
        Item.__init__(self, weight, worth, name)
        self.damage = damage

class Swort(Weapon):
    def __init__(self):
        Weapon.__init__(self, 10, 25, 15, "swort")


class Dagger(Weapon):
    def __init__(self):
        Weapon.__init__(self, 3, 15, 10, "dagger")

class Club(Weapon):
    def __init__(self):
        Weapon.__init__(self, 7, 7, 5, "club")

class Clothers(Item):
    def __init__(self, weight, worth, wp, name):
        Item.__init__(self, weight, worth, name)
        self.wp = wp

class Shoe(Clothers):
    pass

class Food(Item):
    def __init__(self, weight, worth, regenerated_health, name):
        Item.__init__(self, weight, worth, name)
        self.regenerated_health = regenerated_health

class Bread(Food):
    def __init__(self):
        Food.__init__(self, 4, 12, 20, "bread")

class Roll(Food):
    def __init__(self):
        Food.__init__(self, 2, 6, 10, "roll")

class Apple(Food):
    def __init__(self):
        Food.__init__(self, 3, 4, 13, "apple")

class Fish(Food):
    def __init__(self):
        Food.__init__(self, 4, 14, 30, "fish")

class Meat(Food):
    def __init__(self):
        Food.__init__(self, 5, 16, 30, "meat")

class Soup(Food):
    def __init__(self):
        Food.__init__(self, 7, 10, 15, "soup")

class Diamond(Item):
    def __init__(self):
        Item.__init__(self, 3, 100, "diamond")

class Writen_Book(Item):
    def __init__(self, name, content):
        Item.__init__(self, 3, 7, 'book:'+name)
        self.content = content

    def show_content(self):
        print(self.name + ':')
        print(self.content)

class Book(Item):
    def __init__(self):
        Item.__init__(self, 3, 7, '')
        self.content = ""

    def write_book(self):
        if self.name == '':
            self.name = input("name:")
        print(self.name + ':')
        self.content = input()

    def rename_book(self):
        self.name = input("name:")

    def show_content(self):
        print(self.name + ':')
        print(self.content)

class Mettal(Item):
    def __init__(self, weigth, worth, name):
        Item.__init__(self, weigth, worth, name)

class Gold(Mettal):
    def __init__(self):
        Mettal.__init__(self, 20, 50, "gold")

class Silver(Mettal):
    def __init__(self):
        Mettal.__init__(self, 17, 25, "silver")

class Iron(Mettal):
    def __init__(self):
        Mettal.__init__(self, 10, 10, "iron")

class Coal(Item):
    def __init__(self):
        Item.__init__(self, 4, 12, "coal")

class Tourch(Item):
    def __init__(self):
        Item.__init__(self, 3, 7, "tourch")

class Wood(Item):
    def __init__(self):
        Item.__init__(self, 5, 8, "wood")

class Stick(Item):
    def __init__(self):
        Item.__init__(self, 2, 2, "stick")

class Map(Item):
    def __init__(self, content):
        Item.__init__(self, 6, 15, "map")
        self.content = content

class Glass(Item):
    def __init__(self):
        Item.__init__(self, 8, 20, "glass")