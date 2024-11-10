import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

days = np.array([0, 1, 2])
freshness_values = np.array([1.0, 0.694, 0.697])

# Define the exponential decay model function
def freshness_decay_model(t, a, b, c):
    return a * np.exp(-b * t) + c

# Fit the model to the data
params, covariance = curve_fit(freshness_decay_model, days, freshness_values)
a, b, c = params

# Generate a smooth curve for plotting
days_smooth = np.linspace(0, 5, 100)
freshness_smooth = freshness_decay_model(days_smooth, a, b, c)

# Plot the original data points and the fitted curve
plt.scatter(days, freshness_values, color='blue', label='Data Points')
plt.plot(days_smooth, freshness_smooth, color='red', label='Nonlinear Regression Line')
plt.xlabel('Days')
plt.ylabel('Freshness Index')
plt.title('Freshness Index Decay Over Time')
plt.legend()
plt.show()
