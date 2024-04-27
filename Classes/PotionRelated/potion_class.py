'''
A class containing the info for creation of a new potion
'''

class Potion:
    
    def __init__(self):
        self.name = ''
        self.contents = {}

    def add_ingredient(self, ingredient):
        self.contents[ingredient.get_name()] = ingredient