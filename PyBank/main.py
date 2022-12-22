import os
import csv

print("Financial Analysis")
print("------------------------------")

Total_Months = 0
Total = 0
Average_Change = 0

# load csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#open csv file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        Total_Months = Total_Months + 1
        Total = Total + int(row[1])
        
    Average_Change = Total / Total_Months

    print("Total Months: " + str(Total_Months))
    print("Total: " + str(Total))  
    print("Average Change: " + str(Average_Change)) 

  








