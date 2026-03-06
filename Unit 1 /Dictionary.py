#Create and access dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'Pimpri'}
print("Dictionary:", my_dict)
print("Access age:", my_dict['age'])  # Output: 25

#Update dictionary elements
my_dict['age'] = 26  # Update existing key
print("Updated dictionary:", my_dict)

#Adding elements
my_dict['hobby'] = 'coding'  # Add new key-value
print("Dictionary after adding hobby:", my_dict)

#Merging dictionaries
dict2 = {'country': 'India'}
my_dict.update(dict2)  # Merge dict2 into my_dict
print("Merged dictionary:", my_dict)  
# Output: {'name': 'Alice', 'age': 26, 'city': 'Pimpri', 'hobby': 'coding', 'country': 'India'}
