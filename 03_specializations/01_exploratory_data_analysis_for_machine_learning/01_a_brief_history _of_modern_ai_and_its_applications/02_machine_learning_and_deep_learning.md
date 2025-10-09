# Machine Learning and Deep Learning

## What is Machine Learning?

- **Machine Learning (ML)** is the study and construction of programs that are not explicitly programmed, but instead learn patterns from data as they are exposed to more data over time.
- ML is a subset of Artificial Intelligence (AI) that focuses on learning from data rather than following hard-coded rules.
- As more data is provided, ML algorithms generally improve at finding underlying patterns, though performance gains eventually plateau (diminishing returns).

## How Machine Learning Works

- ML programs learn from repeatedly seeing data, not from explicit human programming.
- **Example:** Spam Detection
    - Start with a labeled dataset (emails marked as spam or not spam).
    - The ML algorithm learns patterns that distinguish spam from non-spam.
    - Once trained, the model can predict whether new, unseen emails are spam.

## Features and Target
- **Features:** The input variables used to make predictions (e.g., sepal length, petal width).
- **Target:** The output variable the model is trying to predict (e.g., flower species, spam/not spam).
- **Example:** The classic **iris dataset** has four features (sepal length, sepal width, petal length, petal width) and the target is the species (virginica, setosa, versicolor).

## Types of Machine Learning

### Supervised Learning

- **Dataset:** Has a target column (labels).
- **Goal:** Predict the label (e.g., spam or not spam, flower species).
- **Example:** Fraud detection (predicting if a transaction is fraudulent based on labeled data).

### Unsupervised Learning

- **Dataset:** No target column (no labels).
- **Goal:** Find underlying structure or groupings in the data.
- **Example:** Customer segmentation (grouping customers for marketing without predefined labels).

## Features in Different Data Types

- **Structured Data:** Features are often intuitive (e.g., transaction time, amount, location).
- **Images:** Each pixel can be a feature (e.g., a 256x256 image has 65,536 features).
  - Classic ML struggles with images because:
    - Too many features.
    - Loss of spatial relationships between pixels.
  - **Deep Learning** overcomes these limitations by learning features automatically.

## Deep Learning

- **Deep Learning (DL):**  
  - A subset of ML using deep neural networks (models with many layers).
  - Learns complex features and representations directly from raw data (e.g., pixels in images).
  - Excels at tasks like image classification and natural language processing.
- In classic ML, humans must define features before training the model.
- In DL, the neural network learns to extract and combine features automatically.

## When to Use Machine Learning vs. Deep Learning

- **Deep Learning** is state-of-the-art for large, complex datasets (especially images, audio, text).
- **Classic Machine Learning** often performs better on smaller datasets or when data changes frequently.
- For small or unstable datasets, traditional ML algorithms may outperform deep learning.

## Key Differences: Classic ML vs. Deep Learning

| Classic Machine Learning         | Deep Learning                        |
|----------------------------------|--------------------------------------|
| Requires manual feature engineering | Learns features automatically      |
| Works well with structured/tabular data | Excels with unstructured data (images, text) |
| Simpler models, easier to interpret | Complex models, often less interpretable |
| Performs well with small/medium datasets | Requires large datasets for best performance |

## Summary

- ML learns from data, not explicit rules.
- Supervised learning uses labeled data; unsupervised learning finds structure in unlabeled data.
- Deep learning uses neural networks to automatically learn features, especially useful for complex data like images.
- Classic ML is still valuable, especially for smaller or changing datasets.

---

**Next:** [History of AI](./03_history_of_ai.md)