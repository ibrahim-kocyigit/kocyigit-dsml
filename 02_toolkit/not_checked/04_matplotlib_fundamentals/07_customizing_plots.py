# 07_customizing_plots.py

import matplotlib.pyplot as plt
import numpy as np

# =======================================
# 1. INTRODUCTION TO CUSTOMIZATION
# =======================================
# - The default plots are good, but the real power of Matplotlib is in customizing
#   every detail to make your visualizations clearer and more professional.
# - We can control colors, line styles, markers, text, annotations, and much more.
# - We will continue to use the Object-Oriented (OO) interface (`fig, ax`).


# =======================================
# 2. COLORS, LINESTYLES, AND MARKERS
# =======================================
# - These are the most common customizations, passed as arguments to `ax.plot()`.

# --- Prepare Data ---
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = 0.1 * x**2 - 5 # A quadratic curve

# --- Create Figure and Axes ---
fig, ax = plt.subplots(figsize=(12, 7))


# --- Plotting with Customizations ---

# Plot 1: Dashed blue line, with a thicker line
ax.plot(x, y1,
        color='blue',         # Can use names, hex codes ('#0000FF'), or RGB tuples
        linestyle='--',       # Other options: '-', ':', '-.'
        linewidth=2,          # Control line thickness
        label='Sine (Dashed)')

# Plot 2: Red dotted line
ax.plot(x, y2,
        color='red',
        linestyle=':',
        label='Cosine (Dotted)')

# Plot 3: Green line with circle markers
# `linestyle=''` means only the markers will be drawn.
ax.plot(x, y3,
        color='green',
        linestyle='-',
        marker='o',           # Other options: '.', 's', '^', 'x', '*'
        label='Quadratic (Line with Markers)')


# --- Finalize Plot Elements ---
ax.set_title('Customized Plot with Different Styles')
ax.set_xlabel('X Value')
ax.set_ylabel('Y Value')
ax.legend()
ax.grid(True)
# plt.show() # We will show all plots at the end
print("--- Generated a plot with custom colors, linestyles, and markers ---")
print("-" * 30)


# =======================================
# 3. ADJUSTING AXIS TICKS AND LABELS
# =======================================
# - You can control the exact location and labels of the "ticks" on each axis.

fig2, ax2 = plt.subplots(figsize=(10, 5))

x_ticks_data = np.linspace(0, 2 * np.pi, 100)
y_ticks_data = np.sin(x_ticks_data)

ax2.plot(x_ticks_data, y_ticks_data)
ax2.set_title('Plot with Custom Axis Ticks')

# --- Set specific locations for the x-axis ticks ---
ax2.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])

# --- Set custom labels for those ticks ---
# We can use LaTeX formatting for mathematical symbols by enclosing them in '$'.
ax2.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])

# Also adjust y-axis limits and ticks
ax2.set_ylim(-1.5, 1.5)
ax2.set_yticks([-1, 0, 1])

print("--- Generated a plot with custom axis ticks and labels ---")
print("-" * 30)


# =======================================
# 4. ADDING TEXT AND ANNOTATIONS
# =======================================
# - `ax.text()` places text at a specific coordinate on the plot.
# - `ax.annotate()` is more powerful, allowing you to draw an arrow from the
#   text to a specific point of interest.

fig3, ax3 = plt.subplots(figsize=(10, 6))

ax3.plot(x, y1)
ax3.set_title('Plot with Text and Annotations')

# --- Using `ax.text()` ---
ax3.text(1, -0.5, 'Some example text', fontsize=12, color='red')

# --- Using `ax.annotate()` ---
# Let's annotate the first peak of the sine wave.
peak_x = np.pi / 2
peak_y = np.sin(peak_x)

ax3.annotate(
    'First Peak',                     # The text to display
    xy=(peak_x, peak_y),              # The point (x,y) to annotate
    xytext=(peak_x + 1, peak_y + 0.5),  # The position (x,y) of the text
    arrowprops=dict(facecolor='black', shrink=0.05) # Style of the arrow
)

ax3.grid(True)
print("--- Generated a plot with text and an arrow annotation ---")


# --- Display all created figures ---
print("\nDisplaying all plots. Close the plot windows to end the script.")
plt.show()

# --- End of File ---