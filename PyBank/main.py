import os 
import csv
budget_data_csv = "Resources/budget_data.csv"

 #PyBank   

#Initialize values 
total_months = 0
net_total = 0
previous_profit_loss_value = 0
#Create lists to store differences and corresponding dates
profit_loss_changes = []
profit_loss_dates = []


#Open CSV
with open(budget_data_csv, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
#Calculate the total months by adding 1 everytime code reads through a row
        total_months += 1
#Find the Profits/Losses column and set it to a variable
        profit_losses = int(row[1])
        dates = str(row[0])
#Calculate net total by adding the value of each row to the total, everytime code reads through a row
        net_total += profit_losses
#If the previous value is 0, it will not subtract the difference between the current value and previous value
#If the previous value is not 0, it will subtract the difference between the current value and the previous value
#Since there is no previous value before the first row, we had initially set it to 0, so it will not subtract anything
        if previous_profit_loss_value != 0:
            profit_loss_change = profit_losses - previous_profit_loss_value
#Add the differences between the current and previous value to a list
            profit_loss_changes.append(profit_loss_change)
#Add the dates to the list
            profit_loss_dates.append(dates)
#Reset, previous profit loss values are values in the Profits/Losses row
        previous_profit_loss_value = profit_losses


#Created dictionary 
profit_changes_dict = {profit_loss_dates[i]:profit_loss_changes[i] for i in range(len(profit_loss_dates))}    

        

#Calculations 
average_change = round((sum(profit_loss_changes)/len(profit_loss_changes)),2)
max_profit = max(profit_loss_changes)
min_profit = min(profit_loss_changes)

#https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/ 
max_profit_date = list(filter(lambda x: profit_changes_dict[x] == max_profit, profit_changes_dict))[0]
min_profit_date = list(filter(lambda x: profit_changes_dict[x] == min_profit, profit_changes_dict))[0]

#Printing the values using a function
def pybank_results():
     print(f"Total Months: {total_months}")
     print(f"Total: ${net_total}")
     print(f"Average change: ${average_change}")
     print(f"Greatest Decrease in Profits: {max_profit_date} (${max_profit})")
     print(f"Greatest Increase in Profits: {min_profit_date} (${min_profit})")
pybank_results()



#Write to a txt file 
pybank_txt = open("pybank.txt", "w")
pybank_txt.write("Financial Analysis\n")
pybank_txt.write("-------------------------------------------\n")
pybank_txt.write(f"Total Months: {total_months}\n")
pybank_txt.write(f"Total: {net_total}\n")
pybank_txt.write(f"Average Change: {average_change}\n")
pybank_txt.write(f"Greatest Decrease in Profits: {max_profit_date} (${max_profit})\n")
pybank_txt.write(f"Greatest Increase in Profits: {min_profit_date} (${min_profit})\n")
pybank_txt.close()
