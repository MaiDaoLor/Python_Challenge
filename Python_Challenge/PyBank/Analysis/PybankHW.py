#In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#   1. The total number of months included in the dataset
#   2. The net total amount of "Profit/Losses" over the entire period
#   3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
#   4. The greatest increase in profits (date and amount) over the entire period
#   5. The greatest decrease in profits (date and amount) over the entire period


#Import os and csv file from Module 3 
import os
import csv

# Path to collect data from the resource
data_budget_csv =  os.path.join("PyBank/Resources/budget_data.csv")

monthcount = 0
totalvolume = 0
greatestincrease = 0
bestmonth = ''
greatestdecrease = 0
worstmonth = ''

with open(data_budget_csv) as csvfile:
    csv.reader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first
    csv_header = next(csv.reader)
    print(f"CSV Header: {csv_header}")

    for row in csv.reader:
        monthcount +=1
        totalvolume += int(row[1])
        if int(row[1]) > greatestincrease:
            worstmonth = (row[0])
            greatestdecrease = int(row[1])
            change.append(int(row[1]))
        
# Count total months 
column_a = ws['A']

# For loop for total months
for cell in column


#Create header for data_budget_csv
#Print Header
print("Financial Analysis")

print("---------------------------------------------")

#Print out data results 
print("Total Months:" + str(monthcount))
print("Total: $" + str(totalvolume))
print("Average Change: $" + st(round(averageChange, 2)))
print("Greatest Increase in Profits:" + str(bestmonth) + "($" + str(greatestincrease) + ")")
print("Greatest Decrease in Profits:" + str(worstmonth) + "($" + str(greatestdecrease) + ")")

