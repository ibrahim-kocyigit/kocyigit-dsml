# Introduction and Motivation

### What is Machine Learning?
* Machine learning is about building algorithms (sets of instructions for computers) that can find patterns and insights in data.
* The key word is "automatically". We want general methods that work on many different datasets, not specific solutions for just one problem.
* Thing of it like teaching a computer to learn on its own, rather than telling it exactly what to do.

### Three Core Concepts
1. **Data:** This is the raw material. It could be anything: images, text, numbers, sensor readings, etc. In data science, data is often represented as tables (like spreadsheets), where rows are individual examples (e.g., a customer, an image, a document) and columns are features (e.g., age, color, a word's presence).
2. **Model:** This is a simplified representation of the process that _might_ have created the data. It's like a mathematical guess or hypothesis. For example:
    * In a simple case, a model might be a straight line trying to fit a set of points (linear regression). The line's equation is the model.
    * In a more complex case (like image recognition), the model might be a deep neural network, which is a very complicated mathematical function.
    * The model has _parameters_. These are the numbers that define the model (like the slope and intercept of the line in linear regression).
3. **Learning:** This is the process of adjusting the model's parameters so that it fits the data better. The computer uses the data to "tune" the model. The goal is to find a model that doesn't just fit the _current_ data well, but also _generalizes_ well to new, unseen data. This is crucial; we want our model to be useful in the future, not just on the data we used to train it.

### Why Math Matters
* While you can use pre-built ML software, understanding the underlying math is essential. It's like knowing how a car engine works. You can drive without knowing, but you'll be a much better driver (and mechanic!) if you do.
* Mathematical understanding helps you:
    * **Create new ML solutions:** You can invent new methods, not just use existing ones.
    * **Debug problems:** When your model doesn't work, you can figure out why.
    * **Understand limitations:** Every ML method has assumptions and limitations. Knowing the math helps you understand these, so you don't misuse the tools.

### Example: 
Imagine you're working for an online store, and you have data on customer purchases.

* **Data:** Your data is a table. Each row is a customer. Columns might include things like "age", "total spending", "number of items purchased", "average price per item", etc.
* **Model:** You might build a model to predict how much a new customer will spend. A simple model could be a linear regression: `spending = (a * age) + (b * number_of_items) + c`. Here, `a`, `b`, and `c` are the parameters. 
* **Learning:** The learning algorithm would use the existing customer data to find the best values for `a`, `b`, and `c` that make the model's predictions as accurate as possible. Once you've "learned" these parameters, you can use the model to predict spending for new customers.

## 1.1 Finding Words for Intuitions

A key challenge in ML is the ambiguity of language. The same terms can have different meanings depending on the context. We'll highlight this and introduce core ML concepts in this section.

### Ambiguity in Machine Learning Terminology
It's important to be mindful of context to understand the intended meaning.

* **Example: "Algorithm":**
    * **Sense 1 (Predictor):** A system that makes predictions based on input data. Think of this as the _trained_ model you use to make predictions.
    * **Sense 2 (Training):** A system that _adjusts_ the internal parameters of a predictor (Sense 1) to improve its performance on future, unseen data. This is the process of _creating_ the trained model.  

### Core Components of a Machine Learning System (Revisited)
1. **Data as Vectors:**
    * While data can take many forms, in ML, we often represent data numerically. 
    * We treat data as _vectors_. In data science, a vector is usually an array of numbers representing features.
    * Example: If a vector which represents a house has elements `[120, 3, 2015]`, that might mean that the house has 120 square meter area, 3 rooms, and built in 2015.
2. **Model:**
    * A simplified representation of the (unknown) process that generated the data.
    * Captures relevant patterns and allows for prediction.
    * A good model acts like a stand-in for the real-world process, allowing us to make predictions without running real-world experiments.
3. **Learning:**
    * The process of optimizing a model's parameters using a dataset.
    * We use a _utility function_ (or _loss function_ or _objective function_) to evaluate how well the model fits the training data.
    * An analogy: Think of training as hill climbing. The peak represents the best possible model performance.
    * Crucial point: The goal isn't just to fit the _training_ data perfectly (memorization). We want the model to _generalize_ well to new, _unseen_ data. This is what makes the model useful in real-world applications. 