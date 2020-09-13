## Implementing modules 

import csv
import os

## csv file path

filepath = os.path.join('Resources', 'budget_data.csv')

## Initializing variables

field = []
rows = []
month = 0
average = 0

## Analysis

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    if csv.Sniffer().has_header:
        fields = next(csvreader)
    for row in csvreader: 
        month += 1
    

print('Financial Analysis')
print('---------------------------------------------')
print(f'Total months: {month}')
