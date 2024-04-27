'''
This class is for objects that are considered ingredients. It will contain information about the state of the ingredients.
'''

class Ingredient:

    def __init__(self, name, description, cooked_status, dried_status, ground_status):
        self.name = name
        self.description = description
        self.cooked_status = cooked_status
        self.dried_status = dried_status