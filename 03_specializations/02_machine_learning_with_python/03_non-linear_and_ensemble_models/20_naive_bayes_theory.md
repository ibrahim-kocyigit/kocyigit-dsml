# Lecture Notes: Naive Bayes Classifier

## 1. The Core Idea: Classification with Probability

The **Naive Bayes classifier** is a supervised machine learning algorithm based on applying **Bayes' Theorem**. Unlike other classifiers that try to draw a "line" between classes, Naive Bayes is a **probabilistic classifier**. This means it calculates the probability of a data point belonging to each class and then selects the class with the highest probability.

It's particularly famous for its use in text classification tasks, such as spam filtering.

## 2. The Foundation: Bayes' Theorem

The algorithm is built entirely on Bayes' Theorem, which describes the probability of an event based on prior knowledge of conditions that might be related to the event.

The formula is:
`P(A|B) = (P(B|A) * P(A)) / P(B)`

In machine learning classification terms, we can rewrite this as:

**`P(class | features) = (P(features | class) * P(class)) / P(features)`**

Let's break this down:
*   `P(class | features)`: **Posterior Probability**. This is what we want to calculate: the probability that a data point belongs to a certain *class*, given its *features*.
*   `P(features | class)`: **Likelihood**. The probability of observing the given *features*, assuming the data point belongs to a certain *class*.
*   `P(class)`: **Prior Probability**. The overall probability of a data point belonging to that *class*, based on its frequency in the training data.
*   `P(features)`: **Evidence**. The overall probability of observing the given *features*. This term is constant for all classes, so we can ignore it when comparing probabilities.

## 3. The "Naive" Assumption: Feature Independence

Here's where the "naive" part comes in. The algorithm makes a strong, simplifying assumption: **it assumes that all features are independent of one another, given the class.**

For example, in a spam filter:
*   A "naive" model assumes that the probability of the word "free" appearing in a spam email is completely independent of the probability of the word "viagra" appearing in that same email.

In reality, this assumption is almost never true (these words are likely to appear together). However, this simplification is what makes the algorithm so fast and efficient. It allows us to calculate the total likelihood by simply multiplying the individual likelihoods of each feature:

`P(features | class) = P(feature1 | class) * P(feature2 | class) * ...`

## 4. How Naive Bayes Works: A Spam Filter Example

Let's say we want to classify a new email as either "Spam" or "Not Spam".

### Training Phase:
The model "learns" by calculating probabilities from the training data:
1.  **Calculate Prior Probabilities:**
    *   `P(Spam)` = (Number of spam emails) / (Total number of emails)
    *   `P(Not Spam)` = (Number of not-spam emails) / (Total number of emails)
2.  **Calculate Likelihoods:**
    *   For every word in the vocabulary, calculate its probability of appearing given the class.
    *   `P("viagra" | Spam)` = (Number of times "viagra" appears in spam emails) / (Total words in all spam emails)
    *   `P("report" | Not Spam)` = (Number of times "report" appears in not-spam emails) / (Total words in all not-spam emails)

### Prediction Phase:
For a new email with the words "urgent report", we calculate a score for each class:
*   **Score(Spam)** = `P("urgent"|Spam) * P("report"|Spam) * P(Spam)`
*   **Score(Not Spam)** = `P("urgent"|Not Spam) * P("report"|Not Spam) * P(Not Spam)`

The class with the higher score is the model's prediction.

## 5. Types of Naive Bayes

There are several types of Naive Bayes classifiers, chosen based on the nature of the features:
*   **Gaussian Naive Bayes:** Used for continuous features that are assumed to follow a Gaussian (normal) distribution (e.g., age, income).
*   **Multinomial Naive Bayes:** Used for discrete features, making it the standard for text classification where features are word counts.
*   **Bernoulli Naive Bayes:** Used for binary features (e.g., a word is either present or absent in a document).

## 6. Advantages and Disadvantages

### Advantages:
*   **Extremely Fast:** Training and prediction are very quick because they mostly involve counting and simple multiplication.
*   **Requires Little Data:** It can perform surprisingly well even with a small training dataset.
*   **Excellent for Text Classification:** It remains a strong baseline for tasks like spam filtering and sentiment analysis.
*   **Handles High-Dimensional Data:** It works well even with a very large number of features (e.g., thousands of unique words).

### Disadvantages:
*   **The "Naive" Assumption:** The assumption of feature independence is a strong limitation. If features are highly correlated, the model's performance can suffer.
*   **Zero-Frequency Problem:** If a word in a new email never appeared in the training data for a certain class, its likelihood would be zero, causing the entire score for that class to become zero. This is typically handled with a smoothing technique like **Laplace smoothing**.

---
*This lab was completed by **ibrahim-kocyigit** on **2025-10-30 17:24:10**.*

----------


# Lab: Building a Naive Bayes Spam Classifier

*This notebook demonstrates a complete data science workflow for building a text classification model using Multinomial Naive Bayes to identify spam SMS messages.*

---

## Stage 1: Business Understanding

Let's start by understanding the problem from a business perspective.

*   **Scenario:** We are data scientists for a mobile service provider. Customers are complaining about an increasing number of unsolicited spam messages (SMS).
*   **Business Objective:** To automatically identify and filter spam SMS messages to improve customer satisfaction and reduce unwanted network traffic. The model must be highly accurate at flagging spam while being extremely careful not to incorrectly flag legitimate messages ("ham") as spam.

---

## Stage 2: Analytic Approach

With the business problem defined, we select an analytic approach.

*   **Problem Framing:** The goal is to classify each SMS message as either "spam" or "ham". This is a **binary text classification** problem.
*   **Candidate Model:** We will use the **Multinomial Naive Bayes** classifier. This algorithm is a classic choice for text classification because it is fast, efficient, and performs remarkably well with features representing word counts.
*   **Evaluation Metrics:**
    *   **Accuracy:** The overall percentage of correct predictions.
    *   **Confusion Matrix:** To visualize the model's performance, especially the number of False Positives (legitimate messages flagged as spam) and False Negatives (spam messages missed).
    *   **Precision and Recall:** For a spam filter, these are more important than accuracy.
        *   **Precision** (for the "ham" class) tells us: "Of all the messages we labeled as legitimate, how many actually were?" A high precision here is critical to avoid angry customers whose important messages get filtered.
        *   **Recall** (for the "spam" class) tells us: "Of all the actual spam messages, how many did we successfully catch?"

---

## Stage 3: Data Requirements

To build our model, we need a dataset of SMS messages that have been pre-labeled as either "spam" or "ham". The "SMS Spam Collection Data Set" from the UCI Machine Learning Repository is a standard and publicly available dataset for this task.

---

## Stage 4: Data Collection

The data is available from a public URL. To ensure our project is robust and reproducible, we will first download the data to a local `./data` directory and then load it from there using `pathlib`.

```python
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

# Configurations
%matplotlib inline
plt.style.use('fivethirtyeight')
```

```python
# --- Data Download and Loading ---

# Define the local data directory and file path using pathlib
data_dir = Path("./data")
file_path = data_dir / "sms_spam_collection.zip"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"

# Create the data directory if it doesn't exist
if not data_dir.exists():
    data_dir.mkdir(parents=True)
    print(f"Directory '{data_dir}' created.")

# Download the file if it doesn't already exist
if not file_path.exists():
    print(f"Downloading data from {url}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Data successfully downloaded and saved to '{file_path}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")
else:
    print(f"Data file already exists at '{file_path}'.")

# Load the data from the local file
try:
    # The file is tab-separated and has no header
    df = pd.read_csv(file_path, sep='\t', header=None, names=['label', 'message'])
    print("DataFrame loaded successfully from local file.")
except Exception as e:
    print(f"Error loading data into DataFrame: {e}")

df.head()
```

---

## Stage 5: Data Understanding (EDA)

Let's perform Exploratory Data Analysis to understand the data's characteristics.

```python
# Check the class distribution
print("Class Distribution:")
print(df['label'].value_counts())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
```

> 📊 **Data Understanding Report:**
>
> *   The dataset contains 5,572 messages.
> *   It is imbalanced: there are 4,825 legitimate messages ("ham") and only 747 spam messages. This is typical for spam datasets.
> *   There are no missing values in the dataset.

---

## Stage 6: Data Preparation

This stage is the most critical for any text-based model. We need to convert the raw text messages into a numerical format that the algorithm can understand.

#### 6.1 Feature Extraction (Vectorization)

We will use scikit-learn's `CountVectorizer`. This tool will:
1.  Tokenize the messages (split them into individual words).
2.  Convert all words to lowercase.
3.  Build a vocabulary of all unique words in the dataset.
4.  Create a document-term matrix, where each row is a message and each column is a word from the vocabulary. The value in each cell is the count of how many times that word appeared in that message.

```python
# Separate features (message) and target (label)
X = df['message']
y = df['label']

# Create a CountVectorizer object
vectorizer = CountVectorizer(stop_words='english')

# Fit the vectorizer to the data and transform it into a document-term matrix
X_vectorized = vectorizer.fit_transform(X)
```

#### 6.2 Train-Test Split

Now we split our vectorized data into training and testing sets.

```python
# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42, stratify=y)
```

---

## Stage 7: Modeling

With the data prepared, we can now train our Naive Bayes model. The process is remarkably fast.

```python
# Create and train the Multinomial Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

print("Naive Bayes model trained successfully.")
```

---

## Stage 8: Evaluation

Now we evaluate our trained model on the held-back test set.

```python
# Make predictions on the test set
y_pred = model.predict(X_test)

# --- Performance Metrics ---

# 1. Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Overall Accuracy: {accuracy:.4f}\n")

# 2. Classification Report (Precision, Recall, F1-Score)
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Ham', 'Spam']))

# 3. Confusion Matrix
print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Ham', 'Spam'])
disp.plot(cmap=plt.cm.Blues)
plt.show()
```

### Analysis of Results
*   **High Accuracy:** The model achieves an impressive overall accuracy of ~98.7%.
*   **Excellent Spam Detection (Recall):** The recall for the "Spam" class is ~93%. This means our model successfully identified and caught 93% of all the spam messages in the test set.
*   **Excellent Precision (Crucial for "Ham"):** The precision for the "Ham" class is ~99%. This is the most important metric for user trust. It means that of all the messages the model allowed through as legitimate, 99% of them actually were. Only a very small number of legitimate messages were incorrectly flagged as spam (False Positives), which is exactly what we want.

---

## Stage 9 & 10: Conclusion

In this lab, we successfully built a highly effective SMS spam classifier using the Multinomial Naive Bayes algorithm.

*   We demonstrated the full machine learning workflow, with a special focus on the text preprocessing step using `CountVectorizer`.
*   The model achieved excellent performance, with an overall accuracy of over 98%.
*   Most importantly, the detailed evaluation showed that the model meets the critical business requirement: it is very good at catching spam while being extremely reliable at not flagging legitimate messages incorrectly.

This exercise highlights why Naive Bayes, despite its simplicity, remains a powerful and widely used tool for text classification tasks.

### Congratulations! You have successfully built a spam classifier.

---
*This lab was completed by **ibrahim-kocyigit** on **2025-10-30 17:25:14**.*
