# PyPoll Python Challenge

# dependencies
import os
import csv

#create the path

election_data = os.path.join('Resources','election_data.csv')



# open file and store header
with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)

    #total number of votes
    total_votes = len(list(reader))
    

# Calculate the total number of votes per candidate
with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    khan_votes = []
    correy_votes = []
    li_votes = []
    tooley_votes = []

    for row in reader:
        if row[2] == 'Khan':
            khan_votes.append(row[0])
        elif row[2] == 'Correy':
            correy_votes.append(row[0])
        elif row[2] == 'Li':
            li_votes.append(row[0])
        elif row[2] == "O'Tooley":
            tooley_votes.append(row[0])
    
    khan_total = len(khan_votes)
    correy_total = len(correy_votes)
    li_total = len(li_votes)
    tooley_total = len(tooley_votes)

# find percentage of total vote for each candidate
with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)

    khan_percent = round((khan_total / total_votes) * 100, 3)
    correy_percent = round((correy_total / total_votes) * 100, 3)
    li_percent = round((li_total / total_votes) * 100, 3)
    tooley_percent = round((tooley_total / total_votes) * 100, 3)

#print statement to terminal
print('Election Results')
print('--------------------')
print(f'Total Votes: {total_votes}')
print('--------------------')
print(f'Khan: {khan_percent}% ({khan_total})')
print(f'Correy: {correy_percent}% ({correy_total})')
print(f'Li: {li_percent}% ({li_total})')
print(f"O'Tooley: {tooley_percent}% ({tooley_total})")
print('--------------------')

# Determine the winner of the election
if khan_percent > 50:
    print('Winner: Khan')
elif correy_percent > 50:
    print('Winner: Correy')
elif li_percent > 50:
    print('Winner: Li')
elif tooley_percent > 50:
    print("Winner: O'Tooley")

print('--------------------')

#Export results to a text file

election_analysis = os.path.join("Analysis", "Election_Analysis.txt")

with open(election_analysis, 'w') as writer:
    print('Election Results', file=writer)
    print('--------------------', file=writer)
    print(f'Total Votes: {total_votes}', file=writer)
    print('--------------------', file=writer)
    print(f'Khan: {khan_percent}% ({khan_total})', file=writer)
    print(f'Correy: {correy_percent}% ({correy_total})', file=writer)
    print(f'Li: {li_percent}% ({li_total})',file=writer)
    print(f"O'Tooley: {tooley_percent}% ({tooley_total})", file=writer)
    print('--------------------', file=writer)

    if khan_percent > 50:
        print('Winner: Khan', file=writer)
    elif correy_percent > 50:
        print('Winner: Correy', file=writer)
    elif li_percent > 50:
        print('Winner: Li', file=writer)
    elif tooley_percent > 50:
        print("Winner: O'Tooley", file=writer)
    
    print('--------------------', file=writer)