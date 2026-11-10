# Expense Tracker App

print("Welcome to Expense Tracker")

expenses = []

# FR-01

while True:

    item = input("Item (or 'done' to finish): ")
    
    if item == 'done':
        
        break

    amount = int(input("Amount (Tk): "))

    category = input("Category (leave blank for 'other'): ")
    
    if category == '':
        
        category = "Other"
        
    
    expenses.append(
        
        {
            item
        }
    )