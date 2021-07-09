# import dependencies
import os
import csv

import collections
from collections import Counter

# list to store data
all_vote = []
unique_candidates = []
vote_candidate = []
alpha_candidates = []

# set variables
correy_count = 0
khan_count = 0
li_count = 0
ot_count = 0


# FIGURE OUT THE FILEPATH ON YOUR COMPUTER
csvpath = "PyPoll\Resources\election_data.csv"


# read in the CSV data into memory - a list of lists
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

# exclude header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# to store vote count
    row = csv_header
    
    # count number of votes
    for row in csvreader:
        vote = row
    
        all_vote.append(vote)
        unique_candidates.append(row[2])

    # to alphabetized by candidates name      
    alpha_candidates = sorted(unique_candidates)
    
    # to count the votes per candidates and store it to new variable
    count_votes = Counter (alpha_candidates)
    vote_candidate.append(count_votes)

    # vote_candidate contains number of votes from candiate, but could not pull data from location
    print(vote_candidate)

    # alternate method to count votes per candidate for math
    for line in alpha_candidates:
            if line == "Correy":
                correy_count = correy_count + 1
            elif line == "Khan":
                khan_count = khan_count + 1
            elif line == "Li":
                li_count = li_count + 1
            else:
                ot_count = ot_count + 1

    
# total number of vote
    vote_count = len(all_vote)

# setting variables
correy_percent = 0
khan_percent = 0
li_percent = 0
ot_percent = 0

# calculate percentage of vote
correy_percent = format(correy_count * 100 / vote_count,".3f")
khan_percent = format(khan_count * 100 / vote_count,".3f")
li_percent = format(li_count * 100 / vote_count,".3f")
ot_percent = format(ot_count * 100 / vote_count,".3f")


# attempt to pull data from vote_candidate but unsuccessful
# print(f"{vote_candidate[0][0]}: {correy_percent}% ({vote_candidate[0][1]})")
# print(f"{vote_candidate[1][0]}: {khan_percent}% ({vote_candidate[1][1]})")
# print(f"{vote_candidate[2][0]}: {li_percent}% ({vote_candidate[2][1]})")
# print(f"{vote_candidate[3][0]}: {ot_percent}% ({vote_candidate[3][1]})")

# set to store data
winner = []

# find winner
if correy_count > khan_count and correy_count > li_count and correy_count > ot_count:
    winner = "Correy"
elif khan_count > correy_count and khan_count > li_count and khan_count > ot_count:
    winner = "Khan"
elif li_count > correy_count and li_count > khan_count and li_count > ot_count:
    winner = "Li"
else:
    winner = "O'Tooley"

#print in terminal
print(f"\nElection Results\n")
print(f"------------------\n")
print(f"Total Votes: {vote_count}\n")
print(f"------------------\n")
print(f"Correy: {correy_percent}% ({correy_count})\n")
print(f"Khan: {khan_percent}% ({khan_count})\n")
print(f"Li: {li_percent}% ({li_count})\n")
print(f"O'Tooley: {ot_percent}% ({ot_count})\n")
print(f"------------------\n")
print(f"Winner: {winner}\n")
print(f"------------------\n")

# print out to text file
out_path = "pypoll-txt"
with open(out_path, "w") as f:
    f.write(f"Election Results\n")
    f.write(f"------------------\n")
    f.write(f"Total Votes: {vote_count}\n")
    f.write(f"------------------\n")
    f.write(f"Correy: {correy_percent}% ({correy_count})\n")
    f.write(f"Khan: {khan_percent}% ({khan_count})\n")
    f.write(f"Li: {li_percent}% ({li_count})\n")
    f.write(f"O'Tooley: {ot_percent}% ({ot_count})\n")
    f.write(f"------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write(f"------------------\n")
