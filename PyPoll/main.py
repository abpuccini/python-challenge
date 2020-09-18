# PyPoll

## Implementing modules 

import csv
import os

## File path

data_filepath = os.path.join('Resources', 'election_data.csv')
analysis_filepath = os.path.join('Analysis', 'PyPoll-analysis.txt')

## Election Results

### Part I: Reading file, Storing header and Initializing sets

candidate_votes = {}                                        # Dictionary {Candidate: Votes}
election_votes = []                                         # List of all votes
candidate_name = []                                         # List of election_votes names               
percent_votes = []                                          # List of percentage votes for each election_votes
chart = []

with open(data_filepath, 'r') as csvfile:
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

vote_counts = list(candidate_votes.values())        # Creating vote count list

for p in vote_counts:     
    p_votes = round(float(p / total * 100), 2)               # % of votes for each election_votes
    percent_votes.append("%.3f" % p_votes)                   # Adding % of votes with 3 decimals to the list
    
### Part IV: The Winner

#### Identify winner by using index of the maximum votes because they are arranged in the same order

for m in vote_counts:
    if m == max(vote_counts):
        winner = candidate_name[vote_counts.index(m)]

### Part V: Election Result and exporting result to txt.file

#### Creating votes_chart list containing name, %votes and vote counts

for i in range(len(candidate_name)):
    votes_chart = f'{candidate_name[i]}: {percent_votes[i]}% ({vote_counts[i]})'
    chart.append(votes_chart)

result = [
    'Election Results',
    '-------------------------',
    f'Total Votes: {total}',
    '-------------------------',
    *chart,                                         # *chart >> To unpack the list
    '-------------------------',
    f'Winner: {winner}',
    '-------------------------'
]

with open(analysis_filepath, 'w') as txtfile:
    for r in result:                                # r represents each element in result list
        print(r)
        txtfile.write(str(r) + '\n')










