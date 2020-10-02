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

# Khan votes
with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    khan_votes = []

    for row in reader:
        if row[2] == 'Khan':
            khan_votes.append(row[0])
    
    khan_total = len(khan_votes)
    print(f'Khan: {khan_total} votes')

# Correy votes
with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    correy_votes = []

    for row in reader:
        if row[2] == 'Correy':
            correy_votes.append(row[0])
    
    correy_total = len(correy_votes)
    print(f'Correy: {correy_total} votes')

# Li votes
with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    li_votes = []

    for row in reader:
        if row[2] == 'Li':
            li_votes.append(row[0])
    
    li_total = len(li_votes)
    print(f'Khan: {li_total} votes')

# O'Tooley votes
with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    tooley_votes = []

    for row in reader:
        if row[2] == "O'Tooley":
            tooley_votes.append(row[0])
    
    tooley_total = len(tooley_votes)
    print(f'Khan: {tooley_total} votes')

