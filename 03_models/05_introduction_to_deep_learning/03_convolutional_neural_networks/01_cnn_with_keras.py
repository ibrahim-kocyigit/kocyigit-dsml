import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, datasets
import matplotlib.pyplot as plt

# =======================================
# 1. WHAT ARE CONVOLUTIONAL NEURAL NETWORKS (CNNs)?
# =======================================
# - CNNs are a specialized class of neural networks designed to process grid-like data,
#   such as images.
#
# - Why not use a standard (Dense) network for images?
#   - Flattening a large image into a 1D vector loses all spatial information
#     (which pixels are next to each other).
#   - It creates a huge number of input features, leading to an explosion of
#     model parameters, making it inefficient and prone to overfitting.
#
# - How CNNs work:
#   - They use special layers that preserve spatial structure and learn features hierarchically.
#   - Core Building Blocks:
#     1. Convolutional Layers (`Conv2D`): Act as "feature detectors" that slide
#        across the image to find patterns like edges, corners, textures, and shapes.
#     2. Pooling Layers (`MaxPooling2D`): Downsample the image data to reduce
#        computational complexity and make the detected features more robust to their
#        exact location in the image.


# =======================================
# 2. STEP 1: LOAD AND PREPARE THE IMAGE DATASET
# =======================================
# - We will use the CIFAR-10 dataset, which is built into Keras.
# - It consists of 60,000 32x32 color images in 10 different classes.

print("--- Step 1: Loading and Preparing CIFAR-10 Data ---")
# Load the dataset
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

# --- Preprocess the data ---
# Normalize pixel values to be between 0 and 1. This helps with training stability.
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Define the class names for later visualization
class_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]

print(f"Training data shape: {x_train.shape}")  # (50000, 32, 32, 3)
print(f"Test data shape: {x_test.shape}")  # (10000, 32, 32, 3)

# --- Visualize a few sample images ---
plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i])
    # The y labels are arrays, so we need y_train[i][0] to get the integer value
    plt.xlabel(class_names[y_train[i][0]])
print("Showing 9 sample images from the CIFAR-10 training set...")
# We will show all plots at the end.
print("-" * 30)


# =======================================
# 3. STEP 2 & 3: DEFINE AND COMPILE THE CNN MODEL
# =======================================
# - The common pattern for a CNN block is: Conv2D -> Activation -> MaxPooling2D
# - After extracting features with convolutional blocks, we flatten the output
#   and use Dense layers for the final classification.

print("--- Step 2 & 3: Defining and Compiling the CNN ---")
model = keras.Sequential(
    [
        # Input Layer: Specifies the image shape
        layers.Input(shape=(32, 32, 3)),
        # Convolutional Block 1
        layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        # Convolutional Block 2
        layers.Conv2D(filters=64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        # Flattening and Dense Layers for Classification
        layers.Flatten(),  # Flatten the 2D feature map to a 1D vector
        layers.Dense(units=64, activation="relu"),
        layers.Dense(
            units=10, activation="softmax"
        ),  # Output layer: 10 neurons for 10 classes
    ]
)

# --- Compile the model ---
# - `sparse_categorical_crossentropy` is used when your target `y` variable
#   consists of integers (0, 1, 2...) for each class.
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

model.summary()
print("-" * 30)


# =======================================
# 4. STEP 4: TRAIN THE CNN MODEL
# =======================================
# - We fit the model on our prepared training data and use the test data for validation.
# - Note: Training a CNN, even a small one, can be slow on a CPU.
#   Running for 10-15 epochs might take a few minutes.

print("--- Step 4: Training the Model (this will take a few moments) ---")
history = model.fit(
    x_train,
    y_train,
    epochs=15,
    validation_data=(x_test, y_test),
    verbose=2,  # Show one line per epoch
)
print("Model training complete.")
print("-" * 30)


# =======================================
# 5. STEP 5 & 6: EVALUATE AND VISUALIZE
# =======================================
print("--- Step 5: Evaluating the Model ---")
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"Final Test Accuracy: {test_accuracy:.3f}")

# --- Visualize Training History ---
history_df = pd.DataFrame(history.history)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(history_df["loss"], label="Training Loss")
plt.plot(history_df["val_loss"], label="Validation Loss")
plt.title("Loss Over Epochs")
plt.legend()
plt.grid(True)
plt.subplot(1, 2, 2)
plt.plot(history_df["accuracy"], label="Training Accuracy")
plt.plot(history_df["val_accuracy"], label="Validation Accuracy")
plt.title("Accuracy Over Epochs")
plt.legend()
plt.grid(True)

print("\n--- Step 6: Visualizing Training History ---")
print("This concludes our Introduction to Deep Learning!")


# --- Display all plots ---
plt.tight_layout()
plt.show()

# --- End of File ---
