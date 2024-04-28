'''
A class containing the info for creation of a new potion
'''

class Potion:
    
    def __init__(self):
        self.name = ''
        self.contents = {}
        self.secret_count = 1
        self.okay = 'The potion bubbles and swirls, flashing numerous colors before settling again. You think you did the right thing, at least for now.'

    def add_ingredient(self, ingredient):
        #self.contents[ingredient.get_name()] = ingredient
        self.check_potion(ingredient)

    def dump_potion(self):
        self.contents = {}

    def check_potion(self, ingredient):

        if self.secret_count == 1:
            if (ingredient.get_name() == 'thistle') and (ingredient.get_ground_status() == 'ground') and (ingredient.get_dried_status() == 'dried'):
                print(self.okay)
                self.secret_count += 1
            else:
                self.failure()
        elif self.secret_count == 2:
            if (ingredient.get_name() == 'essence of the sea') and (ingredient.get_ground_status() == 'ground') and (ingredient.get_dried_status() == 'dried'):
                print(self.okay)
                self.secret_count += 1
            else:
                self.failure()
        elif self.secret_count == 3:
            if (ingredient.get_name() == 'bone of the unholy serpent') and (ingredient.get_ground_status() == 'ground') and (ingredient.get_dried_status() == 'dried'):
                print(self.okay)
                self.secret_count += 1
                print('Congratulations! Order 1 is completed. Your current potion is replaced with plain water. Focus on your other orders or else...\n')
            else:
                self.failure()
        elif self.secret_count == 4:
            if (ingredient.get_name() == 'mushroom') and (ingredient.get_ground_status() == 'unground') and (ingredient.get_dried_status() == 'dried'):
                print(self.okay)
                self.secret_count += 1
            else:
                self.failure()
        elif self.secret_count == 5:
            if (ingredient.get_name() == 'mushroom') and (ingredient.get_ground_status() == 'unground') and (ingredient.get_dried_status() == 'dried'):
                print(self.okay)
                self.secret_count += 1
            else:
                self.failure()
        elif self.secret_count == 6:
            if (ingredient.get_name() == 'essence of the sea') and (ingredient.get_ground_status() == 'ground') and (ingredient.get_dried_status() == 'dried'):
                print(self.okay)
                self.secret_count += 1
            else:
                self.failure()
        elif self.secret_count == 7:
            if (ingredient.get_name() == 'leaves of the sacred vine') and (ingredient.get_ground_status() == 'unground') and (ingredient.get_dried_status() == 'dried'):
                print(self.okay)
                self.secret_count += 1
                print('Congratulations! Order 2 is completed. Your current potion is replaced with plain water. Focus on your other orders or else...\n')
            else:
                self.failure()
        elif self.secret_count == 8:
            if (ingredient.get_name() == 'coffee') and (ingredient.get_ground_status() == 'ground') and (ingredient.get_dried_status() == 'dried'):
                print(self.okay)
                self.secret_count += 1
            else:
                self.failure()
        elif self.secret_count == 9:
            if (ingredient.get_name() == 'essence of the sea') and (ingredient.get_ground_status() == 'ground') and (ingredient.get_dried_status() == 'dried'):
                print(self.okay)
                self.secret_count += 1
            else:
                self.failure()
        elif self.secret_count == 10:
            if (ingredient.get_name() == 'leaves of the sacred vine') and (ingredient.get_ground_status() == 'ground') and (ingredient.get_dried_status() == 'dried'):
                print(self.okay)
                print('Congratulations! Order 3 is completed.')
                print('Congratualations. You survived your first day as the Alchemist. Rest well, you will need it for when the orders pick up tomorrow.\n\n\nYou have finished the demo version of the game. Enter any key to exit the game.')
                end_key = input()
                quit()
            else:
                self.failure()

        '''order1 = True
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

        if (logbook.order1.get_raw_status == False) and (order1 == True):
            logbook.order1.complete_order()
            print('Congratulations! Order 1 is completed. Your current potion is replaced with plain water. Focus on your other orders or else...\n')
            user.potion_completed()
            self.dump_potion()
        elif (logbook.order2.get_raw_status == False) and (order2 == True):
            logbook.order2.complete_order()
            print('Congratulations! Order 2 is completed. Your current potion is replaced with plain water. Focus on your other orders or else...\n')
            user.potion_completed()
            self.dump_potion()
        elif (logbook.order3.get_raw_status == False) and (order3 == True):
            logbook.order3.complete_order()
            print('Congratulations! Order 3 is completed. Your current potion is replaced with plain water. Focus on your other orders or else...\n')
            user.potion_completed()
            self.dump_potion()'''

    def failure(self):
        print('The potion boils vigourously and begins to expand. Fumes begin to fill the air as the potion turns black as night. You breathe in the fumes and begin to hallucinate, seeing uncomprehensible horrors. Your last thought is that you wish you\'d been more careful...\n\nGame Over. Enter any key to exit.\n')
        end_key = input()
        quit()