## Implementing modules 

import csv
import os

## csv file path

filepath = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join('Analysis', 'output.csv')

## Initializing variables

fields = []            # set of data header
rows = []              # set of data 
period = []            # set of period
month = 0              # no. of data
total = 0              # total of $ profit/losses
pl_list =[]            # set of profit/losses
pl_index = 1           # profit/losses is stored in index [1] in dataset
deltalist = [0,]       # set of change of profit/losses
deltaperiod = []

## Analysis

### Reading file and store data

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    if csv.Sniffer().has_header:
        fields = next(csvreader)
        fields.append('diff')
    for row in csvreader:
        rows.append(row)
    for month in rows:
        period.append(month[0])

### Part I: The total number of months included in the dataset

    for row in rows:
        month = len(rows)                         
        
### Part II: The net total amount of "Profit/Losses" over the entire period

        pl = int(row[pl_index])
        total += pl                        

### Part III: The average of the changes in "Profit/Losses" over the entire period        

        pl_list.append(int(row[pl_index])) # List of profit/losses
    
    for x in range(1, len(pl_list)):
        delta = pl_list[x] - pl_list[x-1]
        deltalist.append(int(delta))       # List of change in profit/losses
    
    delta_sum = sum(deltalist)
    delta_len = len(deltalist) - 1
    diff_average = float(delta_sum / delta_len)

### Part IV: The greatest increase in profits (date and amount) over the entire period

output = zip(period, pl_list, deltalist)

with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(fields)
    writer.writerows(output)






    
        

### Part V: The greatest decrease in losses (date and amount) over the entire period 

  

## Result
    
print('Financial Analysis')
print('---------------------------------------------')
print(f'Total months: {month}')
print(f'Net Total of profit/loss: ${total}')
print(f'Average of change of profit/loss: ${round(diff_average, 2)}')