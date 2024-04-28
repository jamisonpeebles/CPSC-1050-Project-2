'''
This class is for objects that are considered ingredients. It will contain information about the state of the ingredients.
'''

class Ingredient:

    #initializes the class and its attributes from the DictReader object's row
    def __init__(self, dict_reader_row):
        self.name = dict_reader_row['name']
        self.description = dict_reader_row['description']
        self.dried_status = dict_reader_row['dried_status']
        self.ground_status = dict_reader_row['ground_status']

    #when an instance of the class is printed, the instance's description is printed
    def __str__(self):
        return self.description

    #sets the dried status to dried
    def dry_ingredient(self):
        self.dried_status = 'dried'

    #sets the ground status to ground
    def grind_ingredient(self):
        self.ground_status = 'ground'

    #sets an instance's name
    def set_name(self, name):
        self.name = name
        
    #returns an instance's name
    def get_name(self):
        return self.name
    
    #returns an instance's dried status
    def get_dried_status(self):
        return self.dried_status
    
    #returns an instance's ground status
    def get_ground_status(self):
        return self.ground_status