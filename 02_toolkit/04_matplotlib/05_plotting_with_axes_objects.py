import matplotlib.pyplot as plt
import numpy as np

# =======================================
# 1. PLOTTING WITH THE `Axes` OBJECT
# =======================================
# - Once we have an `Axes` object (which we get from `plt.subplots()`), we can
#   use its methods to create and customize our plot.
# - This gives us explicit control over a specific plot, which is essential
#   when working with multiple subplots in one figure.
#
# - Naming Convention: Many `pyplot` functions have an equivalent `Axes` method.
#   The main difference is the use of `set_*` for labels and titles.
#
#   Pyplot (`plt`)        | Object-Oriented (`ax`)
#   -------------------------------------------------
#   plt.title('My Title')  | ax.set_title('My Title')
#   plt.xlabel('X')        | ax.set_xlabel('X')
#   plt.ylabel('Y')        | ax.set_ylabel('Y')
#   plt.xlim(0, 10)        | ax.set_xlim(0, 10)
#   plt.ylim(-1, 1)        | ax.set_ylim(-1, 1)
#   plt.grid(True)         | ax.grid(True)
#   plt.legend()           | ax.legend()
#   plt.plot(...)          | ax.plot(...)


# =======================================
# 2. BUILDING A PLOT (THE OO WAY)
# =======================================
# - Let's re-create the labeled sine/cosine plot from lesson 2, but this
#   time using the object-oriented approach.

print("--- Building a plot with the OO interface ---")
# --- Step 1: Prepare Data ---
x = np.linspace(0, 10, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)


# --- Step 2: Create a Figure and an Axes object ---
# This is our standard starting point for OO plotting.
fig, ax = plt.subplots(figsize=(10, 6))
print(f"Created a Figure object: {type(fig)}")
print(f"Created an Axes object: {type(ax)}")


# --- Step 3: Plot data directly onto the Axes (`ax`) ---
ax.plot(x, y_sin, label="Sine Wave")
ax.plot(x, y_cos, label="Cosine Wave")


# --- Step 4: Customize the plot using `ax` methods ---
# Use the `set_*` methods to add labels and a title.
ax.set_title("Sine and Cosine Functions (OO Style)")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Set the limits for the axes.
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

# Add a grid.
ax.grid(True)

# Add a legend.
ax.legend()


# --- Step 5: Show the Plot ---
# `plt.show()` is still used to display the final figure.
print("\nDisplaying the fully labeled plot created with OO methods.")
print("Close the plot window to end the script.")
plt.show()

# --- End of File ---
