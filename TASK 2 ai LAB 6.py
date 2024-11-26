import numpy as np
import matplotlib.pyplot as plt

# Data from the table
area = np.array([2600, 3000, 3200, 3600, 4000])
price = np.array([550000, 565000, 610000, 680000, 725000])

# Calculate the slope (m) and y-intercept (b) of the regression line
m = np.sum((area - np.mean(area)) * (price - np.mean(price))) / np.sum((area - np.mean(area)) ** 2)
b = np.mean(price) - m * np.mean(area)

# Predict prices for given areas
predicted_price_5000 = m * 5000 + b
predicted_price_8000 = m * 8000 + b
predicted_price_9000 = m * 9000 + b

# Print the predicted prices
print(f"Predicted price for a home with area = 5000 sqr ft: {predicted_price_5000:.2f}")
print(f"Predicted price for a home with area = 8000 sqr ft: {predicted_price_8000:.2f}")
print(f"Predicted price for a home with area = 9000 sqr ft: {predicted_price_9000:.2f}")

# Plot the data and the regression line
plt.scatter(area, price, label="Data")
plt.plot(area, m * area + b, color='red', label="Regression Line")
plt.xlabel("Area (sqr ft)")
plt.ylabel("Price")
plt.title("Linear Regression for Home Prices")
plt.legend()
plt.show()