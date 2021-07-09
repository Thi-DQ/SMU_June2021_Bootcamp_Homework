import os
import csv

# FIGURE OUT THE FILEPATH ON YOUR COMPUTER
csvpath = "PyBank\HW3 - Python budget_data.csv"


# read in the CSV data into memory - a list of lists
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

# exclude header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Setting variables
    monthly_changes = []
    all_rows = []

    for row in csvreader:

# Changing Profit/Losses column into integer        
        cleanup = row
        cleanup[1] =  int(cleanup[1])
        
        all_rows.append(cleanup)

# length of all data/ # of months
total_month = len(all_rows)
print(total_month)

# total of profit/losses
net_total = sum(row[1] for row in all_rows)
print(net_total)

# to loop through each rows to calculate the change in profit/losses
for i in range(len(all_rows)-1):
    current_profit = all_rows[i][1]
    next_profit = all_rows[i +1][1]
    changes = next_profit - current_profit
    monthly_changes.append(changes)

# total changes of profit/losses for each month
    average_changes = (sum(monthly_changes)/len(monthly_changes))
print(average_changes)

# finding greatest increase and decrease in change of profit/losses
max_change = max(monthly_changes) 
min_change = min(monthly_changes)
print(max_change)
print(min_change)

# return the month for min and max
max_index = monthly_changes.index(max_change) + 1
min_index = monthly_changes.index(min_change) + 1
month_max = all_rows[max_index][0]
month_min = all_rows[min_index][0]
print(month_max)
print(month_min)


# export file to a txt file
out_path = "pybank-txt"
with open(out_path, "w") as f:
    f.write(f"Financial Analysis\n")
    f.write(f"------------------\n")
    f.write(f"Total Months: {total_month}\n")
    f.write(f"Total: ${net_total}\n")
    f.write(f"Average Change: ${round(average_changes,2)}\n")
    f.write(f"Greatest Increase in Profits: {month_max} (${max_change})\n")
    f.write(f"Greatest Decrease in Profits: {month_min} (${min_change})\n")
