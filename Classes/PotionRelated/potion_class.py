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
        order1 = True
        order2 = True
        order3 = True
        for content in self.contents:
            if (content in logbook.order1.ingredients) and (order1 == True):
                order1 = True
            else:
                order1 = False

            if (content in logbook.order1.ingredients) and (order2 == True):
                order2 = True
            else:
                order2 = False
            
            if (content in logbook.order1.ingredients) and (order3 == True):
                order3 = True
            else:
                order3 = False

        if order1 == True:
            for ingredient1 in logbook.order1.ingredients:
                if (ingredient1 in self.contents) and (order1 == True):
                    order1 = True
                else:
                    order1 = False
        elif order2 == True:
            for ingredient2 in logbook.order2.ingredients:
                if (ingredient2 in self.contents) and (order2 == True):
                    order2 = True
                else:
                    order2 = False
        elif order3 == True:
            for ingredient3 in logbook.order1.ingredients:
                if (ingredient3 in self.contents) and (order3 == True):
                    order3 = True
                else:
                    order3 = False

        if order1 == True:
            logbook.order1.complete_order()
            print('Congratulations! Order 1 is completed. Your current potion is replaced with plain water. Focus on your other orders or else...\n')
            self.dump_potion()
        elif order2 == True:
            logbook.order2.complete_order()
            print('Congratulations! Order 2 is completed. Your current potion is replaced with plain water. Focus on your other orders or else...\n')
            self.dump_potion()
        elif order3 == True:
            logbook.order3.complete_order()
            print('Congratulations! Order 3 is completed. Your current potion is replaced with plain water. Focus on your other orders or else...\n')
            self.dump_potion()