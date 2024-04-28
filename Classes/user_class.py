'''
Creates a base class to store data about the user
'''

class User:
    def __init__(self, location, map):
        self.location = location
        self.map = map
        self.room_choice = ''
        self.order_completion = 0
        self.held_item = None

    def __str__(self):
        if type(self.held_item) != type(None):
            prtstr = f'\nCurrent Room: {self.location.get_name()}: {self.location.get_description()}\nOrders Completed: {self.order_completion}/3\nHeld Item: {self.held_item.get_name()}'
        else:
            prtstr = f'\nCurrent Room: {self.location.get_name()}: {self.location.get_description()}\nOrders Completed: {self.order_completion}/3\nHeld Item: Not currently holding an item'
        return prtstr
    
    def set_room_choice(self,map):
        while True:
            choice = input('Please select an exit: ').strip().lower()
            try:
                if choice in self.location.get_exits():
                    self.room_choice = choice
                    self.location = map.get_room(choice)
                    break
                else:
                    raise ValueError
            except:
                print(f'Please enter a valid exit for your current room. Exits: {self.location.get_exits()}')
                continue

    def get_room_choice(self):
        return self.room_choice
    
    def get_inventory(self):
        return self.inventory
    
    def take_from_inventory(self):
        while True:
            item_choice = input('Please choose an item from inventory to hold: ').strip().lower()
            if item_choice == 'exit':
                break
            elif item_choice in self.inventory.keys():
                self.held_item = self.inventory[item_choice]
                self.remove_from_inventory(item_choice)
                break
            else:
                print('Please choose an item from inventory')
                continue
    
    def remove_from_inventory(self, removal):
        if removal in self.inventory.keys():
            self.inventory.pop(removal)
        else:
            raise ValueError
    
    def check_completion():