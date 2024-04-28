'''
Creates specialty class for the ingredient storage room. Inherits methods from the Room class.
'''

from Classes.OperationsRelated.room_class import Room
from Classes.user_class import User

class IngredientStorage(Room):
    #intializes instance with attributes of the class
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
        self.stored_ingredients = []
        self.ingredient_inventory = {}

    #returns the ingredient inventory when an instance is printed
    def __str__(self):
        return f'Inventory contents include the following: \n{self.ingredient_inventory}'

    #sets an instance's name
    def set_name(self,name):
        self.name = name 

    #returns an instance's name
    def get_name(self):
        return self.name

    #adds an ingredient to the stored_ingredients list
    def store_ingredient(self, ingredient):
        self.stored_ingredients.append(ingredient)

    #updates the ingredient_inventory dictionary with the current state of the stored_ingredients list
    def inventory_ingredients(self):
        self.ingredient_inventory = {}
        for ingredient in self.stored_ingredients:
            if ingredient.get_name() in self.ingredient_inventory.keys():
                self.ingredient_inventory[ingredient.get_name()] += 1
            else: 
                self.ingredient_inventory[ingredient.get_name()] = 1

    #allows for the taking of an item from the inventory and returning it from the method
    def take_item(self, item, map):
        if item == 'exit':
            return None
        for ingredient in map.get_room('storage room').stored_ingredients:
            if ingredient.get_name() == item:
                map.get_room('storage room').stored_ingredients.remove(ingredient)
                return ingredient
        raise ValueError