# decalration of path to get access to the resources

# importing modules
import os
import csv

# creating the path to access the database
budget_data = os.path.join("Resources/budget_data.csv")

# create a list of variable
financial_list = []
total_amount_list_net = []
change_profit_lost_list = []

#reading the csv_file
with open (budget_data, 'r') as csv_data:
    data_reader = csv.reader(csv_data, delimiter=",")

    next(data_reader)
    #print("csv_reader")
    #first foor loop of the project to skip each row  
    for row in data_reader:
    
#assigning data to our vaviables
        financial_list.append(row[0])
        total_amount_list_net.append(int(row[1]))

#using of the second for loop in the project 
    for j in range(len(total_amount_list_net)-1):
        change_profit_lost_list.append(total_amount_list_net[j + 1])

    average_changes = round(sum(change_profit_lost_list)/len(change_profit_lost_list),2)

    #determine the greatest increase in profit
    greatest_increase = max(change_profit_lost_list)
    #determine the greatest decrease in profit
    graetest_decrease = min(change_profit_lost_list)
    #total number of months
    total_month = len(financial_list)
    net_total = sum(total_amount_list_net)

    increase_month_index = change_profit_lost_list.index(greatest_increase)+1


    decrease_moth_index = change_profit_lost_list.index(graetest_decrease)+1

    #print result to the terminal 
    print("FIANACIAL ANALYSIS")
    print("-----------------------")
    print(f"Total of Months: {total_month}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_changes}")
    print(f"Greatest increase in profits: {financial_list[increase_month_index]}(${greatest_increase})")
    print(f"Greatest drecrease in profits: {financial_list[decrease_moth_index]}(${graetest_decrease})")

#white the resulte to  a text file (.txt)

budget_output = os.path.join("analysis/budget_data.txt")


with open (budget_output, 'w') as csvfile:
    resultswriter = csv.writer(csvfile)

#print the election result to the csv file
                  
    resultswriter.writerow(["FIANACIAL ANALYSIS"])
    resultswriter.writerow(["-----------------------"])
    resultswriter.writerow([f"Total of Months: {total_month}"])
    resultswriter.writerow([f"Total: ${net_total}"])
    resultswriter.writerow([f"Average Change: ${average_changes}"])
    resultswriter.writerow([f"Greatest increase in profits: {financial_list[increase_month_index]}(${greatest_increase})"])
    resultswriter.writerow([f"Greatest drecrease in profits: {financial_list[decrease_moth_index]}(${graetest_decrease})"])
    

   
    
