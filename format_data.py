import pandas as pd

# Load the data
data = pd.read_csv('Time-to-spoil.csv')

# Find all entries where the food is Fish, Beef, Chicken, Poultry, or Pork
food_data = data[data['Food'].isin(['Meat'])]

# Find all entries where the storage method is raw
storage_data = food_data[food_data['Storage Method'].isin(['Raw'])]

print(storage_data)


