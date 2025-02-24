import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats  # You'll need this for one part

# The following dataset represents the scores of students on a test.
scores = np.array([75, 82, 90, 68, 85, 78, 92, 95, 70, 88, 72, 80, 85, 98, 76])

# 1. Central Tendency:

# a) Calculate the mean score.
mean_score = # YOUR CODE HERE
print(f"Mean score: {mean_score}")

# b) Calculate the median score.
median_score = # YOUR CODE HERE
print(f"Median score: {median_score}")

# c) Calculate the mode score(s).
mode_score = # YOUR CODE HERE
print(f"Mode score(s): {mode_score}")

# 2. Dispersion:

# a) Calculate the variance of the scores (treat this as a sample).
variance_score = # YOUR CODE HERE
print(f"Variance: {variance_score}")

# b) Calculate the standard deviation of the scores (treat this as a sample).
std_dev_score = # YOUR CODE HERE
print(f"Standard Deviation: {std_dev_score}")

# c) Calculate the range of the scores.
range_score = # YOUR CODE HERE
print(f"Range: {range_score}")

# d) Calculate the interquartile range (IQR) of the scores.
iqr_score = # YOUR CODE HERE
print(f"IQR: {iqr_score}")

# 3. Visualization:

# a) Create a histogram of the scores.  Use 5 bins.  Add appropriate labels and title.
# YOUR CODE HERE

# b) Create a box plot of the scores. Add appropriate labels and title.
# YOUR CODE HERE

# 4. DataFrame Operations:
#    Create a Pandas DataFrame from the 'scores' array, with a column named 'Score'.

df_scores = # YOUR CODE HERE
print(df_scores.head())

# 5. Data Selection

# a) Create df_above_90 which includes the students with the score above 90
df_above_90 = # YOUR CODE HERE
print(df_above_90)
# 6. (Bonus - a little trickier):

# a)  Calculate the *population* variance and *population* standard deviation.
#     Store them in variables named 'pop_variance' and 'pop_std_dev'.
pop_variance =  # YOUR CODE HERE
pop_std_dev = # YOUR CODE HERE
print(f"Population Variance: {pop_variance}")
print(f"Population Standard Deviation: {pop_std_dev}")