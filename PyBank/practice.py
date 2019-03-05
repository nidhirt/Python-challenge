
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
    profitloss =[]
    index =0
  
    for row in budgetreader:
        
        change = int(row[1]) #is for feb-10 984655
        profitloss.append(change) #[867884, 984655, 322013]
        count = count + 1 #1 for jan

        # print("Row 1 ", type(row[1]))
        Net_amount = Net_amount + int(row[1]) #because row[1] always returns a string #list of strings
        # print(Net_amount)
        
        if index ==0:
            index_tracker = 0
            #difference = int(row[1]) - int(profitloss[index_tracker]) # for jan - 867884-867884 index[0]
            difference = 0
            #profit_tracker.append(difference) #[0,116771,]
            #month_tracker.append(row[0]) #[jan-10, feb-10, mar-10, apr-10,...]

            index += 1
        else:
            index_tracker = index-1 #0 for jan #1 for feb
            difference = int(row[1]) - int(profitloss[index_tracker]) # for jan - 867884-867884 index[0]
            profit_tracker.append(difference) #[0,116771,]
            month_tracker.append(row[0]) #[jan-10, feb-10, mar-10, apr-10,...]
            index += 1 #2


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




