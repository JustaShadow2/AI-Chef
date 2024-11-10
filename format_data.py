import pandas as pd

category = input("Enter the category of food you would like to search for: ")
storage = input("Enter the storage method you would like to search for: ")

# Load the data
data = pd.read_csv('Time-to-spoil.csv')

# Find all entries where the food is Fish, Beef, Chicken, Poultry, or Pork
food_data = data[data['Food'].isin([category])]

# Find all entries where the storage method is raw
storage_data = food_data[food_data['Storage Method'].isin([storage])]

print(storage_data)

