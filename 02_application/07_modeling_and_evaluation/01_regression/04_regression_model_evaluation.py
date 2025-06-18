import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# =======================================
# 1. WHY WE NEED EVALUATION METRICS
# =======================================
# - Visualizing a model's fit is good for a qualitative understanding, but we need
#   objective, numerical metrics to quantify a model's performance.
# - Metrics allow us to:
#   1. Objectively measure how well a model is performing.
#   2. Compare different models against each other.
#   3. Provide a tangible value to report on model success.
# - All regression metrics work by comparing the model's predictions (`y_pred`)
#   with the true, actual values (`y_test`).


# =======================================
# 2. SETTING UP A PREDICTION SCENARIO
# =======================================
# - To evaluate metrics, we first need to train a model and generate some predictions.
# - We'll follow the same simple workflow as the previous lessons.

# --- Create Data, Split, Train, and Predict ---
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # 100 samples, 1 feature
y = 2 * X.flatten() + 5 + np.random.randn(100) * 2  # y = 2x + 5 + noise

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Generate predictions on the unseen test set
y_pred = model.predict(X_test)

print("--- Prediction Scenario Setup ---")
print("Model trained and predictions generated on the test set.")
# Create a DataFrame to easily compare a few predictions
comparison_df = pd.DataFrame({"Actual Value": y_test, "Predicted Value": y_pred}).head()
print("Sample of Actual vs. Predicted values:\n", comparison_df.round(2))
print("-" * 30)


# =======================================
# 3. METRIC 1: MEAN ABSOLUTE ERROR (MAE)
# =======================================
# - MAE is the average of the absolute differences between predictions and actual values.
# - Formula: MAE = (1/n) * Σ|y_test - y_pred|
# - Interpretation: It's the average magnitude of error in the predictions, in the
#   same units as the target variable. An MAE of 1.5 means our predictions are,
#   on average, off by $1.50.

print("--- Metric 1: Mean Absolute Error (MAE) ---")
mae = metrics.mean_absolute_error(y_test, y_pred)
print(f"The Mean Absolute Error is: {mae:.3f}")
print("This means our model's predictions are, on average, off by this amount.")
print("-" * 30)


# =======================================
# 4. METRIC 2: MEAN SQUARED ERROR (MSE) & RMSE
# =======================================
# - MSE is the average of the squared differences between predictions and actual values.
# - Formula: MSE = (1/n) * Σ(y_test - y_pred)^2
# - Interpretation: Because it squares the errors, it penalizes larger errors much more
#   heavily than smaller ones. The units are squared (e.g., dollars-squared),
#   making it less intuitive than MAE.
#
# - RMSE (Root Mean Squared Error) is the square root of MSE.
# - It is often preferred because taking the square root brings the error metric
#   back into the same units as the target variable, making it more interpretable.

print("--- Metric 2: Mean Squared Error (MSE) & RMSE ---")
mse = metrics.mean_squared_error(y_test, y_pred)
print(f"The Mean Squared Error is: {mse:.3f}")

rmse = np.sqrt(mse)  # Or: metrics.mean_squared_error(y_test, y_pred, squared=False)
print(f"The Root Mean Squared Error is: {rmse:.3f}")
print("RMSE is interpretable in the same units as the target, like MAE.")
print("-" * 30)


# =======================================
# 5. METRIC 3: R-SQUARED (R²)
# =======================================
# - R-squared is the "coefficient of determination". It provides a measure of "goodness of fit".
# - Interpretation: It represents the proportion of the variance in the target
#   variable that is predictable from the input features.
#   - R² = 1.0: The model perfectly explains the variance in the data.
#   - R² = 0.0: The model explains none of the variance (it's no better than predicting the mean).
#   - R² < 0.0: The model is worse than just predicting the mean.

print("--- Metric 3: R-squared (R²) ---")
r2 = metrics.r2_score(y_test, y_pred)
print(f"The R-squared score is: {r2:.3f}")
print(
    f"This means our model explains approximately {r2:.1%} of the variance in the data."
)
print("-" * 30)


# =======================================
# 6. SUMMARY: WHICH METRIC TO USE?
# =======================================
# - MAE: Easy to interpret, robust to outliers. Good for a simple, average error magnitude.
# - RMSE: Penalizes large errors more. Use when you want to make it clear that
#   large errors are particularly undesirable.
# - R²: Explains the proportion of variance captured. Good for assessing the overall
#   explanatory power of your model.
# - Context is Key: The best metric depends on your specific business problem.

# --- End of File ---
