# Linear Regression: Introduction

## 1. The Intuitive Idea: From a Single Average to a Smart Prediction

Imagine you're asked to predict the cartwheel distance for the next person who walks into your study. Looking at the data from 25 people, you see that distances vary, but they cluster around an average.

Your simplest, most basic prediction would be to just use the overall mean: **82.48 inches**. This is your best guess for *anyone*, regardless of their characteristics.

{{ Insert screenshot of the histogram/Q-Q plot for cartwheel distance here }}

But common sense suggests this isn't the whole story. A person's physical attributes, like their height, might influence how far their cartwheel goes. It's plausible that taller people have longer limbs and can therefore travel a greater distance.

This is the core idea of linear regression: we move from a "one-size-fits-all" model (the overall mean) to a more sophisticated model that makes a **conditional prediction**. Instead of asking "What's the average cartwheel distance?", we ask, "**For a person of a specific height**, what is the expected cartwheel distance?"

## 2. Exploring the Relationship: Before We Build the Model

Before fitting a formal model, we must first explore the relationship between our two variables:
*   **Dependent Variable (DV):** `Cartwheel Distance` (the outcome we want to predict).
*   **Independent Variable (IV):** `Height` (the predictor we want to use).

### Step 1: Visualize with a Scatter Plot

A scatter plot is the most important tool for examining the relationship between two quantitative variables.

{{ Insert screenshot of the scatter plot of Cartwheel Distance vs. Height here }}

When describing a scatter plot, we look for four things:
1.  **Form:** Is the overall pattern linear (straight line) or curved? Here, it looks **approximately linear**.
2.  **Direction:** As one variable increases, does the other tend to increase or decrease? Here, it is **positive** (taller people tend to have longer cartwheel distances).
3.  **Strength:** How tightly are the points clustered around the form? The points are somewhat scattered, so we'd call the strength **weak to moderate**.
4.  **Outliers:** Are there any individual points that stray far from the overall pattern? There don't appear to be any major outliers.

### Step 2: Quantify with Correlation and R-Squared

Visuals are great, but we also need numbers to quantify the relationship's strength.

*   **Correlation Coefficient (r):** This measures the strength and direction of the *linear* relationship.
    *   $r = 0.33$
    *   The positive sign confirms the positive direction. The value, 0.33, confirms our visual assessment of a weak-to-moderate linear relationship.

*   **R-Squared ($R^2$):** This is arguably the more important metric. It tells us the **proportion of the variability in the dependent variable that can be explained by its linear relationship with the independent variable.**
    *   $R^2 = (0.33)^2 \approx 0.11$ or **11%**.
    *   **Interpretation:** Cartwheel distances vary a lot from person to person. Our model, which uses `height` as a predictor, can account for about **11% of that total variation**. The other 89% is due to other factors not included in our model (e.g., athletic ability, age, effort, random chance).

## 3. The Theoretical Framework: The Method of Least Squares

Our goal is to find the single "best" straight line that describes the data. But what does "best" mean?

Imagine drawing a potential line through the data. For every actual data point, there's a vertical distance between the point and the line. This distance is the **error** or **residual**—the difference between the *observed* value and the value *predicted* by the line.

$$
\text{Residual} = \text{Observed } Y - \text{Predicted } Y
$$

Some residuals will be positive (the point is above the line) and some will be negative (the point is below the line). We want to find the line that makes these residuals as small as possible overall.

The **Method of Least Squares** is the criterion we use. It states that the best-fitting line is the one that **minimizes the sum of the squared residuals**. We square them to prevent positive and negative errors from canceling each other out and to penalize larger errors more heavily.

### The Linear Regression Model

The equation for our line is:
$$
\hat{Y} = b_0 + b_1X
$$
Where:
*   $\hat{Y}$ ("y-hat") is the **predicted value** of the dependent variable.
*   $X$ is the value of the independent variable.
*   $b_0$ is the **Y-intercept**: the predicted value of Y when X is 0.
*   $b_1$ is the **slope**: the estimated change in Y for a one-unit increase in X.

Using software that implements the least squares method, we get our estimated coefficients:
*   $b_0 = 7.55$ (Intercept)
*   $b_1 = 1.10$ (Slope)

So, our final prediction equation is:
$$
\text{Predicted Cartwheel Distance} = 7.55 + 1.10 \times (\text{Height})
$$

**Interpretation of the Slope ($b_1$):** "For every one-inch increase in an adult's height, we estimate that their average cartwheel distance increases by **1.10 inches**." This is usually the most important parameter for inference.

## 4. Using the Model for Prediction

Once we have our equation, making predictions is straightforward.

**Question:** What is the predicted cartwheel distance for an adult who is 64 inches tall?

$$
\text{Predicted Distance} = 7.55 + 1.10 \times (64) = 78.4 \text{ inches}
$$

It's important to note that this is a prediction of the *average* distance for all people who are 64 inches tall. Any single individual might be different.

We can now calculate the residual for an actual person in our dataset who was 64 inches tall and had a distance of 87 inches:

$$
\text{Residual} = \text{Observed} - \text{Predicted} = 87 - 78.4 = +8.6 \text{ inches}
$$
This person's cartwheel was 8.6 inches longer than our model predicted based on their height. These residuals will become critical for checking our model's assumptions later.

**A Note on Extrapolation:** We should only make predictions for X values that fall within the range of our original data (in this case, heights from roughly 58 to 76 inches). Predicting for an `X` value far outside this range is called **extrapolation** and is very risky, as we have no evidence that the linear relationship holds.

## 5. What's Next?

So far, we have focused on the *descriptive* side of regression—fitting a line to our sample data. Next, we will move to the *inferential* side:
*   Assessing if the relationship we found is statistically significant.
*   Checking the assumptions that must be met for our inferences to be valid.
*   Expanding our model to include more than one predictor variable.


---

**Next:** [Linear Regression: Inference](./02_linear_regression--inference.md)