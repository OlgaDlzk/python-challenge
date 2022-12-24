import os
import csv

print("Financial Analysis")
print("------------------------------")

Total_Months = 0
Total = 0
Delta_list = []
Month = []
Average = 0
GreatestIncrease = 0
BestMonth = " "
GreatestDecrease = 0
WorstMonth = " "

# Max_Increase = ["", 0]
# Max_Decrease = ["", 9999999999]


# load csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
# create output file
outputfile = os.path.join('analysis', 'budget_analysis.txt')

#open csv file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)
    firstrow = next(csvreader)

    Total_Months += 1
    Total += int(firstrow[1])
    Previous = int(firstrow[1])

    # 
    for row in csvreader:
        Total_Months = Total_Months + 1
        Total = Total + int(row[1])    
        Delta = int(row[1]) - Previous
        Previous = int(row[1])
        Delta_list.append(Delta)
        Month.append(row[0])
        Average = round(sum(Delta_list)/len(Delta_list), 2)

        if Delta > GreatestIncrease:
                BestMonth = (row[0])
                GreatestIncrease = Delta

        if Delta < GreatestDecrease:
                WorstMonth = (row[0])
                GreatestDecrease = Delta
        
                
        # if Delta > Max_Increase[1]:
           # Max_Increase[0] = row[0]
            # Max_Increase[1] = Delta

        # if Delta < Max_Decrease[1]:
            # Max_Decrease[0] = row[0]
            # Max_Decrease[1] = Delta
            

print("Total Months: " + str(Total_Months))
print("Total: " + "$" + str(Total)) 
print("Average Change: " + "$" + str(Average)) 
print("Greatest increase in profits: " + BestMonth + " ($"+ str(GreatestIncrease) + ")")
print("Greatest decrease in profits: " + WorstMonth + " ($"+ str(GreatestDecrease) + ")")
# print("Greatest Increase in Profits: " + str(Max_Increase))
# print("Greatest Decrease in Profits: " + str(Max_Decrease))

outputfile = open("budget_analysis.txt", "w")
outputfile.write("Financial Analysis \n")

outputfile.write("---------------------- \n")

outputfile.write("Total Months: " + str(Total_Months))
outputfile.write(" \nTotal: " + "$" + str(Total))
outputfile.write(" \nAverage Change: " + "$" + str(Average))
outputfile.write(" \nGreatest increase in profits: " + BestMonth + " ($"+ str(GreatestIncrease) + ")")
outputfile.write(" \nGreatest decrease in profits: " + WorstMonth + " ($"+ str(GreatestDecrease) + ")")


outputfile.close()
    
   


  








