# The data we need to retrieve.

import csv
import os

# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable for the file to load and the path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter. 

total_votes = 0

# Candidate Options

candidate_options = []

# Declare empty dictionary

candidate_votes = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file

with open(file_to_load) as election_data:

# to do: read and analyze the data here.

    # Read the file object wiht the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row

    headers = next(file_reader)
  
    # Print each row in the CSV file

    for row in file_reader:

        # 2. Add the total vote count
        total_votes += 1

        # Print the candiate name from each row
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate ...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking candidates votes count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Save the results to our text file. 
    with open(file_to_save, "w") as txt_file:
        
        election_results = (
            f"\nElection Results\n"
            f"------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")

        print(election_results, end="")

    #Save the final vote count to the text file
        txt_file.write(election_results)


    # Percentage of votes for each candidate

    # 1. Iterate through the candidate list. 

        for candidate_name in candidate_votes:

        # 2. Retrieve vote count of a candidate

            votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes. 

            vote_percentage = float(votes)/ float(total_votes) * 100   

            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")  
            
            print(candidate_results)

            txt_file.write(candidate_results)


    # Determine winning vote count and candidate
    # Determine if the vote is greater than the winning count. 

            if(votes >= winning_count) and (vote_percentage >= winning_percentage):

                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

# To do: print out the winning candidate, vote count and percentage to terminal 

        

        winning_candidate_summary = (
            f"-------------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"--------------------------------------\n")

                
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
