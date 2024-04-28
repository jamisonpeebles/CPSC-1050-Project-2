'''
Creates specialty class for the ingredient storage room. 
'''

from Classes.OperationsRelated.room_class import Room
from Classes.user_class import User

class IngredientStorage(Room):
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
        self.stored_ingredients = []
        self.ingredient_inventory = {}

    def __str__(self):
        return f'Inventory contents include the following: \n{self.ingredient_inventory}'

    def get_name(self):
        return self.name

    def store_ingredient(self, ingredient):
        self.stored_ingredients.append(ingredient)

    def inventory_ingredients(self):
        self.ingredient_inventory = {}
        for ingredient in self.stored_ingredients:
            if ingredient.get_name() in self.ingredient_inventory.keys():
                self.ingredient_inventory[ingredient.get_name()] += 1
            else: 
                self.ingredient_inventory[ingredient.get_name()] = 1

    def take_item(self, item, map):
        if item == 'exit':
            return None
        for ingredient in map.get_room('storage room').stored_ingredients:
            if ingredient.get_name() == item:
                map.get_room('storage room').stored_ingredients.remove(ingredient)
                return ingredient
        raise ValueError