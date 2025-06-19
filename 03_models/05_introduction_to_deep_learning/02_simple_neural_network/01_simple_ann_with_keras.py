# 02_building_a_simple_neural_network.py

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn import metrics

# =======================================
# 1. THE DEEP LEARNING WORKFLOW
# =======================================
# - The workflow for training a neural network is a series of well-defined steps:
#   1. Prepare Data: Load and preprocess the data. Scaling is crucial for neural networks.
#   2. Define the Model: Stack layers to create the network architecture using Keras.
#   3. Compile the Model: Configure the learning process by specifying the optimizer,
#      loss function, and metrics to monitor. This is a critical step.
#   4. Train the Model: Use the `.fit()` method on the training data.
#   5. Evaluate the Model: Use the `.evaluate()` method to measure performance on the test data.
#   6. Make Predictions: Use the `.predict()` method on new data.


# =======================================
# 2. STEP 1: PREPARE THE DATA
# =======================================
# - We'll create a binary classification dataset and then split and scale it.
# - Scaling is essential for neural networks to help the training process converge smoothly.

print("--- Step 1: Preparing Data ---")
X, y = make_classification(
    n_samples=1000, n_features=20, n_informative=10, n_redundant=5, random_state=42
)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Data prepared and scaled. Training set shape: {X_train_scaled.shape}")
print("-" * 30)


# =======================================
# 3. STEP 2 & 3: DEFINE AND COMPILE THE MODEL
# =======================================
# - We first define the architecture, then configure the training process with `.compile()`.

print("--- Step 2 & 3: Defining and Compiling the Model ---")
# --- Define the architecture using the Sequential API ---
model = keras.Sequential(
    [
        layers.Input(shape=(X_train_scaled.shape[1],)),  # Input layer for 20 features
        layers.Dense(units=32, activation="relu"),  # Hidden layer 1
        layers.Dense(units=16, activation="relu"),  # Hidden layer 2
        layers.Dense(
            units=1, activation="sigmoid"
        ),  # Output layer for binary classification
    ]
)

# --- Compile the model ---
# - `optimizer`: The algorithm that updates the model's weights (e.g., 'adam' is a great default).
# - `loss`: The function that measures how wrong the model is ('binary_crossentropy' for 2 classes).
# - `metrics`: The performance metric to track during training.
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

print("Model has been defined and compiled.")
model.summary()  # Print a summary of the model's architecture
print("-" * 30)


# =======================================
# 4. STEP 4: TRAIN THE MODEL (`.fit()`)
# =======================================
# - The `.fit()` method starts the training process.
# - `epochs`: One full pass through the entire training dataset.
# - `validation_data`: By passing the test set here, Keras will evaluate performance
#   on unseen data at the end of each epoch, which is great for monitoring.
print("--- Step 4: Training the Model ---")
history = model.fit(
    X_train_scaled,
    y_train,
    epochs=25,
    batch_size=32,
    validation_data=(X_test_scaled, y_test),
    verbose=1,  # Show a progress bar for each epoch
)
print("Model training complete.")
print("-" * 30)


# =======================================
# 5. STEP 5 & 6: EVALUATE AND VISUALIZE
# =======================================
# - `.evaluate()` gives the final loss and metrics on the test set.
# - Plotting the training history is the best way to diagnose model behavior.

print("--- Step 5: Evaluating the Model ---")
# The `.evaluate` method returns the loss and any other metrics we compiled.
test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Final Test Accuracy: {test_accuracy:.3f}")
print(f"Final Test Loss: {test_loss:.3f}")

# --- Visualize Training History ---
# The `history` object contains the training history.
history_df = pd.DataFrame(history.history)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Model Training History", fontsize=16)

# Plot Loss
axes[0].plot(history_df["loss"], label="Training Loss")
axes[0].plot(history_df["val_loss"], label="Validation Loss")
axes[0].set_title("Loss Over Epochs")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Loss")
axes[0].legend()
axes[0].grid(True)

# Plot Accuracy
axes[1].plot(history_df["accuracy"], label="Training Accuracy")
axes[1].plot(history_df["val_accuracy"], label="Validation Accuracy")
axes[1].set_title("Accuracy Over Epochs")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Accuracy")
axes[1].legend()
axes[1].grid(True)

print("\n--- Step 6: Visualizing Training History ---")
print("Generated plots showing model loss and accuracy over epochs.")
print(
    "This helps diagnose overfitting (when validation loss increases while training loss decreases)."
)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# --- End of File ---
