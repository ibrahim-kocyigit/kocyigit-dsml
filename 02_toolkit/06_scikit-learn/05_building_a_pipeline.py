import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# =======================================
# 1. WHY USE A PIPELINE?
# =======================================
# - A real-world machine learning workflow often involves a sequence of steps:
#   imputing missing values, scaling numerical features, encoding categorical features,
#   and then finally training a model.
#
# - The Problem with a Manual Workflow:
#   - It's verbose and easy to make mistakes.
#   - It's prone to "data leakage" (e.g., accidentally fitting a scaler on the test set).
#   - It's very difficult to use with advanced techniques like cross-validation and hyperparameter tuning.
#
# - The Solution: `sklearn.pipeline.Pipeline`
#   - A Pipeline chains multiple steps (transformers and an estimator) together.
#   - The entire pipeline behaves like a single estimator, with one `.fit()` and one `.predict()` call.
#   - It guarantees that preprocessing steps are applied correctly and safely, preventing data leakage.


# =======================================
# 2. CREATING A SAMPLE DATASET
# =======================================
# - Let's create a dataset that requires both scaling (for numerical features)
#   and encoding (for categorical features).

data = {
    "age": [25, 45, 35, 50, 23, 55, 65, 30],
    "city": [
        "İzmir",
        "İstanbul",
        "Ankara",
        "İzmir",
        "Ankara",
        "İstanbul",
        "Söke",
        "Söke",
    ],
    "income": [50000, 120000, 80000, 95000, 45000, 150000, 180000, 60000],
    "purchased": [0, 1, 1, 1, 0, 1, 1, 0],  # Target variable
}
df = pd.DataFrame(data)

print("--- Original Mixed-Type Dataset ---")
print(df)

# Define our features (X) and target (y)
X = df.drop("purchased", axis=1)
y = df["purchased"]
print("-" * 30)


# =======================================
# 3. PREPROCESSING WITH `ColumnTransformer`
# =======================================
# - A Pipeline can only have one step for each data type. To apply different
#   transformations to different columns, we first use a `ColumnTransformer`.

print("--- Setting up the Preprocessor ---")
# Identify numerical and categorical columns
numerical_features = ["age", "income"]
categorical_features = ["city"]

# Create a preprocessor object using ColumnTransformer
# This object will apply different transformers to different columns.
preprocessor = ColumnTransformer(
    transformers=[
        # Tuple format: (name_of_step, transformer_object, columns_to_apply_to)
        ("num", StandardScaler(), numerical_features),
        ("cat", OneHotEncoder(), categorical_features),
    ],
    remainder="passthrough",  # Keep other columns (if any). 'drop' is the default.
)
print("Preprocessor created successfully.")
print("-" * 30)


# =======================================
# 4. BUILDING THE FULL PIPELINE
# =======================================
# - Now we chain our `preprocessor` and a final model (estimator) together in a `Pipeline`.

print("--- Building the Full Pipeline ---")
# The pipeline is a list of steps, where each step is a (name, object) tuple.
model_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(random_state=42)),
    ]
)

print("Pipeline created successfully:")
print(model_pipeline)
print("-" * 30)


# =======================================
# 5. USING THE PIPELINE
# =======================================
# - The magic of the pipeline is that you treat it as a single Scikit-Learn estimator.
# - You call `.fit()` and `.predict()` just once on the entire pipeline.

print("--- Training and Predicting with the Pipeline ---")
# --- Step 1: Split the raw data ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# --- Step 2: Fit the ENTIRE pipeline on the raw training data ---
# The pipeline automatically handles:
#  - Fitting the StandardScaler on X_train's numerical columns.
#  - Transforming the X_train numerical columns.
#  - Fitting the OneHotEncoder on X_train's categorical columns.
#  - Transforming the X_train categorical columns.
#  - Training the LogisticRegression model on the fully preprocessed X_train.
model_pipeline.fit(X_train, y_train)
print("Pipeline has been fitted on the training data.")


# --- Step 3: Make predictions on the raw test data ---
# The pipeline automatically handles:
#  - Transforming the X_test numerical columns using the scaler FITTED ON X_TRAIN.
#  - Transforming the X_test categorical columns using the encoder FITTED ON X_TRAIN.
#  - Making predictions with the trained LogisticRegression model.
y_pred = model_pipeline.predict(X_test)
print("\nPredictions on the test set:", y_pred)


# --- Step 4: Evaluate the model ---
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2f}")
print("This workflow prevents data leakage and simplifies your code dramatically.")

# --- End of File ---
