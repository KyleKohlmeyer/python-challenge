import os
import csv
# Define variables
votetotal = 0
cand1total = 0
cand2total = 0
cand3total = 0
cand1per = 0
cand2per = 0
cand3per = 0
winvotes = 0

# Make dictionary to store the three candidates and their votes (their totals will be added later)
candinfo = {"candidate": ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane" ],
           "candvotes": {"Placeholder"}}

# Set path for file
csvpath = os.path.join(os.path.dirname(__file__), "..", "Resources", "election_data.csv")

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
        # Set variable to find out which votes belong to which candidates
        cand = str(row[2])

        # Find total votes
        votetotal = votetotal + 1

        # Using the variable above, find which candidate this vote is for and add it to their totals
        if cand == str("Charles Casper Stockham"):
            cand1total = cand1total + 1
        if cand == str("Diana DeGette"):
            cand2total = cand2total + 1
        if cand == str("Raymon Anthony Doane"):
            cand3total = cand3total + 1

# Create list to add the vote totals to the candidate dictionary
votelist = [cand1total, cand2total, cand3total]
candinfo["candvotes"] = votelist

# Find percentage and format it using format function (function is common knowledge)
cand1per = "{:.2%}".format(cand1total/votetotal)
cand2per = "{:.2%}".format(cand2total/votetotal)
cand3per = "{:.2%}".format(cand3total/votetotal)

# Print result header to the terminal
print("ELection Results")
print("-----------------------------------------------------")
# Print total votes to terminal
print(f"Total votes: {votetotal}")
print("-----------------------------------------------------")
# Print each candidates information to the terminal
print(f' {candinfo["candidate"][0]} {candinfo["candvotes"][0]} votes ({cand1per}) ')
print(f' {candinfo["candidate"][1]} {candinfo["candvotes"][1]} votes ({cand2per})')
print(f' {candinfo["candidate"][2]} {candinfo["candvotes"][2]} votes ({cand3per})')
print("-----------------------------------------------------")

# Find the max amount of votes and compare them to the candidate totals to find winner
if max(votelist) == cand1total:
    candwinner = candinfo["candidate"][0]
    winvotes = cand1total
if max(votelist) == cand2total:
    candwinner = candinfo["candidate"][1]
    winvotes = cand2total
if max(votelist) == cand3total:
    candwinner = candinfo["candidate"][2]
    winvotes = cand3total

# Print winner to terminal
print(f'{candwinner} won the election with {winvotes} votes')
print("-----------------------------------------------------")

# Set file path for printing to new file
output_path = os.path.join(os.path.dirname(__file__), "..", "resources", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows in the new file
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['----------------------------------------------------'])
    csvwriter.writerow([f'The total votes cast in the election: {votetotal} votes'])
    csvwriter.writerow(['----------------------------------------------------'])
    csvwriter.writerow([f'{candinfo["candidate"][0]} received {candinfo["candvotes"][0]} votes ({cand1per})'])
    csvwriter.writerow([f'{candinfo["candidate"][1]} received {candinfo["candvotes"][1]} votes ({cand2per})'])
    csvwriter.writerow([f'{candinfo["candidate"][2]} received {candinfo["candvotes"][2]} votes ({cand3per})'])
    csvwriter.writerow(['----------------------------------------------------'])
    csvwriter.writerow([f'{candwinner} won the election with {winvotes} votes'])
    csvwriter.writerow(['----------------------------------------------------'])