import os
import csv
# Create empty lists
candidates = []
votetotals = []
votes = []

# Set path for file
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
  
        # Set variable to find out whether a candidate is unique and store who the vote is for
        cand = row[2]
        votes.append(cand)

        # Add new candidates and their votetotals to the list if they have not been added yet
        if cand not in candidates: 
            candidates.append(cand)
            votetotals.append(0)

# For loop to determine which candidate the vote belongs to and add it to that candidates vote total
for vote in votes:
    for i in range(len(candidates)):
        if vote == candidates[i]:
            votetotals[i] += 1

# Finding the maximum amount of votes from all candidates vote totals
mostvotes = max(votetotals)

# For loop for finding winner and storing winner as variable
for i in range(len(votetotals)):
        if mostvotes == votetotals[i]:
            winner = candidates[i] 

# Finding the total votes
totalvotes = sum(votetotals)

# Printing to terminal
print("Election Results\n")
print("----------------------------------------------------\n")
print(f"The total votes cast in the election: {totalvotes} votes\n")
print("----------------------------------------------------\n")

# For loop to print each candidate, the votes they received, and the percentage of the total they received
for i in range(len(candidates)):
        percent = "{:.2%}".format(votetotals[i] / totalvotes)
        print(f"{candidates[i]} received {votetotals[i]} votes ({percent} of the votes)\n")

# Printing the winner
print("----------------------------------------------------\n")
print(f"The winner is {winner}\n")
print("----------------------------------------------------\n")

# # Set file path for printing to new file
output_path = os.path.join(os.path.dirname(__file__), "Analysis", "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the content
with open(output_path, "w", encoding="utf-8") as textfile:
    
    # Print info to text file (for loop same as above but writes instead of prints to terminal)
    textfile.write("Election Results\n")
    textfile.write("----------------------------------------------------\n")
    textfile.write(f"The total votes cast in the election: {str(totalvotes)} votes\n")
    textfile.write("----------------------------------------------------\n")
    for i in range(len(candidates)):
        percent = "{:.2%}".format(votetotals[i] / totalvotes)
        textfile.write(f"{str(candidates[i])} received {str(votetotals[i])} votes ({str(percent)} of the votes)\n")
    textfile.write("----------------------------------------------------\n")
    textfile.write(f"The winner is {str(winner)}\n")
    textfile.write("----------------------------------------------------\n")
  