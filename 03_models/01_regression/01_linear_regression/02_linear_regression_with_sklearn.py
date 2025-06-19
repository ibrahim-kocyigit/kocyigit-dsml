import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# =======================================
# 1. INTRODUCTION TO LINEAR REGRESSION
# =======================================
# - Linear Regression is the foundational algorithm for Supervised Learning tasks
#   where the goal is to predict a continuous numerical value (e.g., price, salary, temperature).
# - It aims to find the best-fitting straight line through the data points that
#   minimizes the distance between the line and the actual data points.
# - The formula for a simple line is: y = m*x + b
#   - `y` is the target variable (what we want to predict).
#   - `x` is the input feature.
#   - `m` is the slope or coefficient.
#   - `b` is the y-intercept.
# - The model "learns" the optimal values for `m` and `b` from the training data.


# =======================================
# 2. STEP 1: CREATE A SYNTHETIC DATASET
# =======================================
# - In a real project, you would load data with Pandas.
# - Here, we'll create our own data to model a clear relationship between
#   "Years of Experience" and "Salary".

print("--- Step 1: Creating Data ---")
np.random.seed(0)
# Create our feature X (Years of Experience). It must be a 2D array for Scikit-Learn.
X = np.arange(1, 11).reshape(-1, 1)

# Create our target y (Salary) with a linear relationship + some random "noise"
# Formula: Salary = 50000 + 4000 * Experience + noise
y = 50000 + 4000 * X.flatten() + np.random.normal(0, 5000, 10)

print(f"Shape of features matrix X: {X.shape}")
print(f"Shape of target vector y: {y.shape}")
print("-" * 30)


# =======================================
# 3. STEP 2: SPLIT DATA FOR TRAINING AND TESTING
# =======================================
# - As we learned in the fundamentals section, we split our data to get an
#   unbiased evaluation of our model's performance on unseen data.

print("--- Step 2: Splitting Data ---")
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,  # 30% of data for testing
)
print(f"Training set size: {len(X_train)} samples")
print(f"Testing set size: {len(X_test)} samples")
print("-" * 30)


# =======================================
# 4. STEP 3 & 4: CREATE AND TRAIN THE MODEL
# =======================================
# - We follow the standard Scikit-Learn Estimator API: instantiate, then fit.

print("--- Step 3 & 4: Training the Model ---")
# 1. Instantiate the model
model = LinearRegression()

# 2. "Fit" (train) the model on the training data
model.fit(X_train, y_train)
print("Model training complete.")

# --- Inspect the learned parameters ---
# After fitting, the model stores the learned parameters in attributes
# with a trailing underscore.
print(f"Learned Intercept (b): {model.intercept_:.2f}")
print(f"Learned Coefficient (m): {model.coef_[0]:.2f}")
print("-" * 30)


# =======================================
# 5. STEP 5: MAKE PREDICTIONS
# =======================================
# - We use our trained model to make predictions on the unseen test data.

print("--- Step 5: Making Predictions ---")
y_pred = model.predict(X_test)

# Let's create a small DataFrame to easily compare predictions and actual values
comparison_df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
print(comparison_df.round(2))
print("-" * 30)


# =======================================
# 6. STEP 6: EVALUATE THE MODEL
# =======================================
# - We quantify our model's performance by comparing its predictions (`y_pred`)
#   to the actual values (`y_test`).

print("--- Step 6: Evaluating Model Performance ---")
# Mean Absolute Error (MAE): The average absolute difference between the predictions and the actual values.
print(f"Mean Absolute Error (MAE): {metrics.mean_absolute_error(y_test, y_pred):.2f}")

# Mean Squared Error (MSE): The average of the squared differences. Penalizes larger errors more.
print(f"Mean Squared Error (MSE): {metrics.mean_squared_error(y_test, y_pred):.2f}")

# R-squared (R2 Score): The proportion of the variance in the target that's predictable from the features.
# A score of 1.0 is a perfect fit.
print(f"R-squared (R2 Score): {metrics.r2_score(y_test, y_pred):.2f}")
print("-" * 30)


# =======================================
# 7. STEP 7: VISUALIZE THE RESULTS
# =======================================
# - A plot makes it easy to see how well the model's regression line fits the data.

print("--- Step 7: Visualizing the Results ---")
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the actual data points from the entire dataset
ax.scatter(X, y, color="skyblue", label="Actual Data Points")

# Plot the regression line (our model's predictions) across the entire range of X
ax.plot(X, model.predict(X), color="red", linewidth=2, label="Regression Line")

ax.set_title("Linear Regression: Salary vs. Experience", fontsize=16)
ax.set_xlabel("Years of Experience", fontsize=12)
ax.set_ylabel("Salary", fontsize=12)
ax.legend()
ax.grid(True)

print("Displaying plot. Close the plot window to end the script.")
plt.show()

# --- End of File ---
