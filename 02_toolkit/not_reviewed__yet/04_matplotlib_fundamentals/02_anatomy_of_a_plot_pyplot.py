# 02_anatomy_of_a_plot_pyplot.py

import matplotlib.pyplot as plt
import numpy as np

# =======================================
# 1. THE ANATOMY OF A PLOT
# =======================================
# - A complete visualization is more than just a line; it needs labels and titles
#   to provide context and be easily understood.
# - Matplotlib allows you to customize every part of your plot.
# - Key Components:
#   - Figure: The entire window or page the plot is drawn on.
#   - Axes: The actual plot area where the data is plotted (the x-y coordinate system).
#   - Title: The main title of the plot.
#   - x-label / y-label: The labels for the x and y axes.
#   - Legend: A key to identify different lines or data series on the plot.
#   - Grid: A grid of lines in the background to aid in reading values.


# =======================================
# 2. BUILDING A PLOT STEP-BY-STEP
# =======================================
# - We will use the `pyplot` interface to add these components one by one.

# --- Step 1: Prepare Data ---
# We'll plot two functions, sine and cosine, to demonstrate the legend.
x = np.linspace(0, 10, 100) # 100 points from 0 to 10
y_sin = np.sin(x)
y_cos = np.cos(x)


# --- Step 2: Create the Plot and Add Components ---

# `plt.figure()` can be used to control the overall window size.
plt.figure(figsize=(10, 6)) # (width, height in inches)

# Plot the data. We add a `label` to each line for the legend.
plt.plot(x, y_sin, label='Sine Wave')
plt.plot(x, y_cos, label='Cosine Wave')


# --- Step 3: Add Labels, Title, and other Components ---

# Add a title to the plot
plt.title('Sine and Cosine Functions')

# Add labels to the x and y axes
plt.xlabel('X-axis (from 0 to 10)')
plt.ylabel('Y-axis (Value)')

# Add a legend to identify the lines
# This function automatically uses the `label`s we defined in `plt.plot()`.
plt.legend()

# Add a grid to the background for better readability
plt.grid(True)

# You can manually set the limits of the axes
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)


# --- Step 4: Show the Plot ---
# `plt.show()` displays the final, complete figure.
print("Displaying a fully labeled plot. Close the plot window to end the script.")
plt.show()


# =======================================
# 3. SUMMARY OF PYPLOT COMMANDS
# =======================================
# - `plt.figure(figsize=(w, h))`: Controls the overall figure size.
# - `plt.plot(x, y, label='...')`: Plots the data and assigns it a label.
# - `plt.title('...')`: Sets the plot's main title.
# - `plt.xlabel('...')`: Sets the label for the x-axis.
# - `plt.ylabel('...')`: Sets the label for the y-axis.
# - `plt.legend()`: Displays the legend using the plot labels.
# - `plt.grid(True)`: Turns on the background grid.
# - `plt.xlim(min, max)` / `plt.ylim(min, max)`: Sets the axis limits.
# - `plt.show()`: Displays the figure.


# --- End of File ---