# Model Persistance

## From Notebook to Artifact

Model persistence is the act of **saving a trained machine learning model to disk** so it can be reused later without retraining from scratch. It is the essential first step that bridges the gap between a Jupyter notebook experiment and a production-ready system.

This section is the foundation for everything that follows in the MLOps pillar. Without a saved model file, there is nothing to serve via an API, nothing to containerize, and nothing to deploy.

## Why Model Persistence Matters

Training a machine learning model is expensive. It consumes time, compute resources, and requires access to the original dataset. Once you've found the best model through experimentation and validation, you need a way to **freeze** it and reuse at will.

### The Core Concept: Serialization

At its heart, model persistence is about **serialization**: converting a live Python object (your trained model, with all its learned parameters) into a stream of bytes that can be written to a file on disk.

The reverse process, **deserialization**, reads those bytes back and reconstructs the original Python object in memory, ready to make predictions.

```
Python Object (fitted model) → Serialization → Bytes on Disk (.joblib / .pkl)
Bytes on Disk → Deserialization → Python Object (ready to predict)
```

## Key Concerns

When choosing how to persist a model, there are several important factors to consider:

1. **Reproducibility:** The loaded model must produce the **exact same predictions** as the original. This means everything the model needs to predict (learned weights, hyperparameters, and any preprocessing steps) must be saved together.
2. **Portability:** Can someone else or a different machine (like a cloud server) load and use this file? This depends on the format and the environment.
3. **Security:** Formats like `pickle` can execute arbitrary code during deserialization. You should **never load a pickle file from an untrusted source**. This is a real-world security concern, not just a theoretical one.
4. **Version Compatibility:** A model saved with `scikit-learn==1.6` may not load correctly with `scikit-learn==1.7`. Tracking the library versions used during training is essential.
5. **The Pipeline Rule:** You should almost always save the **entire scikit-learn Pipeline** (preprocessing + model), not just the bare estimator. If you save only the model but forget the scaler, your predictions in production will be garbage because the input data won't be transformed correctly.

## The Format Landscape

| Format | Library | Best For | Cross-Language |
| :--- | :--- | :--- | :---: |
| **Joblib** | `joblib` | scikit-learn models (optimized for NumPy arrays) | ❌ |
| **Pickle** | `pickle` (built-in) | General Python objects | ❌ |
| **ONNX** | `onnx`, `skl2onnx` | Portable, cross-platform deployment | ✅ |

For most freelance data science work, **joblib** will be your go-to tool. ONNX becomes relevant when a client's production stack is not Python-based.

## What You'll Learn
1. **[Pickle and Joblib](./01_pickle_and_joblib.ipynb):** The standard Python tools for saving and loading models. You'll learn the difference between them, when to use which, and how to persist entire Pipelines, not just bare models.
2. **[ONNX Basics](./02_onnx_basics.ipynb):** An introduction to the Open Neural Network Exchange format for cross-platform model deployment. This is awareness-level knowledge for when a client needs a model outside the Python ecosystem.