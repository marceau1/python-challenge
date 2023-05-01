# decalration of path to get access to the resources

# importing modules
import os
import csv

# creating the path to access the database
budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")
# PyBank/Resources/budget_data.csv
# create a list of variable
financial_list = []
total_amount_list_net = []
change_profit_lost_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9000000000000]
total_net = 0
month_of_change = []
total_month = 0
# net_change_list
#reading the csv_file
with open (budget_data, 'r') as csv_data:
    data_reader = csv.reader(csv_data, delimiter=",")

    header = next(data_reader)
    first_row = next(data_reader)
    total_month += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    for row in data_reader:
        # Track the total
        total_month += 1
        total_net += int(row[1])
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        total_amount_list_net += [net_change]
        month_of_change += [row[0]]
        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
  
    net_total = sum(total_amount_list_net)
    net_montly_avg = sum(total_amount_list_net)/len(total_amount_list_net)


    #print result to the terminal 
    print("FIANACIAL ANALYSIS")
    print("-----------------------")
    print(f"Total of Months: {total_month}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${net_montly_avg}")
    print(f"Greatest increase in profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest drecrease in profits: {greatest_decrease[0]}(${greatest_decrease[1]})")

#white the resulte to  a text file (.txt)

budget_output = os.path.join("PyBank/analysis/budget_data.txt")


with open (budget_output, 'w') as csvfile:
    resultswriter = csv.writer(csvfile)

#print the election result to the csv file
                  
    resultswriter.writerow(["FIANACIAL ANALYSIS"])
    resultswriter.writerow(["-----------------------"])
    resultswriter.writerow([f"Total of Months: {total_month}"])
    resultswriter.writerow([f"Total: ${net_total}"])
    resultswriter.writerow([f"Average Change: ${net_montly_avg}"])
    resultswriter.writerow([f"Greatest increase in profits: {greatest_increase[0]}(${greatest_increase[1]})"])
    resultswriter.writerow([f"Greatest drecrease in profits: {greatest_decrease[0]}(${greatest_decrease[1]})"])
    

   
    
