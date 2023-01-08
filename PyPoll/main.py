# decalration of path to get access to the resources

import os
import csv
# delclaration of a variables 

csvpath = os.path.join("Resources","election_data.csv")

total_num_vote = 0
list_of_candidats = []
dictionnariy_candidats = {}
#candidate_name = row[0]

#def display

with open(csvpath) as election:
    csvreader = csv.reader(election, delimiter=',')

    header = next(csvreader)
   # print(csvreader)
    for row in csvreader:
        total_num_vote += 1

        candidat_name = row[2]
#create a condition to add candidate name to candidate dictionnary

        if candidat_name not in list_of_candidats:
            list_of_candidats.append(candidat_name)
            dictionnariy_candidats[candidat_name] = 0
            
        dictionnariy_candidats[candidat_name] = dictionnariy_candidats[candidat_name] + 1
#create a variable that will sotre the percentage
    percentage = []
#creation of a fot loop to determine the values in percentage
    for value in dictionnariy_candidats.values():
        percentage.append((value*100)/total_num_vote)

#create election resultss
#create a list to the dictionnary to get the values
    poll_list = list(dictionnariy_candidats)
#determine the winner
    election_winner = max(dictionnariy_candidats, key = dictionnariy_candidats.get)


# print final result

print("---------------------------")

print("FINAL RESULTS\n")

print(f"Total  number of votes :{total_num_vote}\n")
print(f"{list_of_candidats[0]}: {round(percentage[0], 3)}% ({dictionnariy_candidats[poll_list[0]]})\n")
print(f"{list_of_candidats[1]}: {round(percentage[1], 3)}% ({dictionnariy_candidats[poll_list[1]]})\n")
print(f"{list_of_candidats[2]}: {round(percentage[2], 3)}% ({dictionnariy_candidats[poll_list[2]]})\n")
print(f"The winner is: {election_winner}\n")

#white the resulte to  a text file (.txt)

csvpath = os.path.join("analysis/election_data.txt")
with open (csvpath, 'w') as txt_file:
#print the election result to the csv file
    election_result_txt = (
                      f"(FINAL RESULTS\n)"
                      f"Total  number of votes :{total_num_vote}\n"
                      f"{list_of_candidats[0]}: {round(percentage[0], 3)}% ({dictionnariy_candidats[poll_list[0]]})\n"
                      f"{list_of_candidats[1]}: {round(percentage[1], 3)}% ({dictionnariy_candidats[poll_list[1]]})\n"
                      f"{list_of_candidats[2]}: {round(percentage[2], 3)}% ({dictionnariy_candidats[poll_list[2]]})\n"
                      f"The winner is: {election_winner}\n"
                      )
    

    txt_file.write(election_result_txt)
