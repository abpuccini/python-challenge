## Implementing modules 

import csv
import os

## csv file path

data_filepath = os.path.join('Resources', 'budget_data.csv')
output_filepath = os.path.join('Analysis', 'output.csv')
analysis_filepath = os.path.join('Analysis', 'PyBank-analysis.txt')

## Initializing variables

fields = []            # set of data header
rows = []              # set of data 
period = []            # set of period
month = 0              # no. of data
total = 0              # total of $ profit/losses
pl_list =[]            # set of profit/losses
pl_index = 1           # profit/losses is stored in index [1] in dataset
deltalist = [0,]       # set of change of profit/losses

## Analysis

### Reading file and store data

with open(data_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    if csv.Sniffer().has_header:
        fields = next(csvreader)
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
        deltalist.append(int(delta))       # List of changes in profit/losses
    
    delta_sum = sum(deltalist)
    delta_len = len(deltalist) - 1
    diff_avg = round(float(delta_sum / delta_len), 2)

### Part IV: The greatest increase in profits (date and amount) over the entire period

    Max = max(deltalist)
    max_period = period[deltalist.index(Max)]

### Part V: The greatest decrease in losses (date and amount) over the entire period 

    Min = min(deltalist)
    min_period = period[deltalist.index(Min)]

### Part VI: Storing additional data into CSV file

output = zip(period, pl_list, deltalist)
output_fields = fields + ['Diff']

with open(output_filepath, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(output_fields)
    writer.writerows(output)

### Part VII: Analysis Result

#### Creating list of analysis result
    
result = [
    'Financial Analysis ',
    '------------------------------------------------------',
    f'Total months: {month}',
    f'Net Total of profit/loss: ${total}',
    f'Average of change of profit/loss: ${diff_avg}',
    f'The greatest increase in Profit: {max_period} (${Max})',
    f'The greatest decrease in Profit: {min_period} (${Min})'
]
#### Printing result

for r in result:            # r is elements in result list
    print(r)
    
### Part VIII: Exporting result to txt.file

with open(analysis_filepath, 'w') as txtfile:
    for t in result:
        txtfile.write(str(t) + '\n')