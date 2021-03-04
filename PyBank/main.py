#Import required packages
import os 
import csv

#Files to load and output
PyBankfile_to_load = os.path.join("Resources", "budget_data.csv")
PyBankfile_to_output = os.path.join("PyBank_analysis.txt")

#creating list
months = []
amount = []

#Read the csv 
with open(PyBankfile_to_load) as bank_data:
    reader = csv.reader(bank_data)

    header = next(reader)


#looping through each row and storing the elements in a new list
    for row in reader:

        months.append(row[0])
        total_months = len(months)
        amount.append(int(row[1]))
        total_amount = sum(amount)
        
        change = [amount[i + 1] - amount[i] for i in range(len(amount)-1)] 
    
    average_change = round(sum(change)/(total_months - 1),2)
    greatest_increase = max(change)
    greatest_decrease = min(change)
    greatest_increase_month = months[change.index(greatest_increase)+ 1]
    greatest_decrease_month = months[change.index(greatest_decrease)+ 1]
    

        
# Generate Financial Analysis Output
output = (
    f"\nFinancial Analysis\n"
    f"-----------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_amount}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

# Print all of the results (to terminal)
print(output)


# Save the results to analysis text file
with open(PyBankfile_to_output, "a") as txt_file:
    txt_file.write(output)
