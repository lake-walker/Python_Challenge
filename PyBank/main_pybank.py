# PyBank Python Challenge

# Dependencies
import os
import csv

# Create variables

total_months = []

# Create the path

budget_data = os.path.join("Resources", "budget_data.csv")

print('Financial Analysis')
print('---------------------')

# Open the csv file and store the header 

with open(budget_data, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)
    # Total number of months
    total_months = len(list(reader))
    print(f"Total months: {total_months}")
    
    
with open(budget_data, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)   
    # Net total profit/loss
    net_profloss = sum([int(row[1]) for row in reader])
    print(f"Total: ${net_profloss}")
    
# Average changes in Profit/Loss
with open(budget_data, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)

    # create lists for values to be stored in. One for the profit/loss column, one for the difference, one for the dates
    diff_proffloss = []
    proffloss = []
    date = []

    # append the two empty lists that were created to contain the profit/loss and date data
    for row in reader:
        proffloss.append(float(row[1]))
        date.append(row[0])
    

    # append the difference list to contain the new values with the difference in profit/loss between months 
    for i in range(1 ,len(proffloss)):
       diff_proffloss.append(float(proffloss[i]) - float(proffloss[i - 1])) 
    

    # calculate the average for the profit/loss
    average_profloss = sum(diff_proffloss) / len(diff_proffloss)

    # print and round result to the nearest two decimal places
    print(f"Average Profit/Loss: ${round(average_profloss, 2)}")

    # find values for greatest increase and decrease in profits
    profit_loss = round(min(diff_proffloss))
    profit_gain = round(max(diff_proffloss))

    # find corressponding indecies 
    ind_loss = diff_proffloss.index(profit_loss)
    ind_gain = diff_proffloss.index(profit_gain)

    # find the corressponding date to the previous index found. Have to add 1 because we have 1 less piece of data in that list compared to master list
    loss_date = date[ind_loss + 1]
    gain_date = date[ind_gain + 1]
    
    # print both statements
    print(f'Greatest Increase in Profits: {gain_date} (${profit_gain})')
    print(f'Greatest Decrease in Profits: {loss_date} (${profit_loss})')
    
# write a new file and save the results within


financial_analysis = os.path.join("Analysis", "Financial_Analysis.txt")

with open(financial_analysis, 'w') as writer:
    print('Financial Analysis', file=writer)
    print('---------------------', file=writer)
    print(f"Total months: {total_months}", file=writer)
    print(f"Total: ${net_profloss}", file= writer)
    print(f"Average Profit/Loss: ${round(average_profloss, 2)}", file=writer)
    print(f'Greatest Increase in Profits: {gain_date} (${profit_gain})', file= writer)
    print(f'Greatest Decrease in Profits: {loss_date} (${profit_loss})', file=writer)

    



    



    









