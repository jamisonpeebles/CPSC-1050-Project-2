'''
Class for the rooms that will be navigated through within the alchemist's hut.
'''

# initializes a class for Rooms to hold data about each room and provide methods for retrieving that data
class Room:
    #sets room name, description, and exits (exits should be a list)
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

    #returns name of room
    def get_name(self):
        return self.name
    
    #returns the description of the room
    def get_description(self):
        return self.description
    
    #returns the list of room exits 
    def get_exits(self):
        return self.exits
    
    #returns room exits as strings
    def list_exits(self):
        return_str = ''
        for element in self.exits:
            return_str += (element + '\n')
        return return_str
    
    #returns string representation of all info contained in object of Room class
    def __str__(self):
        string = f'{self.name}: {self.description}\n\nExits:\n{self.list_exits()}'
        return string