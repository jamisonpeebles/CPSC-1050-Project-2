'''
A class containing the info for creation of a new potion
'''

class Potion:
    
    def __init__(self):
        self.name = ''
        self.contents = {}

    def add_ingredient(self, ingredient):
        self.contents[ingredient.get_name()] = ingredient

    def dump_potion(self):
        self.contents = {}

    def check_potion(self, logbook):
        if self.contents.keys() == []