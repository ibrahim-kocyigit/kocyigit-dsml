# Making importing from other directories possible
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

# Importing 3rd party libraries, packages, and modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Importing from my own modules
from models.linear_regression import LinearRegression
from preprocessing.standard_scaler import StandardScaler
from metrics.mse import mean_squared_error

# --- Testing the Linear Regression model ---

# Load the data
sales = pd.read_csv(
    "../data/marketing_sales.csv"
)  # Path is relative to this file's folder

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    sales[["Marketing_Spend"]], sales["Revenue"], test_size=0.33, random_state=42
)

# Convert to numpy arrays
X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use the same scaler for the test set

# Create the Regressor, fit the data, and make predictions
reg = LinearRegression()
reg.fit(X_train_scaled, y_train, alpha=0.001, epochs=10000)
preds = reg.predict(X_test_scaled)

# Calculate MSE
mse = mean_squared_error(y_test, preds)
print(f"Mean Squared Error on the test set: {mse:.2f}")

# Visualize Results
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color="blue", label="Actual Data")
plt.plot(X_test, preds, color="red", linewidth=2, label="Our Prediction")
plt.xlabel("Marketing Spend")
plt.ylabel("Revenue")
plt.title("Model Performance on Test Data")
plt.legend()
plt.grid(True)
plt.show()
