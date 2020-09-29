# PyBank Python Challenge

# Dependencies
import os
import csv

# Create variables

net_profloss = ""
average_profloss = ""
greatest_increase = ""
greatest_decrease = ""
increase_date = ""
decrease_date = ""


# Create the path

budget_data = os.path.join("Resources", "budget_data.csv")

# Total number of months 
total_months = []
with open(budget_data) as csvfile:
    reader = csv.reader(csvfile)
    csv_header = next(reader)
    total_months = len(list(reader))
print(f"Total months: {total_months}")



