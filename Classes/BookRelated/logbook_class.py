'''
Houses a class that will contain the logbook holding the customer's orders.
'''

from Classes.BookRelated.order_class import Order

#creates a class for the game's logbook
class Logbook:
    #initializes logbook objects and assigns attributes, each containing one of the day's orders, an order object containing the recipe for the order
    def __init__(self):
        self.order1 = Order('A poison\nIngredients: \n1 dried and ground thistle\n1 essence of the sea\n1 dried and ground bone of the unholy serpent\n')
        self.order2 = Order('An elixir of health\nIngredients: \n2 dried mushroom\n1 essence of the sea\n1 dried leaves of the sacred vine\n')
        self.order3 = Order('An elixir of unending focus\nIngredients: \n1 dried and ground coffee\n1 essence of the sea\n1 dried and ground leaves of the sacred vine\n')

    #a method that is used to print the logbook object. it returns the orders for the day and each one's recipe as well as the status of each object
    def __str__(self):
        return f'\nYour orders for the day consist of the following: \n{(self.order1)}\n{self.order2}\n{self.order3}\n\nOrder Status: \nOrder 1: {self.order1.check_status()}\nOrder 2: {self.order2.check_status()}\nOrder 3: {self.order3.check_status()}\n'