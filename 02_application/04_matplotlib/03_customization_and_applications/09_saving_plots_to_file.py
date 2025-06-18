# 09_saving_plots_to_file.py

import matplotlib.pyplot as plt
import numpy as np
import os

# =======================================
# 1. INTRODUCTION
# =======================================
# - While `plt.show()` is great for interactive viewing, you'll often need to save
#   your plots to image files for use in reports, presentations, or web pages.
# - The primary method for this is `fig.savefig()` when using the OO interface.

# --- Setup a folder for our saved plots ---
SAVE_FOLDER = "matplotlib_saved_plots"
os.makedirs(SAVE_FOLDER, exist_ok=True)


# =======================================
# 2. CREATING A PLOT TO SAVE
# =======================================
# - Let's first create a high-quality plot that we'll want to save.
# - We'll plot a damped sine wave as an example.

# --- Prepare Data ---
x = np.linspace(0, 5, 200)
y = np.exp(-x) * np.cos(2 * np.pi * x)  # Damped sine wave

# --- Create Figure and Axes ---
fig, ax = plt.subplots(figsize=(10, 6))

# --- Plot and Customize ---
ax.plot(x, y, label="Damped Sine Wave", color="navy")
ax.set_title("Example of a Well-Formed Plot", fontsize=16)
ax.set_xlabel("Time (s)", fontsize=12)
ax.set_ylabel("Amplitude", fontsize=12)
ax.legend()
ax.grid(True, linestyle=":", alpha=0.7)

print("--- Created a sample plot to be saved ---")
print("-" * 30)


# =======================================
# 3. SAVING THE FIGURE WITH `fig.savefig()`
# =======================================
# - This method saves the `Figure` object to a file.
# - Matplotlib can infer the file format from the extension (e.g., .png, .jpg, .pdf, .svg).

print("--- Saving the figure in different formats ---")
# --- Basic Save to PNG ---
path_png = os.path.join(SAVE_FOLDER, "my_plot.png")
try:
    fig.savefig(path_png)
    print(f"Successfully saved plot to '{path_png}'")
except Exception as e:
    print(f"Error saving file: {e}")

# --- Save to PDF (good for vector graphics) ---
path_pdf = os.path.join(SAVE_FOLDER, "my_plot.pdf")
fig.savefig(path_pdf)
print(f"Successfully saved plot to '{path_pdf}'")
print("-" * 30)


# =======================================
# 4. KEY PARAMETERS FOR `savefig()`
# =======================================
# - You can control the quality and appearance of the saved file.

print("--- Saving with different options ---")
# --- `dpi` (Dots Per Inch) ---
# - Controls the resolution of the saved image. Higher DPI means higher quality.
# - 300 is a common value for publication-quality images.
path_high_res = os.path.join(SAVE_FOLDER, "my_plot_high_res.png")
fig.savefig(path_high_res, dpi=300)
print(f"Saved high-resolution (300 DPI) plot to '{path_high_res}'")


# --- `bbox_inches='tight'` ---
# - A very useful parameter that trims excess whitespace around the plot.
path_tight = os.path.join(SAVE_FOLDER, "my_plot_tight.png")
fig.savefig(path_tight, bbox_inches="tight")
print(f"Saved plot with tight bounding box to '{path_tight}'")


# --- `transparent=True` ---
# - Makes the figure background transparent. Useful for web or presentation slides.
path_transparent = os.path.join(SAVE_FOLDER, "my_plot_transparent.png")
fig.savefig(path_transparent, transparent=True, dpi=150)
print(f"Saved plot with transparent background to '{path_transparent}'")
print("-" * 30)


# =======================================
# 5. IMPORTANT: `savefig()` and `show()`
# =======================================
# - A common pitfall: By default, `plt.show()` clears the figure after displaying it.
# - If you call `savefig()` *after* `show()`, you might save a blank image.
#
# - BEST PRACTICE: Save the figure *before* you show it.
#
#   Correct Order:
#   1. Create plot
#   2. Customize plot
#   3. `fig.savefig(...)`
#   4. `plt.show()`

print("--- `savefig` before `show` ---")
# We have already saved our figures above. Now we can show the plot interactively.
print("Displaying the plot. The script will end after the window is closed.")
plt.show()

# --- End of File ---
