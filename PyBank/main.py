import os
import csv

#set the path

budgetcsvpath = os.path.join(".", "Resources", "budget_data.csv")
print(budgetcsvpath)

#open the file and assign it to budgetfile

with open (budgetcsvpath,newline="") as budgetfile:

    budgetreader = csv.reader(budgetfile, delimiter = ",")

    budgetheader = next(budgetreader)

    print(f"budget header : {budgetheader}")

    count = 0 #to count the number of months
    Net_amount = 0
    change = int()
    counter = 0
    profit_tracker = []

    for row in budgetreader:
        
        count = count + 1
        # print("Row 1 ", type(row[1]))
        Net_amount = Net_amount + int(row[1]) #because row[1] always returns a string #list of strings
        # print(Net_amount)
        #difference = int(row[1]) - change
        #profit_tracker.append(difference)


    print(f" Total Months : {count}")
    print(f" Total Amount : {Net_amount}")
    #print(f" Greatest Increase in Profits :    ( {row[3]})")
    #print(f" Greatest Decrease in Profits :    ( {row[3]})")

