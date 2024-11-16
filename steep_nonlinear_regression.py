import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# asm day 5 with freshness 0
days = np.array([0, 1, 2, 3, 4, 5, 6, 7])
freshness_values = np.array([1.0, 0.710923868536591, 0.63709970475181, 0.511606076772564, 0.44434784966860497, 0.40576335646495826, 0.381205757697219, 0.0])

# Define the sigmoid decay model function
def freshness_sigmoid_model(t, L, k, t_0):
    return L / (1 + np.exp(-k * (t - t_0)))

# Provide initial parameter guesses and increase maxfev
initial_guesses = [1, 1, 3]  # Starting guesses for L, k, and t_0, these can be adjusted when we know better
params, covariance = curve_fit(
    freshness_sigmoid_model, 
    days, 
    freshness_values, 
    p0=initial_guesses, 
    maxfev=5000
)

# Extract fitted parameters
L, k, t_0 = params

# Predict freshness values for all days up to Day 5
days_extended = np.linspace(0, 7, 100)  # Use a smoother range for better curve
predicted_freshness = freshness_sigmoid_model(days_extended, L, k, t_0)

# Plot the observed data and the fitted sigmoid curve
plt.scatter(days, freshness_values, color='blue', label='Observed Data Points)')
plt.plot(days_extended, predicted_freshness, color='red', label='Nonlinear Sigmoid Decay Curve')
plt.xlabel('Days')
plt.ylabel('Freshness Index')
plt.title('Nonlinear Freshness Index Decay with Expected Spoilage at Day 7')
plt.legend()
plt.show()
