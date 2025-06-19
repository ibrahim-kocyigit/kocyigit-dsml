import matplotlib.pyplot as plt
import numpy as np

# =======================================
# 1. WHY A NEW INTERFACE? THE LIMITS OF PYPLOT
# =======================================
# - The `pyplot` interface (`plt.plot()`, `plt.title()`, etc.) is a "state-based" interface.
# - It keeps track of the "current" figure and axes, and all `plt` commands apply to them.
# - This is simple and great for quick, interactive plots.
# - However, it can become clumsy and confusing when you need to manage multiple plots
#   or have fine-grained control over the figure elements.
#
# - The Object-Oriented (OO) interface is the solution. Here, you explicitly create
#   and hold onto figure and axes objects, then call methods directly on them.
# - The OO approach is more explicit, less ambiguous, and is the recommended
#   best practice for any non-trivial plot (e.g., in scripts, applications, or for publication).


# =======================================
# 2. THE CORE OBJECTS: `Figure` AND `Axes`
# =======================================
# - The OO interface revolves around two main objects:
#
# - `Figure`: The top-level container for everything. It's the overall window or canvas
#   that holds all the plot elements. You can think of it as the picture frame.
#
# - `Axes`: The actual plot itself — the area where data is plotted with an x-axis and y-axis.
#   A single `Figure` can contain one or more `Axes` objects (subplots).
#   Think of it as the photograph inside the frame. (Note the spelling: Axes, not Axis).


# =======================================
# 3. CREATING A FIGURE AND AXES
# =======================================
# - The `plt.subplots()` function is the most common and convenient way to start an OO plot.
# - It creates a `Figure` and a grid of `Axes` objects all at once.
# - When called with no arguments, it creates one Figure and one Axes.

print("--- Creating Figure and Axes objects ---")
# `fig` is the Figure object.
# `ax` is the Axes object.
fig, ax = plt.subplots()

print(f"Type of fig: {type(fig)}")
print(f"Type of ax: {type(ax)}")
print("-" * 30)


# =======================================
# 4. A SIMPLE PLOT WITH THE OO INTERFACE
# =======================================
# - Let's re-create the simple plot from our first lesson, but this time using OO methods.

# --- Step 1: Prepare Data ---
x_data = np.linspace(0, 10, 50)
y_data = x_data**2

# --- Step 2: Create Figure and Axes ---
# We already did this above, but we'll do it again for a complete example.
fig, ax = plt.subplots(figsize=(8, 6))  # Can still control figure size here

# --- Step 3: Plot data on the Axes object ---
# Instead of `plt.plot()`, we call the `.plot()` method on our `ax` object.
ax.plot(x_data, y_data)


# --- Compare to the pyplot interface ---
# Pyplot way (implicit):
#   plt.plot(x_data, y_data)
#
# OO way (explicit):
#   ax.plot(x_data, y_data)
#
# The OO way is clearer about *where* the plot is being drawn.


# --- Step 4: Show the Plot ---
# `plt.show()` is still used at the end to display the figure.
print("Displaying a simple plot using the Object-Oriented interface.")
print("The next lesson will cover how to add titles and labels using this interface.")
plt.show()


# =======================================
# 5. SUMMARY OF THE OO WORKFLOW
# =======================================
# 1. `import matplotlib.pyplot as plt`
# 2. Prepare your data (e.g., with NumPy).
# 3. Create a Figure and Axes: `fig, ax = plt.subplots()`
# 4. Use `ax` methods to plot and customize: `ax.plot()`, `ax.set_title()`, etc.
# 5. Display the figure: `plt.show()`

# --- End of File ---
