'''
Creates specialty class for the ingredient storage room. 
'''

from room_class import Room

class IngredientStorage(Room):
    def __init__(self):
        self.stored_ingredients = []
        self.ingredient_inventory = {}

    def store_ingredient(self, ingredient):
        self.stored_ingredients.append(ingredient)

    def inventory_an_ingredient(self, ingredient):
        for ingredient in self.stored_ingredients:
            if ingredient.get_name() in self.ingredient_inventory.keys():
                self.ingredient_inventory[ingredient.get_name()] += 1
            else: 
                self.ingredient_inventory[ingredient.get_name()] = 1

    def check_inventory(self):
        pass