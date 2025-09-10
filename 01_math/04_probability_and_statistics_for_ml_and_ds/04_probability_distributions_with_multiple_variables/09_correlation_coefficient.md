# Correlation Coefficient

Covariance tells us how two variables vary together:
- Positive covariance: both variables tend to increase together.
- Negative covariance: one increases while the other decreases.

However, the magnitude of covariance depends on the scale of the variables. For example, a covariance of 17 might not mean a stronger relationship than a covariance of 7.45—the numbers could just be larger.

## The Need for Standardization

To compare relationships across different datasets, we use the **correlation coefficient**.  

The correlation coefficient is always between -1 and 1:
- **+1**: perfect positive correlation (variables increase together)
- **-1**: perfect negative correlation (one increases, the other decreases)
- **0**: no correlation (variables are independent)

## Formula

The correlation coefficient ($r$) is defined as:

$$
r = \frac{\mathrm{Cov}(X, Y)}{\sigma_X \sigma_Y}
$$

Where:
- $\mathrm{Cov}(X, Y)$ is the covariance between $X$ and $Y$
- $\sigma_X$ is the standard deviation of $X$
- $\sigma_Y$ is the standard deviation of $Y$

Or equivalently:

$$
r = \frac{\mathrm{Cov}(X, Y)}{\sqrt{\mathrm{Var}(X)} \sqrt{\mathrm{Var}(Y)}}
$$

## Examples

### Age vs. Naps

- Covariance: -7.45
- Variance of age: 9.17
- Variance of naps: 39.56

Correlation coefficient:  

$$
r = \frac{-7.45}{\sqrt{9.17} \times \sqrt{39.56}} \approx -0.894
$$

### Age vs. Height

- Covariance: 17
- Variance of age: 9.17
- Variance of height: 39.56

Correlation coefficient:
$$
r = \frac{17}{\sqrt{9.17} \times \sqrt{39.56}} \approx 0.893
$$

### Age vs. Grades

- Covariance: 0.1
- Variances: much larger
- Correlation coefficient: very close to 0 (uncorrelated)

### Waiting Time vs. Customer Rating

- Covariance: -7.878
- Standard deviations: calculated from variances
- Correlation coefficient: $-0.845$ (strong negative correlation)

## Visualization

The closer the data points are to a straight line, the closer the correlation coefficient is to +1 or -1.  
- Diagonal from bottom left to top right: positive correlation
- Diagonal from top left to bottom right: negative correlation
- Scattered points: correlation near zero

**Graph:**  
{insert screenshot of scatter plots for age vs. naps, age vs. height, age vs. grades, and waiting time vs. rating}

## Key Takeaways

- The correlation coefficient standardizes covariance, allowing comparison across datasets.
- It always ranges from -1 to 1.
- The sign shows the direction of the relationship; the magnitude shows the strength.
- Useful for comparing pairs of variables in statistics and machine learning.

**Next:** []()