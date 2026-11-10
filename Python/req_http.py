import requests

import json

students = [{
    
    'name' : "Arif", 
    'age' : 30,
    'city' : "Dhaka"
}]


# crate jason

with open ("data.json", 'w') as file:
    
   data = json.dump(students, file, indent=4)
   


# # Read Data

# with open("data.json", 'r') as file:
    
#     data = json.load(file)
    
# print(data)

# print(type(data))