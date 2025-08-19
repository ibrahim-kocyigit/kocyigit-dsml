# 01_matplotlib_intro_and_first_plot.py

# =======================================
# 1. WHAT IS MATPLOTLIB?
# =======================================
# - Matplotlib is the foundational, comprehensive library for creating static,
#   animated, and interactive visualizations in Python.
# - It is the cornerstone of the scientific Python plotting ecosystem. Many other
#   plotting libraries, like Seaborn, are built on top of it.
# - It provides a high degree of control over every aspect of a plot.


# =======================================
# 2. INSTALLATION AND IMPORT CONVENTION
# =======================================
# - To install Matplotlib, run this command in your terminal:
#   `pip install matplotlib`
#
# - The universal community convention for importing Matplotlib's main plotting
#   interface is `pyplot`.
import matplotlib.pyplot as plt

# It's also standard practice to import NumPy for creating data to plot.
import numpy as np


# =======================================
# 3. CREATING YOUR FIRST PLOT
# =======================================
# - The `pyplot` interface is great for creating plots quickly.
# - The process involves three fundamental steps:
#   1. Prepare Data: Create the data you want to visualize.
#   2. Create Plot: Use a `plt` function (like `plt.plot()`) to create the plot in memory.
#   3. Show Plot: Use `plt.show()` to display the plot in a window.

print("--- Creating a simple plot from Python lists ---")
# --- Step 1: Prepare Data ---
x_coords = [0, 1, 2, 3, 4]
y_coords = [0, 1, 4, 9, 16] # y = x^2

# --- Step 2: Create the Plot ---
# `plt.plot()` creates a line plot by default.
plt.plot(x_coords, y_coords)

# --- Step 3: Show the Plot ---
# This command opens a window to display the figure.
# The script will pause here until you close the plot window.
print("Displaying the first plot. Close the plot window to continue...")
# plt.show() # We will call show() once at the end of the script.


# =======================================
# 4. PLOTTING WITH NUMPY ARRAYS
# =======================================
# - Matplotlib integrates seamlessly with NumPy arrays, which is the standard practice.
# - This allows you to easily plot mathematical functions.

print("\n--- Creating a more complex plot with NumPy ---")
# --- Step 1: Prepare Data using NumPy ---
# Create an array of 100 points from 0 to 2*pi
x_np = np.linspace(0, 2 * np.pi, 100)
# Create a corresponding y array using a NumPy universal function
y_np_sin = np.sin(x_np)
y_np_cos = np.cos(x_np)


# --- Step 2: Create the Plot ---
# You can call `plt.plot()` multiple times to draw several lines on the same plot.
plt.plot(x_np, y_np_sin)
plt.plot(x_np, y_np_cos)


# =======================================
# 5. DISPLAYING ALL PLOTS
# =======================================
# - `plt.show()` will display all figures that have been created and not yet shown.
# - In this script, it will open two separate plot windows.

print("\nDisplaying all created plots. Close the windows to end the script.")
plt.show()


# --- End of File ---