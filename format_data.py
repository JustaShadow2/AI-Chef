import pandas as pd

# Load the data
data = pd.read_csv('Time-to-spoil.csv')

# Find all entries where the food is Fish, Beef, Chicken, Poultry, or Pork
food_data = data[data['Food'].isin(['Milk', 'Cheese', 'Egg'])]

# Get a list of the time to spoilage for the meat category
time_to_spoilage = food_data[['Time to spoilage (days)', 'Storage Method']].values.tolist()

print(time_to_spoilage)

#make a new entry in formatted-data.csv as Meat, time_to_spoilage
new_entry = {'Category': 'Dairy', 'Time to spoilage': time_to_spoilage}
formatted_data = pd.read_csv('formatted-data.csv')
formatted_data = formatted_data._append(new_entry, ignore_index=True)
formatted_data.to_csv('formatted-data.csv', index=False)


