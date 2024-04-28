'''
Creates a base class to store data about the user
'''

class User:
    #initializes an instance of the class
    def __init__(self, location, map):
        self.location = location
        self.map = map
        self.room_choice = ''
        self.order_completion = 0
        self.held_item = None

    #when an instance of the user class is printed the __str__ function returns a formatted message
    def __str__(self):
        if type(self.held_item) != type(None):
            prtstr = f'\nCurrent Room: {self.location.get_name()}: {self.location.get_description()}\nOrders Completed: {self.order_completion}/3\nHeld Item: {self.held_item.get_name()}'
        else:
            prtstr = f'\nCurrent Room: {self.location.get_name()}: {self.location.get_description()}\nOrders Completed: {self.order_completion}/3\nHeld Item: Not currently holding an item'
        return prtstr
    
    #sets the user room choice and transports the user to a new location within the hut using user input
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

    #returns room choice
    def get_room_choice(self):
        return self.room_choice