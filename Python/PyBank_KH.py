import os
import csv

csvpath = os.path.join("Instructions", "PyBank", "Resources","budget_data.csv")

with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)
   
    #set count to zero    
    total = 0
    last_profit_losses = 0  
    
    
    budget_data_list = []
    
    #pull in Date and Profit/Losses and calculate profit/loss change and create a list of dictionaries
    #creating list of dictionaries so that min/max change can be pulled along with date
    for row in reader:
        date = row["Date"]
        profit_losses = int(row["Profit/Losses"])
        
        #this will calculate a change for the first month, will drop before calculating min/max and avg change
        profit_change = int(profit_losses - last_profit_losses)
        total = profit_losses + total
        last_profit_losses = int(row["Profit/Losses"])
        
        budget_data_list.append({
                "Date": date,
                "Profit/Losses": profit_losses,
                "Profit Change":profit_change})

    #Calculate "The total number of months included in the dataset"
    count = len(budget_data_list)   
       

    #need to drop first dictionary because no real change in first month
    data_with_profit_change_list = budget_data_list[1:]
 
    #list of just the profit changes
    changes = [row['Profit Change'] for row in data_with_profit_change_list]
    
    average_change = (sum(changes)/len(changes))
    
    #find max change
    max_change = max(changes)
    #use max value as index to find dictionary in order to pull out month
    max_dict = data_with_profit_change_list[changes.index(max_change)]
    max_date = max_dict["Date"]

    #find min change
    min_change = min(changes)
    #use min value as index to find dictionary in order to pull out month
    min_dict = data_with_profit_change_list[changes.index(min_change)]
    min_date = min_dict["Date"]

    #your final script should both print the analysis to the terminal:
    print("Financial Analysis \n ---------------------")
    print(f"Total Months: {count}")                                 
    print(f"Total: ${total}")
    print(f"Average  Change: ${average_change: .2f}") #format average price to only 2 decimals
    print(f"Greatest Increase in Profits: {max_date} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_date} (${min_change})")
    



#and export a text file with the results
output_path = os.path.join("Output", "new.txt")

with open(output_path, 'w') as newFile:

    newFile.write(("Financial Analysis \n ---------------------"))
    newFile.write((f"\nTotal Months: {count}"))                           
    newFile.write((f"\nTotal: ${total}"))
    newFile.write((f"\nAverage  Change: ${average_change: .2f}"))
    newFile.write((f"\nGreatest Increase in Profits: {max_date} (${max_change})"))
    newFile.write((f"\nGreatest Decrease in Profits: {min_date} (${min_change})"))
    
    newFile.close()
    
    


