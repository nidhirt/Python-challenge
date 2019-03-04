
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
    
    profit_tracker = []
    first_row = 'y'
    month_tracker = []
  
    for row in budgetreader:
        
        change = int(row[1])
        count = count + 1
        # print("Row 1 ", type(row[1]))
        Net_amount = Net_amount + int(row[1]) #because row[1] always returns a string #list of strings
        # print(Net_amount)
        

        while first_row == "y":
            
           count = count + 1
           Net_amount = Net_amount + int(row[1])
           
           change = int(row[1])
           next(budgetreader) #skip the first row as teh value is considered in change
           first_row = 'n'

        difference = int(row[1]) - change # get the change
        profit_tracker.append(difference)
        month_tracker.append(row[0])

    print(f"profit_tracker , Month  :  {profit_tracker} ,  {month_tracker}")
       

    # loop for comparing the value of profit change 

    print(f" Total Months : {count}")
    print(f" Total Amount : {Net_amount}")

    #for index in profit_tracker:

       # profit = profit_tracker[index]
       # month =  month_tracker[index]
       # print(profit + "   " + month)


    #print({f" difference : {")
    #print(f" Greatest Increase in Profits :    ( {row[3]})")
    #print(f" Greatest Decrease in Profits :    ( {row[3]})")




