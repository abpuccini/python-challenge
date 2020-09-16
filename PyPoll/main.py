# PyPoll Analysis

## Implementing modules 

import csv
import os

## File path

datafile = os.path.join('Resources', 'election_data.csv')

## Analysis

### Part I: Reading file, Storing header and Initializing sets

candidate_votes = {}                                        # Dictionary {Candidate: Votes}
candidate = []                                              # List of all votes
candidate_name = []                                         # List of candidate names               

with open(datafile, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    header = next(csvreader)                                # Header stored
    for rows in csvreader:
        name_index = 2                                      # Index of names in rows is [2]
        name = rows[name_index]
        candidate.append(name)                              # Adding name to the list
    for n in candidate:                                     # n represents each element in candidate list
        if n not in candidate_name:                         # Removing duplicated candidate names
            candidate_name.append(n)                        # List of candidates
    for i in candidate_name:                                # i represents each element in candidate_name list 
        candidate_votes[i] = candidate.count(i)             # Adding key and value into candidate_vote dictionary
        total = sum(candidate_votes.values())               # Sum of all values in dictionary
        
        





print(total)


        
        
# with open(datafile, 'r') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')  
#     header = next(csvreader)
#     for row in csvreader:
#         name_index = 2
#         candidate_name = row[name_index]                    # List of Candidate names
#         if candidate_name in candidate_vote.keys():
#             candidate_vote[candidate_name] += 1
#         else:
#             candidate_vote[candidate_name] = 1

# # {'Khan': 1}

# # total votes
# totalvotes = sum(candidate_vote.values())
# print(f'Total votes {totalvotes}')
# # calculate inv % candidate
# percent = []
# for i in candidate_vote:
#     percent = round(float(candidate_vote[i] / totalvotes) * 100 , 0)
#     print(f'{i} : {percent}% : {candidate_vote[i]}')
# # finding candidate with max votes
# for key in candidate_vote.keys():
#     if candidate_vote[key] == max(candidate_vote.values()):
#         winner = key

# print(f'Winner is: {winner}')