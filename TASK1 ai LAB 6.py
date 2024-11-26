import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Specify the Excel file name (ensure the file is in the same directory)
file_name = "task1.xlsx"

# Step 1: Import the Excel file into a DataFrame
try:
    df = pd.read_excel(file_name)  # Read the Excel file
    print(f"Successfully loaded data from {file_name}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found. Please ensure it is in the correct directory.")
    exit()

# Step 2: Display the first few rows of the dataset (optional)
print("\nDataset Preview:")
print(df.head())

# Step 3: Define independent (X) and dependent (y) variables
X = df[["area"]]  # 'area' column for independent variable
y = df["price"]   # 'price' column for dependent variable

# Step 4: Train a Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Step 5: Predict prices for areas in the dataset
predictions = model.predict(X)

print("\nTask 1: Predictions for the areas in the dataset")
for area, price in zip(df["area"], predictions):
    print(f"Area: {area} sq ft -> Predicted Price: ${price:.2f}")

# Step 6: Predict prices for new areas
new_areas = [[5000], [8000], [9000]]  # New areas for prediction
new_predictions = model.predict(new_areas)

print("\nTask 2: Predictions for new areas")
for area, price in zip(new_areas, new_predictions):
    print(f"Area: {area[0]} sq ft -> Predicted Price: ${price:.2f}")

# Step 7: Plot the data and predictions
plt.figure(figsize=(10, 6))

# Plot the original data points
plt.scatter(df["area"], df["price"], color="blue", label="Original Data")

# Plot the regression line
plt.plot(df["area"], predictions, color="red", label="Regression Line")

# Plot new predictions
new_areas_flat = [a[0] for a in new_areas]  # Flatten the list of lists
plt.scatter(new_areas_flat, new_predictions, color="green", marker="o", label="Predicted New Areas")

# Customize the plot
plt.title("Home Prices vs. Area", fontsize=16)
plt.xlabel("Area (sq ft)", fontsize=12)
plt.ylabel("Price (USD)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()