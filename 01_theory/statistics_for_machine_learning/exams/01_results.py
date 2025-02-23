import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats  # You'll need this for one part

# The following dataset represents the scores of students on a test.
scores = np.array([75, 82, 90, 68, 85, 78, 92, 95, 70, 88, 72, 80, 85, 98, 76])

# 1. Central Tendency:

# a) Calculate the mean score.
mean_score = np.mean(scores)
print(f"Mean score: {mean_score}")

# b) Calculate the median score.
median_score = np.median(scores)
print(f"Median score: {median_score}")

# c) Calculate the mode score(s).
mode_score = stats.mode(scores).mode
print(f"Mode score(s): {mode_score}")

# 2. Dispersion:

# a) Calculate the variance of the scores (treat this as a sample).
variance_score = np.var(scores, ddof=1)
print(f"Variance: {variance_score}")

# b) Calculate the standard deviation of the scores (treat this as a sample).
std_dev_score = np.std(scores, ddof=1)
print(f"Standard Deviation: {std_dev_score}")

# c) Calculate the range of the scores.
range_score = np.max(scores) - np.min(scores)
print(f"Range: {range_score}")

# d) Calculate the interquartile range (IQR) of the scores.
iqr_score = stats.iqr(scores)
print(f"IQR: {iqr_score}")

# 3. Visualization:

# a) Create a histogram of the scores.  Use 5 bins.  Add appropriate labels and title.
plt.hist(scores, bins=5, edgecolor="black")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Histogram of Exam Scores")
plt.show()

# b) Create a box plot of the scores. Add appropriate labels and title.
plt.boxplot(scores)
plt.ylabel("Score")
plt.title("Box Plot of Exam Scores")
plt.show()

# 4. DataFrame Operations:
#    Create a Pandas DataFrame from the 'scores' array, with a column named 'Score'.
df_scores = pd.DataFrame(scores, columns=["Score"])
print(df_scores.head())

# 5. Data Selection

# a) Create df_above_90 which includes the students with the score above 90
df_above_90 = df_scores[df_scores["Score"] > 90]
print(df_above_90)
# 6. (Bonus - a little trickier):

# a)  Calculate the *population* variance and *population* standard deviation.
#     Store them in variables named 'pop_variance' and 'pop_std_dev'.
pop_variance = np.var(df_scores["Score"])
pop_std_dev = np.std(df_scores["Score"])
print(f"Population Variance: {pop_variance}")
print(f"Population Standard Deviation: {pop_std_dev}")
