import math

def freshness_index(time, mass_initial, mass_curr, temp_curr, temp_optimal, color_curr, color_optimal, weight_mass = 0.5, weight_temp = 0.3, weight_color = 0.2, alpha = 0.01, sigma = 5, lambda_ = 0.05):

    # Mass Factor - not certain about this
    decay_const = 0.28 #not 0.28 but define this later for each food group
    mass_factor = max(0, (mass_curr / mass_initial) * math.exp(-decay_const * time)) * weight_mass
   
    print(mass_factor)

    # Temperature Factor
    temp_factor = math.exp(-((temp_curr - temp_optimal) ** 2) / (2 * sigma ** 2)) * weight_temp
    print(temp_factor)

    # Color Factor - asm color_curr, color_optimal are in range RGB(0-255, 0-255, 0-255)
    color_diff = math.sqrt((color_curr[0] - color_optimal[0]) ** 2 + (color_curr[1] - color_optimal[1]) ** 2 + (color_curr[2] - color_optimal[2]) ** 2)
    color_factor = math.exp(-lambda_ * color_diff) * weight_color
    print(color_factor)

    # Freshness Index
    freshness_index = mass_factor + temp_factor + color_factor
    return min(1, freshness_index) # with the weights summing to 1, the maximum value of the freshness index is 1

# Test the function
test1 = freshness_index(time = 1, mass_initial = 126, mass_curr = 125, temp_curr = 11, temp_optimal = 12, color_curr = (258, 105, 105), color_optimal = (253, 110, 80))

print(test1)
