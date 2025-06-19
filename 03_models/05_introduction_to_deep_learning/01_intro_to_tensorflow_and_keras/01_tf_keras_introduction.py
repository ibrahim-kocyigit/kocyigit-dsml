# =======================================
# 1. WHAT IS DEEP LEARNING?
# =======================================
# - Deep Learning is a subfield of machine learning based on Artificial Neural Networks (ANNs).
# - The "deep" in deep learning refers to having multiple layers in the network
#   (i.e., more than one "hidden" layer between the input and output).
# - This layered structure allows the model to learn complex patterns and hierarchical
#   representations from data automatically.
# - It is incredibly effective for tasks involving unstructured data like images, text, and sound.
# - Unlike classical ML where we often perform "feature engineering" manually, deep
#   learning models often learn the important features themselves through their layers.


# =======================================
# 2. INTRODUCING TENSORFLOW AND KERAS
# =======================================
# - TensorFlow: An open-source, end-to-end platform for machine learning developed
#   by Google. It's a powerful library for numerical computation using "tensors"
#   and can run efficiently on hardware like GPUs and TPUs.
#
# - Keras: A high-level deep learning API for building and training models with a focus
#   on user-friendliness and fast experimentation.
#
# - The Relationship: Keras is the official high-level API of TensorFlow. It is the
#   standard way for most practitioners to build TensorFlow models.
#
# - Analogy: TensorFlow is the powerful engine. Keras is the user-friendly dashboard
#   and steering wheel that lets you drive the car easily.


# =======================================
# 3. INSTALLATION AND IMPORTS
# =======================================
# - To install TensorFlow, run this command in your terminal:
#   `pip install tensorflow`
#
# - The standard imports are as follows:
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers  # The building blocks of our models
import numpy as np


# =======================================
# 4. THE CORE DATA STRUCTURE: TENSORS
# =======================================
# - The fundamental data structure in TensorFlow is the `tf.Tensor`.
# - Tensors are multi-dimensional arrays, very similar to NumPy arrays.
# - A key difference is that Tensors can be processed on specialized hardware like GPUs
#   to accelerate computations.

print("--- Working with Tensors ---")
# Create a Tensor from a list
tensor_1d = tf.constant([1, 2, 3, 4])
print("1D Tensor:", tensor_1d)

# Tensors have a shape and a data type, just like NumPy arrays
print(f"Shape: {tensor_1d.shape}, Dtype: {tensor_1d.dtype}")

# Perform operations on tensors
tensor_doubled = tensor_1d * 2
print("Tensor * 2:", tensor_doubled)

# Convert a NumPy array to a Tensor
np_array = np.array([[1, 2], [3, 4]])
tensor_2d = tf.convert_to_tensor(np_array)
print("\n2D Tensor from NumPy array:\n", tensor_2d)
print("-" * 30)


# =======================================
# 5. THE CORE IDEA: BUILDING MODELS BY STACKING LAYERS
# =======================================
# - Building a model in Keras is like stacking LEGO blocks. Each block is a "Layer".
# - A Layer is a data processing module that you can think of as a filter for data.
# - `keras.Sequential` is the simplest way to build a model: a linear stack of layers.

print("--- Building a Simple Keras Sequential Model ---")
# --- Define the model ---
# This model is not trained; we are just defining its architecture.
model = keras.Sequential(
    [
        # Input Layer: Specifies the shape of the input data for the model.
        # Here, we expect each input sample to be a vector of 10 features.
        layers.Input(shape=(10,)),
        # Hidden Layer 1: A "Dense" (fully-connected) layer with 64 neurons.
        # `relu` (Rectified Linear Unit) is a common "activation function".
        layers.Dense(units=64, activation="relu", name="hidden_layer_1"),
        # Hidden Layer 2: Another Dense layer with 32 neurons.
        layers.Dense(units=32, activation="relu", name="hidden_layer_2"),
        # Output Layer: A Dense layer with 1 neuron.
        # `sigmoid` activation is used for binary classification to output a probability (0-1).
        layers.Dense(units=1, activation="sigmoid", name="output_layer"),
    ],
    name="my_first_neural_network",
)


# --- `.summary()`: The most useful method for inspecting a model ---
# This prints a clear, text-based summary of the model's architecture.
print("Model Summary:")
model.summary()
print("-" * 30)


# =======================================
# 6. CONCLUSION AND NEXT STEPS
# =======================================
# - We've learned that Deep Learning uses neural networks, TensorFlow is the engine,
#   and Keras is the user-friendly interface for building these networks.
# - The fundamental building blocks are Tensors and Layers.
# - In the next lesson, we will take this knowledge and apply it to a real problem:
#   we will build, compile, train (`.fit`), and evaluate a simple neural network.

# --- End of File ---
