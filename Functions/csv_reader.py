'''
Houses a function that will read data from a csv file containing all ingredient information.
'''

import csv

def csv_to_dict_reader(file_path):
    with open(file_path, 'r') as csvfile:
        csv_read = csv.DictReader(csvfile)
        
    return csv_read
