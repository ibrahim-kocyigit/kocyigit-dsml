# Introduction and Motivation

Machine learning (ML) is all about creating computer programs that can automatically learn useful things from data, without needing a human to explicitly program every step.

#### What is Machine Learning?
* Machine learning is about building algorithms (sets of instructions for computers) that can find patterns and insights in data.
* The key word is "automatically". We want general methods that work on many different datasets, not specific solutions for just one problem.
* Thing of it like teaching a computer to learn on its own, rather than telling it exactly what to do.

#### Three Core Concepts
1. **Data:** This is the raw material. It could be anything: images, text, numbers, sensor readings, etc. In data science, data is often represented as tables (like spreadsheets), where rows are individual examples (e.g., a customer, an image, a document) and columns are features (e.g., age, color, a word's presence).
2. **Model:** This is a simplified representation of the process that _might_ have created the data. It's like a mathematical guess or hypothesis. For example:
    * In a simple case, a model might be a straight line trying to fit a set of points (linear regression). The line's equation is the model.
    * In a more complex case (like image recognition), the model might be a deep neural network, which is a very complicated mathematical function.
    * The model has _parameters_. These are the numbers that define the model (like the slope and intercept of the line in linear regression).
3. **Learning:** This is the process of adjusting the model's parameters so that it fits the data better. The computer uses the data to "tune" the model. The goal is to find a model that doesn't just fit the _current_ data well, but also _generalizes_ well to new, unseen data. This is crucial; we want our model to be useful in the future, not just on the data we used to train it.

#### Why Math Matters
* While you can use pre-built ML software, understanding the underlying math is essential. It's like knowing how a car engine works. You can drive without knowing, but you'll be a much better driver (and mechanic!) if you do.
* Mathematical understanding helps you:
    * **Create new ML solutions:** You can invent new methods, not just use existing ones.
    * **Debug problems:** When your model doesn't work, you can figure out why.
    * **Understand limitations:** Every ML method has assumptions and limitations. Knowing the math helps you understand these, so you don't misuse the tools.

#### Example: 
Imagine you're working for an online store, and you have data on customer purchases.

* **Data:** Your data is a table. Each row is a customer. Columns might include things like "age", "total spending", "number of items purchased", "average price per item", etc.
* **Model:** You might build a model to predict how much a new customer will spend. A simple model could be a linear regression: `spending = (a * age) + (b * number_of_items) + c`. Here, `a`, `b`, and `c` are the parameters. 
* **Learning:** The learning algorithm would use the existing customer data to find the best values for `a`, `b`, and `c` that make the model's predictions as accurate as possible. Once you've "learned" these parameters, you can use the model to predict spending for new customers.

### 1.1 Finding Words for Intuitions

