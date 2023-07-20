#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

#   1.The total number of votes cast
#   2.A complete list of candidates who received votes
#   3.The percentage of votes each candidate won
#   4.The total number of votes each candidate won
#   5.The winner of the election based on popular vote

# Import os and csv file from Module 3
import os
import csv

# Path to collect data from Resource
election_data_csv = os.path.join("PyPoll/Resources/election_data.csv")

totalcount = 0
candidatelist = ''
uniquecandidate = ''
vote_count = 0
vote_percent = 0

with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Conduct the ask

    for row in csvreader:
        # Count the total number of votes

# Create header for election_data.csv
#Print header
print("Election Results")   
print("---------------------------------")
print("Total Votes :" + str(count))    

print("----------------------------------")

print("The winner is: ")

print("-------------------------")
