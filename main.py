"""
Author:         Jamison Peebles
Date:           April 25, 2024
Assignment:     Project 02
Course:         CPSC1050

CODE DESCRIPTION: 

"""

class Entity(hp = 0):
    self.hp = hp
    self.weapon = 'unarmed'

    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_weapon(self):
        return self.weapon
    
    def add_hp(self, hp_add_amount):
        self.hp += hp_add_amount

    def subtract_hp(self, hp_subtract_amount):
        self.hp -= hp_subtract_amount

    def get_hp(self):
        return self.hp

class Weapon():
    pass

class Location():
    pass

class Food():
    pass

def main():
    #prints welcome message
    print('Welcome to the Campsite. You and your bro are sitting around the campfire when you decide to go on a quest to find a mythical plant, only foretold in myths and omens. You know from talking to the locals that the plant can be found nearby, but you know the path to find it will not be easy... \n Your first decision lies in which direction you must head. You see three choices ahead of you. You can venture deeper into the woods, towards the river you hear in the distance, or towards the mountains looming in the mist.')

    #prompts user for location choice
    location_choice = input('Please enter a location to explore: (woods/river/mountains)').strip().lower()

if __name__ == '__main__':
    main()