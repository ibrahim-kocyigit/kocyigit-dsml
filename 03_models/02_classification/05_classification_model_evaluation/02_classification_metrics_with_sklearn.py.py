import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn import metrics

# =======================================
# 1. INTRODUCTION: WHY ACCURACY ISN'T ENOUGH
# =======================================
# - While accuracy (the percentage of correct predictions) is intuitive, it can be
#   very misleading, especially on "imbalanced" datasets.
#
# - The Accuracy Paradox: Imagine a dataset where 99% of samples are "Class A"
#   and 1% are "Class B". A lazy model that *always* predicts "Class A" will be
#   99% accurate, but it's completely useless because it fails to identify any
#   instances of the rare (and often more important) Class B.
#
# - The Solution: We need more nuanced metrics that give a fuller picture of a
#   model's performance, such as Precision, Recall, and the Confusion Matrix.


# =======================================
# 2. SETTING UP A PREDICTION SCENARIO
# =======================================
# - To make these metrics interesting, we'll create a slightly imbalanced dataset.

print("--- Step 1: Creating & Splitting Imbalanced Data ---")
# Create data where 90% is class 0 and 10% is class 1.
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=5,
    n_redundant=0,
    n_classes=2,
    weights=[0.9, 0.1],
    random_state=42,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Train a simple model and get predictions
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[
    :, 1
]  # Probabilities for the positive class (1)

print("Model trained and predictions generated.")
print("-" * 30)


# =======================================
# 3. THE CONFUSION MATRIX
# =======================================
# - The foundation of most classification metrics. It's a table that breaks down
#   predictions into four categories.
#   - True Positives (TP): Correctly predicted positive.
#   - True Negatives (TN): Correctly predicted negative.
#   - False Positives (FP): Incorrectly predicted positive (Type I Error).
#   - False Negatives (FN): Incorrectly predicted negative (Type II Error).

print("--- The Confusion Matrix ---")
conf_matrix = metrics.confusion_matrix(y_test, y_pred)

# Visualize the confusion matrix with a heatmap for clarity
plt.figure(figsize=(6, 5))
sns.heatmap(
    conf_matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Predicted Negative (0)", "Predicted Positive (1)"],
    yticklabels=["Actual Negative (0)", "Actual Positive (1)"],
)
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.title("Confusion Matrix")
print("Generated a plot for the Confusion Matrix.")
print("-" * 30)


# =======================================
# 4. CORE CLASSIFICATION METRICS
# =======================================
print("--- Core Classification Metrics ---")
accuracy = metrics.accuracy_score(y_test, y_pred)
precision = metrics.precision_score(y_test, y_pred)
recall = metrics.recall_score(y_test, y_pred)
f1 = metrics.f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.3f}")
print("  - Q: Overall, what fraction of predictions were correct?")

print(f"Precision: {precision:.3f}")
print(
    "  - Q: Of all the times the model predicted POSITIVE, what fraction was actually correct?"
)
print(
    "  - High precision is important when False Positives are costly (e.g., spam detection)."
)

print(f"Recall (Sensitivity): {recall:.3f}")
print(
    "  - Q: Of all the actual POSITIVE cases, what fraction did the model correctly identify?"
)
print(
    "  - High recall is important when False Negatives are costly (e.g., medical diagnosis)."
)

print(f"F1-Score: {f1:.3f}")
print(
    "  - The harmonic mean of Precision and Recall. A good single score that balances both."
)
print("-" * 30)


# =======================================
# 5. THE `classification_report`
# =======================================
# - A convenient function that calculates and displays all the main metrics at once.
print("--- Classification Report ---")
report = metrics.classification_report(y_test, y_pred)
print(report)
print("-" * 30)


# =======================================
# 6. ROC CURVE AND AUC SCORE
# =======================================
# - ROC Curve: A plot of the True Positive Rate (Recall) vs. the False Positive Rate
#   at various probability thresholds. A good model's curve "hugs" the top-left corner.
# - AUC (Area Under the Curve): A single number summary of the ROC curve's performance.
#   - AUC = 1.0: Perfect classifier.
#   - AUC = 0.5: Useless classifier (same as random guessing).

print("--- ROC Curve and AUC ---")
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_proba)
auc_score = metrics.auc(fpr, tpr)
print(f"AUC Score: {auc_score:.3f}")

# Plot the ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color="blue", lw=2, label=f"ROC curve (AUC = {auc_score:.3f})")
plt.plot([0, 1], [0, 1], color="red", lw=2, linestyle="--", label="Random Guess")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate (Recall)")
plt.title("Receiver Operating Characteristic (ROC) Curve")
plt.legend(loc="lower right")
print("Generated the ROC Curve plot.")


# --- Display all plots ---
plt.show()

# --- End of File ---
