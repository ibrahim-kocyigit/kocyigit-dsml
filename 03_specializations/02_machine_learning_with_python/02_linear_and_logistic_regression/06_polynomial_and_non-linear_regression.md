# Polynomial and Non-Linear Regression

## 1. The Intuitive Idea: Beyond the Straight Line

So far, we've focused on linear regression, which tries to fit a straight line to our data. However, real-world data is rarely so simple. Often , the relationship between our features and the target follows a curve. 

If we try to fit a stright line to data that is clearly curved, our model will be too simplistic and will make poor decisions. This is known as **underfitting**.

<img src="./images/0601.png" alt="Linear vs Non-linear fit" width="400"/>

**Non-Linear Regression** is a broad category of methods used to model these curved, non-linear relationships between variables.

## 2. Polynomial Regression: The "Linear" Trick

Polynomial regression is one of the simplest and most common ways to model non-linear relationships. Instead of fitting a straight line, we fit a polynomial curve (like a quatratic or cubic curve) to the data.

The model equation looks like this:  

$$ \hat{y} = \theta_0 + \theta_1 x + \theta_2 x^2 + \dots + \theta_n x^n $$

Where:
*   $\hat{y}$ is the predicted value.
*   $x$ is the original independent variable.
*   $x^2, x^3, \dots, x^n$ are the new polynomial features.
*   $n$ is the degree of the polynomial.

<img src="./images/0602.png" alt="" width="800"/>

### The Trick: Transforming it into a Linear Problem

How do we solve this? We can transform this into a **Multiple Linear Regression** problem with a clever trick: we treat each polynomial term as a *new, separate feature*.

Let's say we have a cubic model ($n=3$):  

$$ \hat{y} = \theta_0 + \theta_1 x + \theta_2 x^2 + \theta_3 x^3 $$

We can define new features:
*   $x_1 = x$
*   $x_2 = x^2$
*   $x_3 = x^3$

Now, our equation becomes:
$$ \hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3 $$