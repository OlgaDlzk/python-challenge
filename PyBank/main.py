import os
import csv

print("Financial Analysis")
print("------------------------------")

# creating variables 
Total_Months = 0
Total = 0
Delta_list = []
Month = []
Average = 0
GreatestIncrease = 0
BestMonth = " "
GreatestDecrease = 0
WorstMonth = " "

# load csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
# create output file
outputfile = os.path.join('analysis', 'budget_analysis.txt')

#open csv file
with open(csvpath) as csvfile:

    # CSV reader specifies variable that holds contents
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)
    firstrow = next(csvreader)

    Total_Months += 1
    Total += int(firstrow[1])
    Previous = int(firstrow[1])

    # looping through each row to calculate needed parameters
    for row in csvreader:
        Total_Months = Total_Months + 1
        Total = Total + int(row[1])    
        Delta = int(row[1]) - Previous
        Previous = int(row[1])
        Delta_list.append(Delta)
        Month.append(row[0])
        Average = round(sum(Delta_list)/len(Delta_list), 2)
        # determining greatest deacrease and greatest increase
        if Delta > GreatestIncrease:
                BestMonth = (row[0])
                GreatestIncrease = Delta

        if Delta < GreatestDecrease:
                WorstMonth = (row[0])
                GreatestDecrease = Delta                   

print("Total Months: " + str(Total_Months))
print("Total: " + "$" + str(Total)) 
print("Average Change: " + "$" + str(Average)) 
print("Greatest increase in profits: " + BestMonth + " ($"+ str(GreatestIncrease) + ")")
print("Greatest decrease in profits: " + WorstMonth + " ($"+ str(GreatestDecrease) + ")")

# printing data in txt file
with open(outputfile, "w") as file:
    file.write("Financial Analysis \n")
    file.write("\n---------------------- \n")
    file.write("\nTotal Months: " + str(Total_Months))
    file.write("\nTotal: " + "$" + str(Total))
    file.write("\nAverage Change: " + "$" + str(Average))
    file.write("\nGreatest increase in profits: " + BestMonth + " ($"+ str(GreatestIncrease) + ")")
    file.write("\nGreatest decrease in profits: " + WorstMonth + " ($"+ str(GreatestDecrease) + ")")

   


  








