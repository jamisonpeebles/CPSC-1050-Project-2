'''
Houses a function that will read data from a csv file containing all ingredient information.
'''

import csv

#opens a .csv file and reads it into a DictReader object
def csv_to_dict_reader(file_path):
    with open(file_path, 'r') as csvfile:
        csv_read = csv.DictReader(csvfile)
        
    return csv_read
