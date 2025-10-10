# Regression Model

## Linear Regression Model with One Variable

- **Linear Regression** is one of the most widely used learning algorithms. It fits a straight line to data.
- It is a type of **supervised learning** model.
- It is also a **regression model** because it predicts a continuous numerical output.

### Example: Housing Price Prediction

- **Goal:** Predict the price of a house based on its size.
- **Dataset:** House sizes (input) and their corresponding sale prices (output).
- **Process:**
    1. Plot the data (size vs. price).
    2. Fit a straight line to the data points.
    3. Use the line to predict the price for a new house size (e.g., a 1250 sq ft house might be predicted to sell for $220,000).

![](./images/0301.png)

### Terminology and Notation
- **Training Set:** The dataset used to train the model.
- **Input Variable (Feature):** The input data, denoted by lowercase $x$ (e.g., size of the house).
- **Output Variable (Target):** The value to predict, denoted by lowercase $y$ (e.g., price of the house).
- **Number of Training Examples:** The total number of data points in the training set, denoted by $m$.
- **A Single Training Example:** A pair $(x, y)$ representing one input and its corresponding output.
- **The $i$-th Training Example:** The $i$-th row in the dataset, denoted as $(x^{(i)}, y^{(i)})$.
    - The superscript $(i)$ is an index, not an exponent. For example, $x^{(1)}$ is the input feature for the first training example.
