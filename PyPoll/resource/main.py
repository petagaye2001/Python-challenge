# Objective: helping a small rural town modernize its vote counting process.
# Store the file path associated with the file in the set of poll data called election_data.csv. 
import os
import numpy
import csv

electiondata_file = 'election_data.csv'

count = 0
candidatelist =[]
unique_candidate = []
vote_count = []
vote_percent = []

#The dataset is composed of three columns: Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:

# Open the file in "read" mode ('r') and store the content
with open(electiondata_file, 'r') as text:
    csvreader = csv.reader(electiondata_file, delimiter=",")
    csv_header = next(csvreader)
# Conduct the ask
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        #candidatelist.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")




# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.