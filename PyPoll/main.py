import os
import csv
import pathlib

#access file here
election_data = os.path.join(pathlib.Path(__file__).parent.resolve(), "Resources", "election_data.csv")

# variables here; can start counters
vote_count = 0
percent_votes = []
candidates = []
num_votes = []
#start doing stuff here
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile) #, delimiter = "," do I need this?
    csv_header = next(csvreader)
    for row in csvreader:
        vote_count += 1 
#* The total number of votes cast
    #print(f"Total Votes: {vote_count}")


#  * A complete list of candidates who received votes
#loop through each line and find unique candidate names
    if row[2] not in candidates:
        candidates.append(row[2])
        index = candidates.index(row[2])
        num_votes.append(1)
    else:
        index = candidates.index(row[2])
        num_votes[index] += 1

#  * The percentage of votes each candidate won
#loop through rows and tally votes for each candidate
#translate to a percentage
#I can't figure this part out
    for votes in num_votes:
        percentage = (votes/vote_count) * 100
        percent_votes.append(percentage)

#  * The winner of the election based on popular vote.
#Determine candidate with most votes #????? also not right
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]
#print it all down here to look nicer
print("Election Results")
print("----------------")
print(f"Total Votes: {vote_count}")
print("----------------")
for i in range(len(candidates)):
    print(f"{candidates}: {percent_votes} ({num_votes})")   #??? I know I did this wrong
print("----------------")
print(f"Winner: {winning_candidate}")
print("----------------")

# Exporting to .txt file
with open('analysis.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('/n')
