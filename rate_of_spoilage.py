import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

import matplotlib.pyplot as plt

#Fish, Beef, Chicken, Poultry, Pork are all meats
#Milk, Cheese, Yogurt are all dairy products
#Bread, Cereal, Pasta are all grains
#Apple, Banana, Orange are all fruits
#Carrot, Lettuce, Tomato are all vegetables

# Define the categories
categories = {
    'Meat': ['Fish', 'Beef', 'Chicken', 'Poultry', 'Pork'],
    'Dairy': ['Milk', 'Cheese', 'Yogurt'],
    'Grains': ['Bread', 'Cereal', 'Pasta'],
    'Fruits': ['Apple', 'Banana', 'Orange'],
    'Vegetables': ['Carrot', 'Lettuce', 'Tomato']
}

# Load the data
data = pd.read_csv('Time-to-spoil.csv')

# Define a function for the nonlinear regression (e.g., exponential decay)
def spoilage_model(x, a, b, c):
    return a * np.exp(-b * x) + c

# Define a function to fit the model to the data
def fit_model(data):
    # Get the unique categories
    unique_categories = data['Category'].unique()
    
    # Create a dictionary to store the parameters for each category
    parameters = {}
    
    # Fit the model to each category
    for category in unique_categories:
        # Get the data for the current category
        category_data = data[data['Category'] == category]
        
        # Get the x and y values
        x = category_data['Time (days)']
        y = category_data['Spoilage']
        
        # Fit the model to the data
        popt, _ = curve_fit(spoilage_model, x, y)
        
        # Store the parameters for the current category
        parameters[category] = popt

    return parameters

# Fit the model to the data
parameters = fit_model(data)

# Plot the data and the fitted model for each category
for category in categories:
    # Get the data for the current category
    category_data = data[data['Category'] == category]
    
    # Get the x and y values
    x = category_data['Time (days)']
    y = category_data['Spoilage']
    
    # Get the parameters for the current category
    popt = parameters[category]
    
    # Plot the data
    plt.scatter(x, y, label=category)
    
    # Plot the fitted model
    plt.plot(x, spoilage_model(x, *popt), label='Fitted ' + category)

plt.xlabel('Time (days)')
plt.ylabel('Spoilage')
plt.legend()
plt.show()

