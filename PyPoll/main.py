import os
import csv

print("Election Results")
print("---------------------")

# load csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# set up variables

# amount of total rows, not uncluding the header
total_vote = 0

# dict with key-value pair candidate: numer of votes
candidates_list = {}

# variables for the popular votes winner
popular_votes = 0
winner = ""

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    for row in csvreader:
        # total amount of rows - header row = total amoun of votes 
        total_vote +=1
        # all the key values in dic are nunique. 
        # So if candidate name is already added, it will skip that part and 
        # just will add +1 to the vote count for this candidate
        if row[2] not in candidates_list:
            candidates_list[row[2]] = 1
        else:
            candidates_list[row[2]] += 1    


print("Total Votes: "+ str(total_vote))
print(candidates_list)

