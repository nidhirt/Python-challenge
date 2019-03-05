import os
import csv


#set the path

budgetcsvpath = os.path.join(".", "Resources", "budget_data.csv")
outputpath = os.path.join(".", "Analysis", "output.csv")  #output file
#print(budgetcsvpath)

#open the file and assign it to budgetfile

with open (budgetcsvpath,newline="") as budgetfile:

    budgetreader = csv.reader(budgetfile, delimiter = ",")

    budgetheader = next(budgetreader)

    #print(f"budget header : {budgetheader}")

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
        
            difference = 0
           

            index += 1
        else:
            index_tracker = index-1 #0 for jan #1 for feb
            difference = int(row[1]) - int(profitloss[index_tracker]) # for jan - 867884-867884 index[0]
            profit_tracker.append(difference) #[0,116771,]
            month_tracker.append(row[0]) #[jan-10, feb-10, mar-10, apr-10,...]
            index += 1 #2


    #print(f"profit_tracker , Month  :  {profit_tracker} ,  {month_tracker}")
       
    avg_change = round((sum(profit_tracker)/float(len(profit_tracker))),2)
    min_value = min(profit_tracker)
    min_valueindex = int(profit_tracker.index(min_value)) # get index of min value
    min_valuemonth = month_tracker[min_valueindex] #get month with min value change index
    
    max_value = max(profit_tracker) 
    max_valueindex = int(profit_tracker.index(max_value))#get index of max change
    max_valuemonth = month_tracker[max_valueindex] #get max value change month

    # loop for comparing the value of profit change 

    Output = (
    f"\nFinancial Analysis\n"
    f"-------------------------------------\n"
    f"  Total Months : {count}\n"
    f"  Total Amount : {Net_amount}\n"
    f"  Average Change : {avg_change}\n"
    f"  Greatest increase in Profits  : {max_valuemonth}    (${max_value})\n"
    f"  Greatest decrease in Profits  : {min_valuemonth}    (${min_value})\n"
    )
    print(Output)

with open(outputpath,"w") as output_file:
        output_file.write(Output)
    






