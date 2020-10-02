# PyPoll Python Challenge

# dependencies
import os
import csv

#create the path

election_data = os.path.join('Resources'/'election_data.csv')

# open file and store header
with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)

    #total number of votes
    
