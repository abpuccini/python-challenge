## Implementing modules 

import csv
import os

## File path

datafile = os.path.join('Resources', 'election_data.csv')


candidate_vote = {}
candidate_nane = []

with open(datafile, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    header = next(csvreader)
    for row in csvreader:
        candidate_name = row[2]         #candinate name list
        if candidate_name in candidate_vote.keys():
            candidate_vote[candidate_name] = candidate_vote[candidate_name] + 1
        else:
            candidate_vote[candidate_name] = 1

# {'Khan': 1}

# total votes
totalvotes = sum(candidate_vote.values())
print(f'Total votes {totalvotes}')
# calculate inv % candidate
percent = []
for i in candidate_vote:
    percent = round(float(candidate_vote[i] / totalvotes) * 100 , 0)
    print(f'{i} : {percent}% : {candidate_vote[i]}')
# finding candidate with max votes
for key in candidate_vote.keys():
    if candidate_vote[key] == max(candidate_vote.values()):
        winner = key

print(f'Winner is: {winner}')
print(header)

