#PyPoll
import os 
import csv
poll_data_csv = "Resources/election_data.csv"

#Initialize variables
total_votes = 0 
charles_count = 0
diana_count = 0
raymon_count = 0 
#Create dictionary to story voter counts
candidate_totals = {"Charles Casper Stockam":[],
                    "Diana DeGette":[],
                    "Raymon Anthony Doane": []}


#Open the CSV file
with open(poll_data_csv, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
#Read through every row in csv file
    for row in csvreader:
#count the number of row and store it in total_votes
        total_votes += 1 
#identify the candidates
        candidate = str(row[2])
#For every candidate that matches with the candidate name, add to the count of how many voters that candidate received
#Then add the voter count for that candidate into list in the candidate_totals dictionary
        if candidate == "Charles Casper Stockham":
            charles_count += 1
            candidate_totals["Charles Casper Stockam"].append(charles_count)
        if candidate == "Diana DeGette":
            diana_count += 1
            candidate_totals["Diana DeGette"].append(diana_count)
        if candidate == "Raymon Anthony Doane":
            raymon_count += 1
            candidate_totals["Raymon Anthony Doane"].append(raymon_count)
        
        
#Calculate percentages for each candidate
charles_percentage = round(((charles_count/total_votes) * 100),3)
diana_percentage = round(((diana_count/total_votes) * 100),3)
raymon_percentage = round(((raymon_count/total_votes) * 100), 3)

#https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
#Obtain the name of the winner from the dictionary
winner = max(candidate_totals, key=lambda x: len(candidate_totals[x]))

#Function to print each result
def pypoll_results():
    print(f"Total Votes: {total_votes}")
    print(f"Charles Casper Stockham: {charles_percentage}% ({charles_count})")
    print(f"Diana DeGette: {diana_percentage}% ({diana_count})")
    print(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_count})\n")
    print(f"Winner: {winner}\n")

pypoll_results()


#Write to a txt file
pypoll_txt = open("pypoll.txt", "w")
pypoll_txt.write("Election Results\n")
pypoll_txt.write("-------------------------------------------\n")
pypoll_txt.write(f"Total Votes: {total_votes}\n")
pypoll_txt.write("-------------------------------------------\n")
pypoll_txt.write(f"Charles Casper Stockham: {charles_percentage}% ({charles_count})\n")
pypoll_txt.write(f"Diana DeGette: {diana_percentage}% ({diana_count})\n")
pypoll_txt.write(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_count})\n")
pypoll_txt.write("-------------------------------------------\n")
pypoll_txt.write(f"Winner: {winner}\n")
pypoll_txt.write("-------------------------------------------\n")
pypoll_txt.close()
