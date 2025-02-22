# Descriptive Statistics

## What is Descriptive Statistics?
Descriptive statistics involves summarizing and presenting data in a meaningful way. It helps us to understand the basic properties of a dataset, such as its distribution, central tendency, and variability.

## Key Concepts
* **Measures of Central Tendency:** These describe the typical or average value of a dataset.
    * **Mean:** The arithmetic average of all values.
    * **Median:** The middle value when the data is sorted in ascending order.
    * **Mode:** The most frequently occurring value.
* **Measures of Variability:** These describe how spread out the data is.
    * **Range:** The difference between the maximum and minimum values.
    * **Interquartile Range (IQR):** The difference between the third quartile (Q3) and the first quartile (Q1), representing the spread of the middle 50% of the data.
    * **Variance:** The average squared deviation of each value from the mean.
    * **Standard Variation:** The square root of the variance, providing a measure of dispersion in the same units as the data.
* **Distribution:** The pattern of how values are distributed in a dataset.
    * **Normal Distribution:** A bell-shaped curve that is symmetric about the mean.
    * **Skewness:** The degree to which the distribution is skewed to one side.
    * **Kurtosis:** The degree to which the distribution has heavy tails or outliers.

## Python Implementation
* **NumPy:** Provides functions for calculation mean, median, mode, variance, and standard deviation.
* **Matplotlib:** Offers plotting functions to visualize distributions.

## Why is descriptive statistics important for machine learning?
Descriptive statistics helps us to:
* understand the nature of the data,
* identify outliers or unusual patterns,
* select appropriate statistical methods for analysis,
* communicate results to others.

## Example: Exam Scores Analysis
Let's say we have a dataset of exam scores for a class. We can use descriptive statistics to summarize the data.

### Mean: 79.5
The average score is 79.5, which is relatively high. This indicates that, on average, the class performed well. 
* If the mean were significantly lower, this would have indicated that the class, on average, struggled with the exam. We would assume that the exam might have been too difficult, or the students were underprepared.
* If the mean were significantly higher, this would have indicated that the class, on average, performed exceptionally well. We would assume that the exam might have been too easy, or the students were exceptionally well-prepared.

### Median: 80.5
The middle score is 80.5, which is very close to the average (79.5). This suggests that the distribution is relatively symmetrical and not heavily skewed. 
* If the median were significantly higher than the mean, the distribution would be negatively skewed (left-skewed), meaning there are more lower scores.
* If the median were significantly lower the median, the distribution would be positively skewed (right-skewed), meaning there are more higher scores.

### Mode: None
There is no mode, all scores are unique. Because there is no mode, this means that there is not a score that is heavily repeated. This indicates a diverse spread of scores. If there were a distinct mode, this would indicate that a significant number of students achieved that particular score. In that case, we would have assumed that:
* A common understanding or misunderstanding of a specific topic might have led to that common score
* The exam could have had a question that was very easy or very difficult for many students.

### Standard Deviation: 12.5
The standard deviation is 12.5, indicating a moderate spread of scores around the mean. This means that, on average, scores deviate from the mean by 12.5 points. 
* If the standard deviation were very low, this would indicate that most scores were very close to the mean. In that case, we would have assumed that:
    * The class performed very consistently
    * The exam was likely well-matched to students' abilities
* If the standard deviation were very high, this would indicate a wide range of scores. In that case, we would have assumed that:
    * There is a significant disparity in student abilities within the class
    * The exam might have been too broad, testing a wide range of knowledge levels

### Interquartile Range (IQR): 18
The range is very sensitive to outliers, so we'll use Interquartile Range. The IQR of 18 points indicates that the middle 50% of the scores fall in a 18-point range.
* If the IQR were very small, this would indicate that the middle 50% of the scores are very tightly clustered. In that case, we would have assumed that:
    * The majority of the class performed very consistently within a narrow range.
    * The exam effectively targeted the core understanding of the subject.
* If the IQR were much larger, this would indicate a wider spread in the middle 50% of the scores. In that case, we would have assumed that:
    * There is a noticeable variation in the core understanding of the subject among the majority of the students.
    * While outliers might be present, the core group of students displays a significant spread in performance.