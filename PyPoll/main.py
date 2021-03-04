#Import required packages
import os 
import csv



#Files to load and output
PyPollfile_to_load = os.path.join("../Resources", "election_data.csv")
PyPollfile_to_output = os.path.join("PyPoll_analysis.txt")

#creating list

voterId = []
candidate_list = []
unique_candidate = []
result = []

#Read the csv 
with open(PyPollfile_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)



#looping through each row and storing the elements in a new list
    for row in reader:
        voterId.append(row[0])
        
        candidate_list.append(row[2])

        if row[2] not in unique_candidate:
            unique_candidate.append(row[2])

total_votes = len(voterId)

#creating dictionaries for vote count and percentage        
candidate_vote = {}.fromkeys(unique_candidate, 0 )
candidate_per = {}.fromkeys(unique_candidate, 0)
for  candidate in candidate_list:
        candidate_vote[candidate] += 1
        candidate_per[candidate] = '{: .3%}'.format(( candidate_vote[candidate] / total_votes ) )
        
output = (
    f"\nElection Results\n"
    f"----------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------------------------\n")

for key in candidate_vote:
    output += (f"{key}: {candidate_per[key]} ({(candidate_vote[key])})\n")


winner = max(candidate_vote, key = candidate_vote.get)

#print(len(unique_candidate))
#print(candidate_vote)

#print(candidate_per)
#print(result)

# Generate Election Results Output

output += (f"-----------------------------------\n"
    f"Winner: {winner}  \n"
    f"-----------------------------------\n")
   


    
        
    

# Print all of the results (to terminal)
print(output)


# Save the results to analysis text file
with open(PyPollfile_to_output, "a") as txt_file:
    txt_file.write(output)
