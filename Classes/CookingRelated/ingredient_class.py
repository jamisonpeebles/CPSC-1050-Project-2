'''
This class is for objects that are considered ingredients. It will contain information about the state of the ingredients.
'''

class Ingredient:

    def __init__(self, dict_reader_row):
        self.name = dict_reader_row['name']
        self.description = dict_reader_row['description']
        self.cooked_status = dict_reader_row['cooked_status']
        self.dried_status = dict_reader_row['dried_status']
        self.ground_status = dict_reader_row['ground_status']

    def __str__(self):
        return self.description

    def cook_ingredient(self):
        self.cooked_status = 'cooked'

    def dry_ingredient(self):
        self.dried_status = 'dried'

    def grind_ingredient(self):
        self.ground_status = 'ground'

    def get_name(self):
        return self.name