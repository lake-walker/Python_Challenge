# PyBank Python Challenge

# Dependencies
import os
import csv

# Create variables

total_months = []
# average_profloss = ""
# greatest_increase = ""
# greatest_decrease = ""
# increase_date = ""
# decrease_date = ""


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

    # create lists for values to be stored in. One for the profit/loss column and one for the difference
    diff_proffloss = []
    proffloss = []
    loss_date = []

    # append column list to contain all the original values
    for row in reader:
        proffloss.append(float(row[1]))
        loss_date.append(row[0])
    

    # append the difference list to contain new values
    for i in range(1 ,len(proffloss)):
       diff_proffloss.append(float(proffloss[i]) - float(proffloss[i - 1])) 
    

    # calculate the average for the profit/loss
    average_profloss = sum(diff_proffloss) / len(diff_proffloss)

    # print and round result to the nearest two decimal places
    print(f"Average Profit/Loss: ${round(average_profloss, 2)}")

    # find the greatest increase and decrease in profits
    profit_loss = min(diff_proffloss)
    profit_gain = max(diff_proffloss)

    # loss_date = []
    for col in reader:
        if float(col[1]) == profit_loss:
            loss_date.append(str(col[0]))
    
    print(loss_date)



    









