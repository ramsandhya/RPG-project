"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
from random import randint
import time

class bcolors:
    LIGHTGREEN = '\033[92m'
    RED = '\033[31m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.zombie_repellant = False
        self.prize_coins = 0

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def double_attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power * 2)
        time.sleep(1.5)

    def drunk_attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s, but falls and hurts himself/herself." % (self.name, enemy.name)
        enemy.receive_damage(self.power * 2)
        self.receive_damage(self.power - 2)
        time.sleep(4.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print bcolors.LIGHTGREEN + bcolors.BOLD + "%s has %d health and %d power." % (self.name, self.health, self.power) + bcolors.ENDC

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.zombie_killer = False
        self.armor = 0
        self.evade = 0
        self.drunk = False

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def receive_damage(self, points):
        hero_health = random.random()
        if hero_health < hero.evade:
            print "%s evaded %s's attack and received 0 damage" % (self.name, enemy.name)
        else:
            self.health -= points - self.armor
            print "%s received %d damage." % (self.name, points - self.armor)
        if self.health <= 0:
            hero.coins += self.prize_coins
            print "%s is dead." % (self.name)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.prize_coins = 5

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            hero.coins += self.prize_coins
            print "%s is dead. You looted %d coins from their body." % (self.name, self.prize_coins)

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.prize_coins = 6

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            hero.coins += self.prize_coins
            print "%s is dead. You looted %d coins from their body." % (self.name, self.prize_coins)

class Medic(Character):
    def __init__(self):
        self.name = "medic"
        self.health = 6
        self.power = 2
        self.prize_coins = 6

    def receive_damage(self, points):
        medic_health = random.random()
        if medic_health < 0.2:
            self.health -= points
            self.health += 2
            print "%s received %d damage, but recovered 2 health points!" % (self.name, points)
        else:
            self.health -= points
            print "%s received %d damage" % (self.name, points)

        if self.health <= 0:
            hero.coins += self.prize_coins
            print "%s is dead. You looted %d coins from their body." % (self.name, self.prize_coins)

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 1
        self.prize_coins = 10

    def receive_damage(self, points):
        shadow_health = random.random()
        if shadow_health < 0.1:
            self.health -= points
            print "%s received %d damage." % (self.name, points)
        else:
            print "%s evaded your attack and received 0 damage" % (self.name)

        if self.health <= 0:
            hero.coins += self.prize_coins
            print "%s is dead. You looted %d coins from their body." % (self.name, self.prize_coins)

class Toby(Character):
    def __init__(self):
        self.name = 'toby'
        self.health = 10
        self.power = -3
        self.zombie_killer = False
        self.prize_coins = 3

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            hero.coins += self.prize_coins
            print "%s is dead. You looted %d coins from their body." % (self.name, self.prize_coins)

class Lawrence(Character):
    def __init__(self):
        self.name = 'lawrence'
        self.health = 5
        self.power = 3
        self.zombie_killer = False
        self.prize_coins = 10

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        time.sleep(45)
        if self.health <= 0:
            hero.coins += self.prize_coins
            print "%s is dead. You looted %d coins from their body." % (self.name, self.prize_coins)



class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 6
        self.power = 2
        self.zombie_killer = False
        self.prize_coins = 1000000

    def receive_damage(self, points):
        if self.zombie_killer is True:
            self.health -= 100
            print "Hero has zombie killer! %s received 100 damage points!" % (self.name)
        else:
            self.health -= points
            self.health += 6
            print "%s received zero damage. He's already dead!" % (self.name)

        if self.health <= 0:
            hero.coins += self.prize_coins
            print "%s is dead. You looted %d coins from their body." % (self.name, self.prize_coins)

class Battle(object):
    def do_battle(self, hero, enemy):
        if hero.drunk is False:
            print "====================="
            print bcolors.HEADER + "Hero faces the %s" % enemy.name + bcolors.ENDC
            print "====================="
            while hero.alive() and enemy.alive():
                hero.print_status()
                enemy.print_status()
                time.sleep(1.5)
                print "-----------------------"
                print bcolors.UNDERLINE + "What do you want to do?" + bcolors.ENDC
                print "1. fight %s" % enemy.name
                print "2. do nothing"
                print "3. flee"
                print "> ",
                input = int(raw_input())
                if input == 1:
                    dbl_atk_prob = random.random()
                    if dbl_atk_prob < 0.2:
                        hero.double_attack(enemy)
                    else:
                        hero.attack(enemy)
                elif input == 2:
                    pass
                elif input == 3:
                    print "Goodbye."
                    exit(0)
                else:
                    print "Invalid input %r" % input
                    continue
                enemy.attack(hero)
            if hero.alive():
                print "You defeated the %s" % enemy.name
                return True
            else:
                print "YOU LOSE!"
                return False
        else:
            print "====================="
            print bcolors.HEADER + "Herbo feces thaaa %s" % enemy.name + bcolors.ENDC
            print "====================="
            while hero.alive() and enemy.alive():
                hero.print_status()
                enemy.print_status()
                time.sleep(1.5)
                print "-----------------------"
                print bcolors.UNDERLINE + "What you wa..... to do?" + bcolors.ENDC
                print "1. faght that stupid %s" % enemy.name
                print "2. take a nap"
                print "3. run awayyss"
                print "> ",
                input = int(raw_input())
                if input == 1:
                    dbl_atk_prob = random.random()
                    if dbl_atk_prob < 0.8:
                        hero.drunk_attack(enemy)
                    else:
                        hero.attack(enemy)
                elif input == 2:
                    pass
                elif input == 3:
                    print "Goodbye."
                    exit(0)
                else:
                    print "Invalid input %r" % input
                    continue
                enemy.attack(hero)
            if hero.alive():
                print bcolors.OKGREEN + "You defeated the %s" % enemy.name + bcolors.ENDC
                return True
            else:
                print bcolors.FAIL + "YOU LOSE!" + bcolors.ENDC
                return False
class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class Zombie_Killer(object):
    cost = 15
    name = "zombie killer"
    def apply(self, character):
        character.zombie_killer = True
        print "Zombie killer equipped"

class SuperTonic(object):
    cost = 10
    name = "supertonic"
    def apply(self, hero):
        hero.health += 10
        print "Your health has increased by 10."

class Armor(object):
    cost = 10
    name = "armor"
    def apply(self, hero):
        hero.armor += 2
        print "You have %d armor points" % (hero.armor)

class Evade(object):
    cost = 5
    name = 'evade'
    def apply(self, hero):
        hero.evade += .075
        print 'You have %d evade points' % (hero.evade)

class Whiskey(object):
    cost = 10
    name = 'whiskey'
    def apply(self, hero):
        hero.drunk = True


class Shopping(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Shopping.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Zombie_Killer, Armor, Evade, Whiskey]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print bcolors.OKBLUE + "Welcome to the store!" + bcolors.ENDC
            print "====================="
            print "You have %d coins." % hero.coins
            print bcolors.UNDERLINE + "What do you want to do?" + bcolors.ENDC
            for i in xrange(len(Shopping.items)):
                item = Shopping.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Shopping.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Goblin(), Wizard(), Medic(), Lawrence(), Shadow(), Toby(), Zombie()]
battle_engine = Battle()
shopping_engine = Shopping()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print bcolors.FAIL + "YOU LOSE!" + bcolors.ENDC
        exit(0)
    shopping_engine.do_shopping(hero)

print bcolors.OKGREEN + "YOU WIN!" + bcolors.ENDC
