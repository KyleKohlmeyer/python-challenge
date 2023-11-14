
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
csvpath = os.path.join(os.path.dirname(__file__), "..", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header
    for row in csvreader:
        print(row)
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
print(f"The amount of months is: {rowcount}")
print(f"The net profit/loss is: ${rowsum}")
print(f"The average change is: ${int(average_change)}")
print(f"The maximum profit is {rowhead} ${rowmax}")
print(f"The greatest loss is {rowheadmin} ${rowmin}")

output_path = os.path.join(os.path.dirname(__file__), "..", "resources", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------------------------------'])
    csvwriter.writerow([f'The amount of months is: {rowcount}'])
    csvwriter.writerow([f'The net profit/loss is: ${rowsum}'])
    csvwriter.writerow([f'The average change is: ${average_change}'])
    csvwriter.writerow([f'Great increase in profits: {rowhead} ${rowmax}'])
    csvwriter.writerow([f'Greateast loss in profits: {rowheadmin} ${rowmin}'])

    
