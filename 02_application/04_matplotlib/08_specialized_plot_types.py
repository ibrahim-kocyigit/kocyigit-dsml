# 08_specialized_plot_types.py

import matplotlib.pyplot as plt
import numpy as np

# =======================================
# 1. INTRODUCTION
# =======================================
# - Beyond the basics, Matplotlib supports a wide variety of specialized plots
#   that are crucial for statistical analysis and representing complex data.
# - We will cover three important types using the Object-Oriented interface:
#   1. Box Plots: For visualizing data distribution and outliers.
#   2. Error Bars: For showing uncertainty in measurements.
#   3. Heatmaps: For visualizing 2D data as a grid of colors.

# --- Setup a figure with 3 subplots side-by-side ---
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))


# =======================================
# 2. BOX PLOTS (`ax.boxplot`)
# =======================================
# - A box plot (or box-and-whisker plot) is a standardized way of displaying
#   the distribution of data based on a five-number summary:
#   minimum, first quartile (Q1), median, third quartile (Q3), and maximum.
# - It is excellent for comparing distributions across multiple groups.

# --- Prepare Data ---
# Create three different datasets to compare
np.random.seed(10)
data1 = np.random.normal(100, 10, 200)  # Mean=100, Std=10
data2 = np.random.normal(80, 30, 200)  # Mean=80,  Std=30
data3 = np.random.normal(90, 20, 200)  # Mean=90,  Std=20
data_to_plot = [data1, data2, data3]

# --- Create Plot on the first Axes ---
ax1 = axes[0]
# `patch_artist=True` fills the boxes with color
bp = ax1.boxplot(
    data_to_plot, patch_artist=True, labels=["Group A", "Group B", "Group C"]
)

ax1.set_title("Box Plot of Different Data Groups")
ax1.set_ylabel("Value")
ax1.grid(True, linestyle="--", alpha=0.6)

# Customize the colors of the boxes
colors = ["lightblue", "lightgreen", "lightpink"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)


# =======================================
# 3. PLOTS WITH ERROR BARS (`ax.errorbar`)
# =======================================
# - Error bars are used to show the uncertainty or variability in a measurement.
# - They are common in scientific and experimental data visualizations.

# --- Prepare Data ---
x = np.arange(5)
y = 2.5 * x + 1 + np.random.randn(5) * 0.5  # A linear trend with noise
# Define the error for each point (e.g., standard deviation of measurements)
y_error = 0.5 + 0.5 * np.random.rand(5)

# --- Create Plot on the second Axes ---
ax2 = axes[1]
ax2.errorbar(
    x,
    y,
    yerr=y_error,  # Vertical error bars
    fmt="o-",  # Format: 'o' for markers, '-' for line
    color="salmon",
    ecolor="gray",  # Color of the error bars
    elinewidth=3,  # Thickness of error bars
    capsize=5,
)  # Size of the "caps" on the error bars

ax2.set_title("Data Points with Error Bars")
ax2.set_xlabel("Measurement Number")
ax2.set_ylabel("Measured Value")
ax2.grid(True, linestyle="--", alpha=0.6)


# =======================================
# 4. HEATMAPS (`ax.imshow`)
# =======================================
# - Heatmaps visualize 2D data by representing values as colors.
# - They are perfect for showing correlation matrices or any matrix-like data.

# --- Prepare Data ---
# Create a 5x5 matrix of random data
np.random.seed(1)
heatmap_data = np.random.rand(5, 5)

# --- Create Plot on the third Axes ---
ax3 = axes[2]
# `imshow` displays data as an image; i.e., on a 2D regular raster.
# `cmap` specifies the color map to use.
im = ax3.imshow(heatmap_data, cmap="viridis")

# --- Add a Color Bar ---
# A color bar is essential for a heatmap to serve as a legend for the colors.
fig.colorbar(im, ax=ax3)

# --- Add annotations (the numerical value) to each cell ---
for i in range(5):
    for j in range(5):
        text = ax3.text(
            j, i, f"{heatmap_data[i, j]:.2f}", ha="center", va="center", color="w"
        )

ax3.set_title("Heatmap of 2D Data")
ax3.set_xticks([])  # Hide x-axis ticks
ax3.set_yticks([])  # Hide y-axis ticks


# --- Final Touches and Display ---
plt.tight_layout()  # Adjust plots to prevent labels from overlapping
print("Displaying a figure with three specialized plot types.")
print("Close the plot window to end the script.")
plt.show()

# --- End of File ---
