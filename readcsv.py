# written by lukas (i am the greatest coder of all time)

import csv
import ast

class Food:
    def __init__(self, food_name, food_group, colour_day, mass_day, temp_day):
        self.food_name = food_name
        self.food_group = food_group
        self.colour_day = colour_day
        self.mass_day = mass_day
        self.temp_day = temp_day

    def __str__(self):
        return (
            f"Food Name: {self.food_name}\n"
            f"Food Group: {self.food_group}\n"
            f"Colour (RGB) by Day: {self.colour_day}\n"
            f"Mass (grams) by Day: {self.mass_day}\n"
            f"Temperature (degrees C) by Day: {self.temp_day}\n"
        )

foodList = []

with open('ourData.csv', "r") as commentedFile: 
    reader = csv.reader(commentedFile)
    next(reader)  # skip line of headers

    for row in reader:
        food_name = row[0].strip()
        food_group = row[1].strip()
        colour_day_raw = row[2].strip()
        mass_day_raw = row[3].strip()
        temp_day_raw = row[4].strip()

        colour_day_list = ast.literal_eval(colour_day_raw)
        mass_day_list = ast.literal_eval(mass_day_raw)
        temp_day_list = ast.literal_eval(temp_day_raw)

        # Use lists instead of dictionaries because duplicate values erases entries that we need
        colour_day = colour_day_list
        mass_day = mass_day_list
        temp_day = temp_day_list

        food = Food(food_name, food_group, colour_day, mass_day, temp_day)

        foodList.append(food)

for food in foodList:
    print(food)