
import os
import csv
#Define variables
rowcount = 0
rowsum = 0
rowbegin = 0
average_change = 0
rowmax = 0
rowmin = 0

# Set path for file
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    
    
    # Read each row of data after the header
    for row in csvreader:
      
        #count each row (month) for the dataset to find total number of months
        rowcount = rowcount + 1

        #Find net profit/loss by adding the amount for each row
        rowsum = rowsum + float(row[1])

        #find first datapoint for the average
        if rowcount == 1:
            rowbegin = float(row[1])

        #Find maximum profit for the dataset
        if float(row[1]) >= rowmax:
            rowmax = float(row[1])
            rowhead = row[0]

        #Find maximum loss for the dataset
        if float(row[1]) <= rowmin:
            rowmin = float(row[1])
            rowheadmin = row[0]

#Calculate average change
average_change = (float(row[1]) - rowbegin) / rowcount

#Print results to terminal
print("Financial Analysis")
print("---------------------------------------------------------------------")
print(f"The amount of months is: {rowcount}")
print(f"The net profit/loss is: ${rowsum}")
print(f"The average change is: ${average_change}")
print(f"Greatest increase in profits: {rowhead} ${rowmax}")
print(f"The greatest loss in profits: {rowheadmin} ${rowmin}")
print("---------------------------------------------------------------------")

output_path = os.path.join(os.path.dirname(__file__), "Analysis", "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the content
with open(output_path, "w", encoding="utf-8") as textfile:
    
    # Print info to text file
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------------------------------\n")
    textfile.write(f"The amount of months is: {rowcount}\n")
    textfile.write(f"The net profit/loss is: ${rowsum}\n")
    textfile.write(f"The average change is: ${average_change}\n")
    textfile.write(f"Greatest increase in profits: {rowhead} ${rowmax}\n")
    textfile.write(f"The greatest loss in profits: {rowheadmin} ${rowmin}\n")
    textfile.write("----------------------------------------------------\n")
   
   
   

    
