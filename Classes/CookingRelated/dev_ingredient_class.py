'''
This class is for objects that are considered ingredients but only for the order compaisions. It will contain information about the state of the ingredients.
'''

class devIngredient:

    def __init__(self, name, description, cooked_status, dried_status, ground_status):
        self.name = name
        self.description = description
        self.cooked_status = cooked_status
        self.dried_status = dried_status
        self.ground_status = ground_status

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