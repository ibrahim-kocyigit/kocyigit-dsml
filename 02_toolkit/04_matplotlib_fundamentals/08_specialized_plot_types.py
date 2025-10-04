import matplotlib.pyplot as plt
import numpy as np

# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. Introduction
# 2. Box Plots (`ax.boxplot`)
# 3. Plots with Error Bars (`ax.errorbar`)


# =======================================
# 1. INTRODUCTION
# =======================================
# - Beyond the basics, Matplotlib supports a wide variety of specialized plots
#   that are crucial for statistical analysis and representing complex data.
# - We will cover three important types using the Object-Oriented interfacce:
#   1. Box Plots: For visualizing data distribution and outliers.
#   2. Error Bars: For showing uncertainty in measurements.
#   3. Heatmaps: For visualizing 2D data as a grid of colors.

# --- Setup a figure with 3 subplots side-by-side ---
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))


# =======================================
# 2. BOX PLOTS (`ax.boxplot`)
# =======================================
# - A box plot (or box-and-whisher plot) is a standardized way of displaying
#   the distribution of data based on a five-number summary:
#   minimum, first quartile (Q1), median, third quartile (Q3), and maximum.
# - It is excellent for comparing distributions across multiple groups.

# --- Prepare Data ---
# Create three different datasets to compare
np.random.seed(10)
data1 = np.random.normal(100, 10, 200)  # mean=100, std=10
data2 = np.random.normal(80, 30, 200)  # mean=80, std=30
data3 = np.random.normal(90, 20, 200)  # mean=90, std=20
data_to_plot = [data1, data2, data3]

# --- Create Plot on the first Axes ---
ax1 = axes[0]
# `patch_artis=True` fills the boxes with color
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
