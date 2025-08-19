# 06_creating_multiple_subplots.py

import matplotlib.pyplot as plt
import numpy as np

# =======================================
# 1. THE POWER OF THE OO INTERFACE
# =======================================
# - A major strength of the Object-Oriented interface is the ability to easily
#   create complex layouts with multiple plots (Axes) within a single Figure.
# - This is essential for comparing different views of your data side-by-side.
# - We do this by passing arguments to the `plt.subplots()` function.


# =======================================
# 2. CREATING A GRID OF SUBPLOTS
# =======================================
# - `fig, axes = plt.subplots(nrows, ncols)` creates a figure and a grid of subplots.
# - IMPORTANT: When you create more than one subplot, the returned `axes` variable
#   is a NumPy array of `Axes` objects.
# - You access each individual plot using standard NumPy indexing.

print("--- Understanding the `axes` array ---")
# --- Example 1: A 2x1 vertical grid ---
# This creates 2 plots stacked vertically.
fig1, axes1 = plt.subplots(nrows=2, ncols=1)
print(f"For a 2x1 grid, `axes` is a 1D NumPy array with shape: {axes1.shape}")
# You access them with a single index:
ax_top = axes1[0]
ax_bottom = axes1[1]
ax_top.set_title("Top Plot")
ax_bottom.set_title("Bottom Plot")


# --- Example 2: A 2x2 grid ---
fig2, axes2 = plt.subplots(nrows=2, ncols=2)
print(f"\nFor a 2x2 grid, `axes` is a 2D NumPy array with shape: {axes2.shape}")
# You access them with 2D indexing:
axes2[0, 0].set_title("Top-Left Plot")
axes2[0, 1].set_title("Top-Right Plot")
axes2[1, 0].set_title("Bottom-Left Plot")
axes2[1, 1].set_title("Bottom-Right Plot")

# We will close these empty figures when we call plt.show() at the end.
print("-" * 30)


# =======================================
# 3. A COMPLETE EXAMPLE: 2x2 PLOT GRID
# =======================================
# - Let's create a full figure with four different types of plots.

# --- Step 1: Create the Figure and the 2x2 grid of Axes ---
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))


# --- Step 2: Plot on each Axes object individually ---

# Plot 1: Top-Left (Line Plot)
x_line = np.linspace(0, 2 * np.pi, 100)
y_line = np.sin(x_line)
axes[0, 0].plot(x_line, y_line, color='blue')
axes[0, 0].set_title('Sine Wave')
axes[0, 0].set_xlabel('Angle [rad]')
axes[0, 0].set_ylabel('Amplitude')
axes[0, 0].grid(True)

# Plot 2: Top-Right (Scatter Plot)
np.random.seed(42)
x_scatter = np.random.rand(50)
y_scatter = x_scatter + np.random.randn(50) * 0.1
axes[0, 1].scatter(x_scatter, y_scatter, color='green', alpha=0.6)
axes[0, 1].set_title('Correlated Data Scatter Plot')
axes[0, 1].set_xlabel('Feature 1')
axes[0, 1].set_ylabel('Feature 2')

# Plot 3: Bottom-Left (Bar Chart)
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 22, 18]
axes[1, 0].bar(categories, values, color='purple')
axes[1, 0].set_title('Sales by Category')
axes[1, 0].set_xlabel('Category')
axes[1, 0].set_ylabel('Sales')

# Plot 4: Bottom-Right (Histogram)
hist_data = np.random.randn(1000)
axes[1, 1].hist(hist_data, bins=30, color='orange')
axes[1, 1].set_title('Data Distribution')
axes[1, 1].set_xlabel('Value')
axes[1, 1].set_ylabel('Frequency')


# =======================================
# 4. IMPROVING THE LAYOUT
# =======================================
# - Often, titles and labels can overlap in a grid.
# - `fig.suptitle()` adds a centered title for the entire figure.
# - `plt.tight_layout()` automatically adjusts subplot params for a tight layout.

fig.suptitle('A Dashboard of Different Plots', fontsize=16)

# This command is a lifesaver for making plots look good.
plt.tight_layout(rect=[0, 0, 1, 0.96]) # rect adjusts for the suptitle


# =======================================
# 5. SHARING AXES
# =======================================
# - You can link the axes of subplots using `sharex=True` or `sharey=True`.
# - This is useful for comparing plots on the same scale.

fig_shared, axes_shared = plt.subplots(nrows=2, ncols=1, figsize=(8, 6), sharex=True)
axes_shared[0].plot(x_line, y_line, color='red')
axes_shared[0].set_title('Sine Wave')
axes_shared[1].plot(x_line, -y_line, color='black') # Plot -sin(x)
axes_shared[1].set_title('Negative Sine Wave')
# Notice how the x-axis labels are automatically hidden on the top plot to save space.


# --- Display all created figures ---
print("Displaying three figures: an empty 2x1, an empty 2x2, a 2x2 dashboard, and a 2x1 shared-axis plot.")
print("Close the plot windows to end the script.")
plt.show()

# --- End of File ---