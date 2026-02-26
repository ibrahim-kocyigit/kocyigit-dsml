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


## 3. Saving Models with Pickle

**Pickle** works similarly but is less efficient for large models.

```python
import pickle

# Save the model
with open('models/random_forest_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Load the model
with open('models/random_forest_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Make predictions
predictions = loaded_model.predict(X[:5])
print(predictions)
```

## 4. Saving Pipelines

Pipelines bundle preprocessing and modeling together, ensuring consistency between training and inference. **This is the recommended approach for production systems.**

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

# Create a pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2)),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train the pipeline
pipeline.fit(X, y)

# Save the entire pipeline
joblib.dump(pipeline, 'models/pipeline_model.joblib')

# Load the pipeline
loaded_pipeline = joblib.load('models/pipeline_model.joblib')

# The pipeline handles all preprocessing automatically
predictions = loaded_pipeline.predict(X[:5])
print(predictions)
```

> ❗️ **Key Advantage**: All preprocessing steps (scaling, PCA) are applied automatically when you call `predict()`. No manual preprocessing needed!