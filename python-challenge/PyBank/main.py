# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# * Your task is to create a Python script that analyzes the records to calculate each of the following:

import os
import csv
import pathlib

#open here
budget_data = os.path.join(pathlib.Path(__file__).parent.resolve(), "Resources", "budget_data.csv")
#variables here
month_count = 0
profitloss = 0
month_value = 0
change = 0
dates = []
profits = []

#start here; be sure to skip header, can start counters
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    month_count += 1
    profitloss += int(first_row[1])
    month_value = int(first_row[1])

#budget_data_source = budget_data_source[1:]? shorten your variables and be more specific. *clarity*
#   * The total number of months included in the dataset
# float not necessary
#Total number of months in dataset
#for row in data[1:]:

    csv_header = next(csvreader)
    first_row = next(csvreader)
    month_count += 1
    profitloss += int(first_row[1])
    month_value = int(first_row[1])
    
 #loop through rows; dates, change by month
    for row in csvreader:
        dates.append(row[0])
        
        change = int(row[1])-month_value
        profits.append(change)
        month_value = int(row[1])
        
        #Total number of months
        month_count += 1

#   * The net total amount of "Profit/Losses" over the entire period

#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#add each cell month by month to find changes
        profitloss = profitloss + int(row[1])

#use found changes to calculate average change
    average_change = sum(profits)/len(profits)

#   * The greatest increase in profits (date and amount) over the entire period
#Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]
#print(f"Greatest Increase: {} {}")
#   * The greatest decrease in profits (date and amount) over the entire period
# #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]
#print(f"Greatest Decrease: {} {}")
#print it all here
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${profitloss}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})")

# Exporting to .txt file
with open('analysis.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("---------------------\n")
    f.write(f"Total Months: {month_count}\n")
    f.write(f"Total: ${profitloss}\n")
    f.write(f"Average Change: ${round(average_change,2)}\n")
    f.write(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})\n")
    f.write(f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})\n")