'''
Provides a class for each order to belong to before being stored in the logbook
'''

class Order:
    #creates a method that will allow the creation of an object of the Order class along with the necessary characteristics. 
    def __init__(self, status):
        self.status = status

    def __str__(self):
        pass

    #allows for the setting of the status of each order
    def set_status(self, status):
        if status in ['yes', 'no']:
            self.status = status
        else:
            raise ValueError
        
