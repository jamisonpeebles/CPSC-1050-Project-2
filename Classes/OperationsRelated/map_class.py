'''
Creates a class to hold information about the map of the hut.
'''

#creates a class to hold information about the map for the adventure
class Map():

    #initializes class with variable inputs for a dictionary containing the rooms present in the map
    def __init__(self):
        self.map = {}

    #creates a method to add a room to the map dictionary
    def add_room(self, room):
        self.map[room.get_name()] = room

    #returns a room from the map given its name as input
    def get_room(self, room_name):
        if room_name in self.map.keys():
            return self.map[room_name]
        else:
            print(f'{room_name} is not a valid exit')