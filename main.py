"""
Author:         Jamison Peebles
Date:           April 25, 2024
Assignment:     Project 02
Course:         CPSC1050

CODE DESCRIPTION: 

"""

import csv

from Classes.user_class import User
from Classes.BookRelated.logbook_class import Logbook
from Classes.BookRelated.order_class import Order
from Classes.BookRelated.recipe_class import Recipe
from Classes.CookingRelated.ingredient_class import Ingredient
from Classes.CookingRelated.dev_ingredient_class import devIngredient
from Classes.OperationsRelated.ingredient_room_class import IngredientStorage
from Classes.OperationsRelated.map_class import Map
from Classes.OperationsRelated.room_class import Room
from Classes.PotionRelated.potion_class import Potion
from Functions.create_game_fn import init_game
from Functions.csv_reader import csv_to_dict_reader
from Functions.instruction_delivery_fn import instructions

def main():

    map = Map()
    logbook = Logbook()
    potion = Potion()

    init_game(map, logbook)

    user = User(map.get_room('storage room'), map)

    #prints welcome message
    print('You have awoken in your bedroom; however, it is not actually your bedroom. Looking around, you make several conclusions about your newfound residence. You see maps and photos on your walls and combining theses with the surroundings you observe outside your window, you realize you are in a small cottage in southern France. You also realize that it is no longer modern day. Rather, you have somehow been transported back to the middle ages. Rising from bed, you see your room is simply furnished by the bed you awoke from, a small dresser, and a desk. There is an old, word, leather-bound book sitting on top of the desk with a folded piece of paper tucked into the cover. You draw the paper from the book and read: "Welcome to your new home. Your first trial is to make it through the day. Make it through a month, and the curse will be lifted. Don\'t fail. Today you will only have three customers. Each will request a different product, good luck figuring out how to make them. Use your intuition and guess your way through it; I have left you more than enough ingredients for your first day, but if you need extra help, check the recipe list within this book. Luckily your customers are infinitely patient and write their orders in the Logbook to help you out. Don\'t worry, you did nothing to deserve this. The curse randomly selects a new Alchemist each month after one completes their service... or fails. \nOn that note, good luck and good riddance to this place. \n\n\t-Alchemist MDCCXVII\n\n')

    while True:
        
        potion.check_potion(logbook, user)
        user.check_completion()

        print(user)

        while True: 
            print('What would you like to do? (exit room / read logbook / dump current potion / use held item / throw away held item / take item from storage (note: must be in storage room to take items))')
            
            first_choice = input().strip().lower()
            
            if first_choice == 'exit room':
                
                print(f'Exit options: {user.location.get_exits()}')
                user.set_room_choice(map)
                break

            elif first_choice == 'take item from storage':
                #while True:

                if user.location.get_name() == 'storage room' and (user.held_item == None):
                    
                    map.get_room('storage room').inventory_ingredients()
                    print(map.get_room('storage room'))

                    item_choice = ''
                    while not (item_choice == 'exit'):
                    
                        item_choice = input('What item would you like to take from storage? (enter "exit" to leave menu)\n').strip().lower()
                        
                        try:
                            user.held_item = map.get_room('storage room').take_item(item_choice, map)
                            print(f'You are now holding the following item: {user.held_item.get_name()}')
                        except:
                            print(f'You must select and item from the storage room')

                        break

                else:
                    print('You must be in the storage room with no currently held item to access the hut\'s storage')
                    break

            elif first_choice == 'use held item':
                if type(user.held_item) != type(None):
                    
                    while True:
                        item_choice = input('Choose what to do with your item: ( exmaine item, dry item, grind item, use item in current potion )\n').strip().lower()

                        if item_choice == 'dry item':
                            user.held_item.dry_ingredient()
                            print(f'Your {user.held_item.get_name()} is now dried')
                            break

                        elif item_choice == 'examine item':
                            print(user.held_item)
                            break

                        elif item_choice == 'grind item':
                            if user.held_item.dried_status == 'dried':
                                user.held_item.grind_ingredient()
                                print(f'Your {user.held_item.get_name()} is now ground')
                            else:
                                print('You probably shouldn\'t try to grind something without drying it first.')
                            break

                        elif item_choice == 'use item in current potion':
                            potion.add_content(user.held_item)
                            user.held_item = None
                            break

                        else:
                            print('Please enter a choice from the options')
                            continue

                else:
                    print('You must be holding an item to use it')

            elif first_choice == 'throw away held item':
                user.held_item = None
                print('You have thrown away your item. Beware running out of materials, you can\'t get any more...')

            elif first_choice == 'read logbook':
                print(logbook)

            elif first_choice == 'dump current potion':
                potion.dump_potion()
                print('Your potion is fresh of boiling water. Your old ingerdients have been washed into the abyss. Don\'t be wasteful...')
                        
            else:
                print('Please choose a valid option')
                continue

if __name__ == '__main__':
    main()