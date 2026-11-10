
import json

import os

# Check old database

if os.path.exists('database.txt'):

    with open('database.json', 'r') as file:

        try:
            database = json.load(file)

        except json.JSONDecodeError:
            
            database = []

else:
    
    database = []


while True:
    
    item = input("Item (or 'done' for finished): ")
    
    if item == 'done':
        
        break
    
    amount = int(input("Price: "))
    
    category = input("Category (or left blank for 'Other'): ")
    
    if category == '':
        
        category = "Other"
        
    
    database.append(
        
        {
            "item" : item,
            "amount" : amount,
            "category" : category
        }
    )


# Save updated database

with open ('database.json', 'w') as file:
    
    json.dump(database, file, indent=4 )

