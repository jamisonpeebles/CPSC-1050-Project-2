"""
Author:         Jamison Peebles
Date:           April 25, 2024
Assignment:     Project 02
Course:         CPSC1050
GitHub link:    https://github.com/jamisonpeebles

CODE DESCRIPTION: 

"""
#imports needed functions and classes from other files
import csv

from Classes.user_class import User
from Classes.BookRelated.logbook_class import Logbook
from Classes.BookRelated.order_class import Order
from Classes.CookingRelated.ingredient_class import Ingredient
from Classes.OperationsRelated.ingredient_room_class import IngredientStorage
from Classes.OperationsRelated.map_class import Map
from Classes.OperationsRelated.room_class import Room
from Classes.PotionRelated.potion_class import Potion
from Functions.create_game_fn import init_game
from Functions.csv_reader import csv_to_dict_reader

def main():
    #initializes objects of the corresponding type
    map = Map()
    logbook = Logbook()
    potion = Potion()

    #runs init_game function
    init_game(map, logbook)

    #initializes instance of the User class
    user = User(map.get_room('bedroom'), map)

    #prints welcome message
    print('You have awoken in your bedroom; however, it is not actually your bedroom. Looking around, you make several conclusions about your newfound residence. You see maps and photos on your walls and combining theses with the surroundings you observe outside your window, you realize you are in a small cottage in southern France. You also realize that it is no longer modern day. Rather, you have somehow been transported back to the middle ages. Rising from bed, you see your room is simply furnished by the bed you awoke from, a small dresser, and a desk. There is an old, word, leather-bound book sitting on top of the desk with a folded piece of paper tucked into the cover. You draw the paper from the book and read: "Welcome to your new home. Your first trial is to make it through the day. Make it through a month, and the curse will be transferred to another. Don\'t fail. Today you will only have three orders. Each will request a different product, the logbook will tell you their orders and the recipes. Be very careful, potion-creation is a delicate and precise endeavor, and the materials in this hut are quite volatile. I have left you more than enough ingredients for your first day, but if you need extra help, check the recipes within the logbook. Luckily, your customers are infinitely patient. Don\'t worry, you did nothing to deserve this. The curse randomly selects a new Alchemist each month after one completes their service... or fails. \nOn that note, good luck, and good riddance to this place. \n\n\t-Alchemist MDCCXVII\n\n')

    #starts turn-taking loop
    while True:

        #prints user info
        print(user)

        #starts a loop that requires the user to choose what they will do
        while True: 
            print('\nWhat would you like to do? (exit room / read logbook / use held item / throw away held item / take item from storage room))')
            #takes user input for their choice for what they will do with their turn
            first_choice = input().strip().lower()
            
            #if the user chooses to exit the room, they will be shown a list of the exit options and asked to choose one
            if first_choice == 'exit room':
                
                print(f'\nExit options: {user.location.get_exits()}')
                user.set_room_choice(map)
                break

            #if the user chooses to take from storage, they will be prompted to choose an item from a shown list of the storage room's inventory
            elif first_choice == 'take item from storage room':

                #verifies user is in the storage room and does not have another item in their hand
                if user.location.get_name() == 'storage room' and (user.held_item == None):
                    
                    map.get_room('storage room').inventory_ingredients()
                    print(map.get_room('storage room'))

                    item_choice = ''
                    while not (item_choice == 'exit'):
                        #takes user input for item to be taken
                        item_choice = input('What item would you like to take from storage? (enter "exit" to leave menu)\n').strip().lower()
                        
                        try:
                            user.held_item = map.get_room('storage room').take_item(item_choice, map)
                            print(f'You are now holding the following item: {user.held_item.get_name()}')
                        except:
                            print(f'You must select an item from the storage room')

                        break

                else:
                    print('You must be in the storage room with no currently held item to access the hut\'s storage')
                    continue

            #allows the user to take actions upon their held item
            elif first_choice == 'use held item':
                #verifies user is holding an object
                if type(user.held_item) != type(None):
                    
                    while True:
                        #takes user input for what to do with the item
                        item_choice = input('Choose what to do with your item: (exmaine item / dry item / grind item / use item in current potion)\n').strip().lower()

                        #if user is in the drying_room, the held item is dried
                        if item_choice == 'dry item':
                            if user.location.get_name() == 'drying room':
                                user.held_item.dry_ingredient()
                                print(f'Your {user.held_item.get_name()} is now dried')
                            else: 
                                print('You must be in the drying room to dry ingredients')
                            break

                        #prints info about the held item
                        elif item_choice == 'examine item':
                            print(f'\n{user.held_item.get_name()}: {user.held_item}\nCharacteristics: {user.held_item.get_dried_status()}, {user.held_item.get_ground_status()}\n')
                            break

                        #if user is in the bottling room, the held item is ground
                        elif item_choice == 'grind item':
                            if user.held_item.dried_status == 'dried':
                                if user.location.get_name() == 'bottling room':
                                    user.held_item.grind_ingredient()
                                    print(f'Your {user.held_item.get_name()} is now ground')
                                else:
                                    print('Your mortar and pestle are in the bottling room. You must go there to grind this ingredient')
                                    break
                            else:
                                print('You probably shouldn\'t try to grind something without drying it first.')
                            break

                        #if user is in the bottling room, the held item is added to the potion
                        elif item_choice == 'use item in current potion':
                            if user.location.get_name() == 'bottling room':
                                potion.add_ingredient(user.held_item, user, logbook, )
                                user.held_item = None
                            else:
                                print('Your cauldron is in the bottling room. Go there to add to the potion')
                            break

                        else:
                            print('Please enter a choice from the listed options')
                            continue

                else:
                    print('You must be holding an item to use it.')
                    continue

            #allows the user to throw out their held item
            elif first_choice == 'throw away held item':
                user.held_item = None
                print('You have thrown away your item. Beware running out of materials, you can\'t get any more...')

            #displays the content of the logbook for the user
            elif first_choice == 'read logbook':
                print(logbook)

            else:
                print('Please choose a valid option')
                continue

if __name__ == '__main__':
    main()