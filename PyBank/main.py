## Implementing modules 

import csv
import os

## File path

data_filepath = os.path.join('Resources', 'budget_data.csv')
output_filepath = os.path.join('Analysis', 'output.csv')
analysis_filepath = os.path.join('Analysis', 'PyBank-analysis.txt')

## Initializing sets

headers = []                                        # set of data header
rows = []                                           # set of data 
period = []                                         # set of period
pl_list =[]                                         # set of profit/losses
deltalist = []                                # set of change of profit/losses 

## Analysis

### Reading file and store data

with open(data_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    headers = next(csvreader)                       # Header stored
    for row in csvreader:                           
        rows.append(row)                            # List of data in original file
    for data in rows:
        momth_index = 0                             # Index of each month in rows is [0]
        pl_index = 1                                # Index of each profit/losses in rows is [1]
        period.append(data[momth_index])            # List of periods
        pl_list.append(int(data[pl_index]))         # List of profit/losses
    for x in range(len(pl_list)):                   # x represents index of data in pl_list
        if x == 0:
            delta = 0                               # Index[0] has no comparison to calculate differences
        else:
            delta = pl_list[x] - pl_list[x-1]       # delta is profit/losses differences between period x and x-1
        deltalist.append(int(delta))                # List of changes in profit/losses
        
### Part I: The total number of months included in the dataset

month = len(period)                       
        
### Part II: The net total amount of "Profit/Losses" over the entire period

total = sum(pl_list)                        

### Part III: The average of the changes in "Profit/Losses" over the entire period        
     
delta_sum = sum(deltalist)
delta_len = len(deltalist) - 1                      # First index of deltalist is N/A, to have 
diff_avg = round(float(delta_sum / delta_len), 2)

### Part IV: The greatest increase in profits (date and amount) over the entire period

Max = max(deltalist)
max_period = period[deltalist.index(Max)]

### Part V: The greatest decrease in losses (date and amount) over the entire period 

Min = min(deltalist)
min_period = period[deltalist.index(Min)]

### Part VI: Storing additional data into CSV file

output = zip(period, pl_list, deltalist)
output_headers = headers + ['Diff']

with open(output_filepath, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(output_headers)
    writer.writerows(output)

### Part VII: Analysis Result and exporting result to txt.file

result = [
    'Financial Analysis ',
    '------------------------------------------------------',
    f'Total months: {month}',
    f'Net Total of profit/loss: ${total}',
    f'Average of change of profit/loss: ${diff_avg}',
    f'The greatest increase in Profit: {max_period} (${Max})',
    f'The greatest decrease in Profit: {min_period} (${Min})'
]

with open(analysis_filepath, 'w') as txtfile:
    for r in result:                                # r represents each element in result list
        print(r)
        txtfile.write(str(r) + '\n')


