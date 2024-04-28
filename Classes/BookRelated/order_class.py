'''
Provides a class for each order to belong to before being stored in the logbook
'''

class Order:
    #creates a method that will allow the creation of an object of the Order class along with the necessary characteristics. 
    def __init__(self, text, status=False):
        self.text = text
        self.ingredients = []
        self.status = status

    #when object is printed, it returns the text associated with the order, in this case the recipe
    def __str__(self):
        return self.text
    
    def set_text(self, text):
        self.text = text

    #allows for the setting of the status of each order
    def complete_order(self):
        self.status = True

    #gets the raw status in boolean form for the order
    def get_raw_status(self):
        return self.status

    #returns a string representation of the order status
    def check_status(self):
        if self.status == True:
            return 'Order Complete'
        else:
            return 'Order Incomplete'

    #allows for the addition of ingredients to an order's ingredient list
    def add_ingredients(self, ingredient):
        self.ingredients.append(ingredient)