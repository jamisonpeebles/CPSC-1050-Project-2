'''
Provides a class for each order to belong to before being stored in the logbook
'''

class Order:
    #creates a method that will allow the creation of an object of the Order class along with the necessary characteristics. 
    def __init__(self, text, status=False):
        self.text = text
        self.ingredients = []
        self.status = status

    def __str__(self):
        return self.text

    #allows for the setting of the status of each order
    def complete_order(self):
        self.status = True

    def get_raw_status(self):
        return self.status

    def check_status(self):
        if self.status == True:
            return 'Order Complete'
        else:
            return 'Order Incomplete'

    def add_ingredients(self, ingredient):
        self.ingredients.append(ingredient)