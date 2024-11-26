import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dataset
calories = np.array([500, 1000, 1500, 1750, 2100]).reshape(-1, 1)
weight_gain = np.array([1, 2, 2.5, 3.2, 3.9])

# Linear Regression Model
model = LinearRegression()
model.fit(calories, weight_gain)

# Predictions
predictions = model.predict(calories)

# Model Evaluation
mse = mean_squared_error(weight_gain, predictions)
r2 = r2_score(weight_gain, predictions)

# Print results
print("Coefficients (Slope):", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Visualization
plt.scatter(calories, weight_gain, color="blue", label="Actual data")
plt.plot(calories, predictions, color="red", label="Regression line")
plt.title("Linear Regression: Calories vs Weight Gain")
plt.xlabel("Calories Consumed")
plt.ylabel("Weight Gain")
plt.legend()
plt.show()
