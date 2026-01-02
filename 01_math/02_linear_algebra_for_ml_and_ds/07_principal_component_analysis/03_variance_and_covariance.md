# Variance and Covariance

As mentioned before, PCA relies on a few core statistical concepts:

### The Mean
The **mean** is the average value of all observations in a dataset. Geometrically, it represents the "center of mass" of your data points.

For a 2D dataset, the mean point has the coordinates $(\mu_x, \mu_y)$, where $\mu_x$ is the average of all x-values and $\mu_y$ is the average of all y-values.

$$
\mu_x = \frac{1}{n}\sum_{i=1}^{n} x_i \quad , \quad \mu_y = \frac{1}{n}\sum_{i=1}^{n} y_i 
$$

### Variance: A Measure of Spread

While the mean tells us the center of our data, **variance** tells us how spread out the data is from that center. A small variance means the data is tightly clustered, while a large variance means it's widely dispersed.

We can look at the variance along each axis separately. In the plot below, you can see that the data is more spread out along the horizontal (x-axis) than the vertical (y-axis). Therefore, the x-variance is larger than the y-variance.

![](./images/0301.png)

The formula for the variance of a variable `x` is:  

$$
\text{Var}(x) = \sigma^2 = \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \mu_x)^2 
$$

This is the **average squared distance** of each point from the mean. The key takeaway is that as your data becomes more spread out, the variance increases.

## Covariance: A Measure of Joint Variance

Variance alone isn't enough to describe a dataset. Two datasets could have the exact same variance for `x` and `y`, but show completely different patterns.

**Covariance** measures how two variables vary *together*.
* **Positive Covariance:** As `x` increases, `y` tends to increase.
* **Negative Covariance:** As `x` increases, `y` tends to decrease.
* **Zero Covariance:** There is no linear relationship between `x` and `y`.

The formula for covariance is similar to variance:  

$$
\text{Cov}(x, y) = \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \mu_x)(y_i - \mu_y) 
$$

We can understand this formula by dividing our data into four quadrants centered on the mean point $(\mu_x, \mu_y)$.

![Covariance](./images/0302.png)

* **Quadrant 1 (Top-Right):** Points here are above the mean for both `x` and `y`. The term $(x_i - \mu_x)(y_i - \mu_y)$ will be `(positive) * (positive) = positive`.
* **Quadrant 2 (Top-Left):** Points have `x` below its mean but `y` above its mean. The term will be `(negative) * (positive) = negative`.
* **Quadrant 3 (Bottom-Left):** Points are below the mean for both `x` and `y`. The term will be `(negative) * (negative) = positive`.
* **Quadrant 4 (Bottom-Right):** Points have `x` above its mean but `y` below its mean. The term will be `(positive) * (negative) = negative`.

Covariance is essentially the average of these products.
* If most points are in the **positive quadrants** (1 and 3), the covariance will be **positive**.
* If most points are in the **negative quadrants** (2 and 4), the covariance will be **negative**.
* If points are spread evenly, the terms cancel out, and the covariance is near **zero**.

---

**Next:** [Covariance Matrix](./04_covariance_matrix.md)