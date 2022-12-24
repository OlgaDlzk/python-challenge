import os
import csv

print("Election Results")
print("------------------------------")

Total_Votes = 0


# load csv file
csvpath = os.path.join('Resources', 'election_data.csv')
outputfile = os.path.join('analysis', 'election_analysis.txt')

#open csv file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csv_header:
        Total_Votes = Total_Votes + 1

    print("Total Votes: " + str(Total_Votes))    