
import os
import csv
import re


#set the path

pollcsvpath = os.path.join(".", "Resources", "election_data.csv")
outputpath = os.path.join(".", "output.txt")  #output file

#open the file and assign it to pollfile

with open (pollcsvpath,newline="") as pollfile:

    pollreader = csv.reader(pollfile, delimiter = ",")
    header = next(pollreader)

    count=0
    candidate = []
    votes = []
    unique = []
    index = 0

    
    for row in pollreader: # get the unique candidates in a list
        count+=1
        candidate.append(row[2])
   
        if (row[2]) not in unique:
                
            unique.append(row[2])

    print(f" \n Election Results")
    print(f"--------------------------------")
    print(f" Total Votes :  {count} ")
    print(f"---------------------------------\n")

with open(outputpath,"w") as output_file:
    
    output_file.write (

    f" \n Election Results \n"
    f"---------------------------------\n"
    f" Total Votes :  {count} \n"
    f"---------------------------------\n")



    #print(f" unique values are   {unique}")

    for j in range(len(unique)):

        vote_count = candidate.count(unique[j])
        votes.append(vote_count)
        percent_votes = "{:.3f}".format((vote_count/len(candidate)*100))

        output_file.write(f" \n {unique[j]} :   {percent_votes}%   ({vote_count})\n  ")
        print(f" {unique[j]} :   {percent_votes}%   ({vote_count})  ")

    winner = votes.index(max(votes))

    output_file.write(

    f" \n---------------------------------\n"

    f" Winner  :    {unique[winner]} \n"

    f"---------------------------------\n")

    print(f"---------------------------------")
    print(f" Winner  :    {unique[winner]}")
    print(f"---------------------------------")


    #for i in range(len(candidate)): 

        #if candidate[i] in unique:

            #vote_count = int(unique.index(candidate[i]))
            #votes[vote_count] = votes[vote_count] + 1
         

