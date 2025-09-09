# Covariance of a Dataset

So far, we've focused on describing a single random variable using its mean and variance. But what if we want to understand the **relationship between two variables**? For example, we can assume that as a child's age increases, their height also tends to increase.

The **covariance** is a measure that quantifies this relationship. It tells us the direction of the linear relationship between two variables.

To explore this, let's use the dataset from the video, which considers three scenarios for a group of children:
1.  **Age vs. Height:** We expect a positive relationship.
2.  **Age vs. Grades:** We might expect no clear relationship.
3.  **Age vs. Naps per day:** We expect a negative relationship.

![](./images/0601.png)

## Calculating Covariance Step-by-Step

The formula for the sample covariance is the average of the product of deviations from the mean for each variable.
```math
\text{Cov}(X, Y) = \frac{1}{n}\sum_{i=1}^{n} (x_i - \mu_x)(y_i - \mu_y)
```
*(Note: The course video uses `n` in the denominator, which is common in machine learning contexts. Some statistical formulas use `n-1`.)*

Let's calculate this for each of our three scenarios.

### Scenario 1: Age vs. Height
* **Mean of Age ($\mu_x$):** 10.5
* **Mean of Height ($\mu_y$):** 60.0

| Age (x) | Height (y) | Centered Age (x - μx) | Centered Height (y - μy) | Product |
| :---: | :---: | :---: | :---: | :---: |
| 6 | 50 | -4.5 | -10.0 | 45.0 |
| 7 | 52 | -3.5 | -8.0 | 28.0 |
| 8 | 55 | -2.5 | -5.0 | 12.5 |
| 9 | 57 | -1.5 | -3.0 | 4.5 |
| 10 | 60 | -0.5 | 0.0 | 0.0 |
| 11 | 62 | 0.5 | 2.0 | 1.0 |
| 12 | 64 | 1.5 | 4.0 | 6.0 |
| 13 | 65 | 2.5 | 5.0 | 12.5 |
| 14 | 67 | 3.5 | 7.0 | 24.5 |
| 15 | 68 | 4.5 | 8.0 | 36.0 |
| **Sum** | | | | **170.0** |

```math
\text{Cov}(\text{Age, Height}) = \frac{170.0}{10} = 17.0
```
<br>

The large positive covariance confirms the strong positive linear relationship we see in the plot.

### Scenario 2: Age vs. Naps per Day
* **Mean of Age ($\mu_x$):** 10.5
* **Mean of Naps ($\mu_y$):** 3.7

| Age (x) | Naps (y) | Centered Age (x - μx) | Centered Naps (y - μy) | Product |
| :---: | :---: | :---: | :---: | :---: |
| 6 | 8 | -4.5 | 4.3 | -19.35 |
| 7 | 7 | -3.5 | 3.3 | -11.55 |
| 8 | 6 | -2.5 | 2.3 | -5.75 |
| 9 | 5 | -1.5 | 1.3 | -1.95 |
| 10 | 4 | -0.5 | 0.3 | -0.15 |
| 11 | 3 | 0.5 | -0.7 | -0.35 |
| 12 | 2 | 1.5 | -1.7 | -2.55 |
| 13 | 1 | 2.5 | -2.7 | -6.75 |
| 14 | 1 | 3.5 | -2.7 | -9.45 |
| 15 | 0 | 4.5 | -3.7 | -16.65 |
| **Sum** | | | | **-74.5** |

```math
\text{Cov}(\text{Age, Naps}) = \frac{-74.5}{10} = -7.45
```
<br>

The large negative covariance confirms the strong negative linear relationship.

### Scenario 3: Age vs. Grades
* **Mean of Age ($\mu_x$):** 10.5
* **Mean of Grades ($\mu_y$):** 5.0

| Age (x) | Grades (y) | Centered Age (x - μx) | Centered Grades (y - μy) | Product |
| :---: | :---: | :---: | :---: | :---: |
| 6 | 5 | -4.5 | 0.0 | 0.0 |
| 7 | 7 | -3.5 | 2.0 | -7.0 |
| 8 | 8 | -2.5 | 3.0 | -7.5 |
| 9 | 3 | -1.5 | -2.0 | 3.0 |
| 10 | 1 | -0.5 | -4.0 | 2.0 |
| 11 | 1 | 0.5 | -4.0 | -2.0 |
| 12 | 6 | 1.5 | 1.0 | 1.5 |
| 13 | 10 | 2.5 | 5.0 | 12.5 |
| 14 | 2 | 3.5 | -3.0 | -10.5 |
| 15 | 7 | 4.5 | 2.0 | 9.0 |
| **Sum** | | | | **1.0** |

```math
\text{Cov}(\text{Age, Grades}) = \frac{1.0}{10} = 0.1
```
<br>

The covariance is very close to zero, confirming the lack of a clear linear relationship that we observed in the scatter plot.