# PyPoll Python Challenge

# dependencies
import os
import csv

#create the path

election_data = os.path.join('Resources','election_data.csv')

print('Election Results')
print('--------------------')

# open file and store header
with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)

    #total number of votes
    total_votes = len(list(reader))
    print(f'Total Votes: {total_votes}')
    print('--------------------')

with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    khan_votes = []

    for row in reader:
        if row[2] == 'Khan':
            khan_votes.append(row[0])
    
    khan_total = len(khan_votes)
    print(f'Khan: {khan_total} votes')


