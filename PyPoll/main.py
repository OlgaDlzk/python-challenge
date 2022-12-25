import os
import csv

print("Election Results")
print("---------------------")

# load csv file
csvpath = os.path.join('Resources', 'election_data.csv')
# create output file
outputfile = os.path.join('analysis', 'election_data.txt')

# set up variables
# amount of total rows, not uncluding the header
total_vote = 0

# dict with key-value pair candidate: number of votes
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
print("----------------------------------")

# use for loop t loop through the dict and tuple unpacking to gain
# more control over key-value pair
for key, value in candidates_list.items():
    print(key + ": " + "{:.3f}".format(value/total_vote*100) + "% (" + str(value) + ")")
    
    # determine the popular vote winner
    if value > popular_votes:
        popular_votes = value
        winner = key 

print("----------------------------------")
print("Winner: " + winner)
print("-----------------------------------")

# printing data in txt file
with open(outputfile, "w") as file:
    file.write("Election Results \n")
    file.write("\n---------------------- \n")
    file.write("\nTotal Votes: " + str(total_vote) + " \n")
    file.write("\n---------------------- \n")
    file.write("\n")

    for key, value in candidates_list.items():
        file.write(key + ": " + "{:.3f}".format(value/total_vote*100) + "% (" + str(value) + ")")
        file.write("\n")
        
    file.write("\n---------------------- \n")
    file.write("Winner: " + winner)
    file.write("\n---------------------- \n")
    