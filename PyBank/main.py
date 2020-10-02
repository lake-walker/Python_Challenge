# PyBank Python Challenge

# Dependencies
import os
import csv

# Create variables

total_months = []
average_profloss = ""
greatest_increase = ""
greatest_decrease = ""
increase_date = ""
decrease_date = ""


# Create the path

budget_data = os.path.join("Resources", "budget_data.csv")


# Open the csv file and store the header 

with open(budget_data, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    # Total number of months
    total_months = len(list(reader))
    print(f"Total months: {total_months}")
# Net total profit/loss
with open(budget_data, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    net_profloss = sum([int(row[1]) for row in reader])
    print(f"Total: ${net_profloss}")

# Average changes in Profit/Loss

with open(budget_data, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)

    diff_proffloss = 0
    i = 0

    for row in reader:
       i += 1
       diff_proffloss = (float(row[i]) - float(row[i - 1])) 
    
    print(diff_proffloss)


    









