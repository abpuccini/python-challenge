# PyPoll

## Implementing modules 

import csv
import os

## File path

datafile = os.path.join('Resources', 'election_data.csv')

## Election Results

### Part I: Reading file, Storing header and Initializing sets

candidate_votes = {}                                        # Dictionary {Candidate: Votes}
election_votes = []                                         # List of all votes
candidate_name = []                                         # List of election_votes names               
percent_votes = []                                          # List of percentage votes for each election_votes
winner = []

with open(datafile, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    header = next(csvreader)                                # Header stored
    for rows in csvreader:
        name_index = 2                                      # Index of names in rows is [2]
        name = rows[name_index]
        election_votes.append(name)                         # Adding name to the list
    for n in election_votes:                                # n represents each element in election_votes list
        if n not in candidate_name:                         # Removing duplicated election_votes names
            candidate_name.append(n)                        # List of candidates

### Part II: Total votes

for i in candidate_name:                                    # i represents each element in candidate_name list 
    candidate_votes[i] = election_votes.count(i)            # Adding key and value into candidate_vote dictionary

total = sum(candidate_votes.values())                       # Sum of all values in dictionary

### Part III: Number and Percentage of Each candidates' votes

candidate_votes_list = list(candidate_votes.values())        # Creating vote count list

for p in candidate_votes_list:     
    p_votes = round(float(p / total * 100), 2)               # % of votes for each election_votes
    percent_votes.append("%.3f" % p_votes)                   # Adding % of votes with 3 decimals to the list
    
### Part IV: The Winner

for m in candidate_votes_list:
    if m == max(candidate_votes_list):
        name = candidate_name[candidate_votes_list.index(m)]    # Identify winner by 

print(name)





