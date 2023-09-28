# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict
# Access to the value by the key
Dict["key1"]
# Access to the value by the key
Dict[(0, 1)]

# Create a sample dictionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict

# Get value by keys
release_year_dict['Thriller'] 
# Get value by key
release_year_dict['The Bodyguard'] 
# Get all the keys in dictionary
release_year_dict.keys()
# Get all the values in dictionary
release_year_dict.values() 
# Append value with key into dictionary
release_year_dict['Graduation'] = '2007'
release_year_dict
# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict
# Verify the key is in the dictionary
'The Bodyguard' in release_year_dict

######################### QUIZ: Dictionaries #########################

# Question sample dictionary
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic

soundtrack_dic.keys()
soundtrack_dic.values()

album_sales_dict = {"Back in Black":50, "The Bodyguard":50, "Thriller":65}

album_sales_dict["Thriller"]
album_sales_dict.keys()
album_sales_dict.values()

## Scenario: Inventory store

### Task 1: Create an empty dictionary

inventory = {}

### Task 2: Store the first product details in variable

ProductNo1 = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_releaseYear= 2020

### Task 3: Add the details in inventory

inventory["ProductNo1"]= ProductNo1
inventory["ProductNo1_quantity"]= ProductNo1_quantity
inventory["ProductNo1_price"]= ProductNo1_price
inventory["ProductNo1_releaseYear"]=ProductNo1_releaseYear

### Task 4: Store the second product details in a variable.
ProductNo2 = "Laptop"
ProductNo2_quantity = 10
ProductNo2_price = 50000
ProductNo2_releaseYear= 2023

### Task 5: Add the item detail into the inventory.

inventory["ProductNo2"]= ProductNo2
inventory["ProductNo2_quantity"]= ProductNo2_quantity
inventory["ProductNo2_price"]= ProductNo2_price
inventory["ProductNo2_releaseYear"]= ProductNo2_releaseYear

### Task 6: Display the Products present in the inventory

print(inventory)

### Task 7: Check if ProductNo1_releaseYear and ProductNo2_releaseYear is in the inventory

"ProductNo1_releaseYear" in inventory
"ProductNo2_releaseYear" in inventory

### Task 8: Delete release year of both the products from the inventory

del(inventory["ProductNo1_releaseYear"])
del(inventory["ProductNo2_releaseYear"])
inventory

######################### END OF QUIZ #########################