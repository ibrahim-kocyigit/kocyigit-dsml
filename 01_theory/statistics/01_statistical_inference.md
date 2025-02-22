# Statistical Inference

## What is Statistical Inference?
Statistical inference is the process of drawing conclusions about a population based on a sample of data. In machine learning, we often use statistical inference to:
* estimate model parameters,
* evaluate model performance,
* make predictions about unseen data,
* understand the relationships between variables.

## Key Concepts
* **Population:** The entire group of individuals or items that we are interested in studying. 
* **Sample:** A subset of population that we collect data from.
* **Parameter:** A numerical characteristic of a population (e.g., the population mean)
* **Statistic:** A numerical characteristic of a population (e.g., the sample mean)
* **Estimation:** Using sample statistics to estimate population parameters.
* **Hypothesis Testing:** Testing claims about population parameters.

## Example
Imagine we want to know the average height of all adults in a city (the population). It's impossible to measure everyone, so we take a random sample of 500 adults and calculate their average height (the sample mean). We can then use this sample mean to estimate the average height of the entire population.

## Types of Inference:
1. **Point Estimation:** Providing a single value as an estimate of a population parameter.
2. **Interval Estimation:** Providing a range of values within which the population parameter is likely to lie (confidence intervals).
3. **Hypothesis Testing:** Making decisions about population parameters based on sample data.

## Why is statistical inference important for machine learning?
* When we train a model, we are essentially estimating the parameters of a function that best fits the training data (our sample).
* We use statistical inference to assess how well our model generalizes to unseen data (the population).
* We use hypothesis testing to compare different models or to evaluate the significance of features.