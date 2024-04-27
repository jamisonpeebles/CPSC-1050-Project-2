'''
Houses a class that will contain the logbook holding the customer's orders.
'''

class Logbook:

    def __init__(self, order_list = []):
        self.order_list = order_list

    def add_order(self, order):
        self.order.append(order)

    def __call__(self):
        print(f'Your orders for the day consist of the following: \n{print(self.order_list[0])}\n{print(self.order_list[1])}\n{print(self.order_list[2])}')

    def __str__(self):
        return f'Your orders for the day consist of the following: \n{print(self.order_list[0])}\n{print(self.order_list[1])}\n{print(self.order_list[2])}'