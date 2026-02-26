# Saving and Loading Models

## 1. Basic Workflow

The standard workflow for model persistence involves three steps:

1. **Train** your model (or pipeline)
2. **Save** the trained model to disk
3. **Load** the model when needed and use it for predictions

## 2. Saving Models with Joblib

**Joblib** is the recommended method for scikit-learn models and pipelines.


```python
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Train a simple model
X, y = load_iris(return_X_y=True)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
joblib.dump(model, 'models/random_forest_model.joblib')

# Load the model
loaded_model = joblib.load('models/random_forest_model.joblib')

# Make predictions
predictions = loaded_model.predict(X[:5])
print(predictions)
```
