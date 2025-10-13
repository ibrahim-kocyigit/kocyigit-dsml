# Machine Learning: An Overview

## What is Machine Learning?

**Machine Learning (ML)** is a subset of Artificial Intelligence (AI) that teaches computers to learn from data, identify patterns, and make decisions without receiving explicit instructions.

- **AI**: The broad field of making computers appear intelligent by simulating human cognitive abilities.
- **ML**: The subset of AI that uses algorithms and requires **feature engineering** by practitioners.
- **Deep Learning**: A subset of ML that uses many-layered neural networks to automatically extract features from complex, unstructured data.

## How Machine Learning Models Learn

ML models differ based on their learning process:

| Learning Type | Description |
| :--- | :--- |
| **Supervised** | Trains on **labeled data** to learn how to make inferences and predict unknown labels on new data. |
| **Unsupervised** | Works **without labels** by finding inherent patterns and structures in data. |
| **Semi-Supervised** | Trains on a small set of labeled data and iteratively retrains itself by adding new, self-generated labels. |
| **Reinforcement** | An AI agent interacts with an environment and learns to make decisions based on feedback (rewards/punishments). |

## Key Machine Learning Techniques

The choice of technique depends on the problem, data type, available resources, and desired outcome.

| Technique | Purpose | Example |
| :--- | :--- | :--- |
| **Classification** | Predicts the class or category of a case. | Identifying a cell as benign or malignant; predicting customer churn. |
| **Regression/Estimation** | Predicts continuous numerical values. | Predicting house prices or CO2 emissions from a car. |
| **Clustering** | Groups similar cases together. | Customer segmentation in banking; finding similar patients. |
| **Association** | Finds items or events that often co-occur. | Market basket analysis (e.g., grocery items bought together). |
| **Anomaly Detection** | Discovers abnormal and unusual cases. | Credit card fraud detection. |
| **Sequence Mining** | Predicts the next event in a sequence. | Clickstream analytics on websites. |
| **Dimension Reduction** | Reduces data size, particularly the number of features. | - |
| **Recommendation Systems** | Associates people's preferences to recommend new items. | Netflix or Amazon recommendations. |

### Deeper Dive: Key Techniques

- **Classification vs. Regression**:
    - **Classification** categorizes input into predefined classes.
    - **Regression** predicts a continuous numerical value.
- **Clustering**: An unsupervised technique for grouping similar data points.

<img src="./images/0101.png" width="500">

## Applications of Machine Learning

### Healthcare: Cancer Diagnosis
- **Problem**: Determining if a human cell sample is benign or malignant based on characteristics (clump thickness, cell size uniformity, etc.).
- **ML Solution**:
    1. Obtain a dataset of thousands of cell samples.
    2. Clean the data and select a prediction algorithm.
    3. Train the model to understand patterns of benign vs. malignant cells.
    4. Use the trained model to predict new, unknown cell samples with high accuracy.

### Business & Consumer Applications
- **Recommendation Systems**: Amazon and Netflix use ML to recommend products and content.
- **Banking & Finance**: ML predicts an applicant's probability of loan default to aid approval decisions.
- **Telecommunications**: Uses demographic data to segment customers and predict **churn** (which customers will unsubscribe).

### Computer Vision
- **Problem**: Differentiating between cats and dogs in images.
- **Old Approach (Failure)**: Manually creating rules for features (eyes, ears, tail) was too rigid and failed on unseen data.
- **ML Approach**: A model **learns** distinguishing features from known examples and uses them to automatically infer the animal type.

### Other Everyday Applications
- Virtual assistants and chatbots.
- Face recognition for phone logins.
- Game-playing AI (e.g., chess).

## The Human Element

Despite the power of ML, **humans are still crucial** in the loop. For example, if an ML algorithm denies a loan, a banker needs to understand why and initiate a follow-up.

## Summary

- **Machine Learning** is an AI subset that uses algorithms to learn from data.
- **Learning Models** include Supervised, Unsupervised, Semi-supervised, and Reinforcement learning.
- **Key Techniques** include Classification, Regression, Clustering, Association, Anomaly Detection, Sequence Mining, Dimension Reduction, and Recommendation systems.
- **Applications** are vast, spanning disease prediction, consumer behavior analysis, and image recognition.

---

**Next:** []()