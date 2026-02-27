# API Development

## Serving Models to the World

An API (Application Programming Interface) is the most common way to make a trained machine learning model accessible to the outside world. Instead of sharing a `.joblib` file and expecting your client to write Python code, you provide a **web endpoint**, a URL that accepts input data and returns predictions.

This is how ML models power real products: a mobile app sends a photo to an API, the API runs a model, and returns *"This is a cat"*. A web form sends patient data, the API returns *"Low risk"*. The model lives behind the API, and the client never needs to know (or care) that it's scikit-learn, Python, or anything else.

## Why FastAPI?

There are several Python web frameworks (Flask, Django, FastAPI). For ML model serving, **FastAPI** is the modern standard because:

| Feature | FastAPI | Flask |
| :--- | :--- | :--- |
| **Speed** | Build on ASGI (async), one of the fastest Python frameworks | WSGI (synchronous), slower |
| **Data Validation** | Built-in via **Pydantic**, validates request data automatically | Manual validation or extensions |
| **Auto Documentation** | Generates interactive Swagger UI and ReDoc at `/docs` | Requires extensions |
| **Type Hint** | First-class support, your IDE autocompletes everything | Optional |
| **Learning Curve** | Minimal if you know Python type hints | Minimal |

FastAPI's killer feature for ML is **Pydantic integration:** You define a Python class describing what your model expects as input (feature names, types, value ranges), and FastAPI automatically validates every incoming request against it. If a client sends bad data, they get a clear error; your model never sees garbage input.

## Key Concepts

### Request-Response Cycle

Every API interaction follows the same pattern:

> Client sends a REQUEST (input data as JSON)  
> → Server receives it  
> → Server validates the data (Pydantic)  
> → Server loads the model and runs prediction  
> → Server sends a RESPONSE (prediction as JSON)

### HTTP Methods

For ML model serving, you primarily need two:

- **`GET`**: Retrieve information (e.g., *"Is the server alive?"*, *"What model is loaded?"*). No data sent in the body.
- **`POST`**: Send data to the server and get a result back (e.g., *"Here are 4 features, give me a prediction"*). Data sent as JSON in the request body.

### JSON: The Language of APIs

APIs communicate using **JSON (JavaScript Object Notation)**; a lightweight, human-readable data format. You already know it from saving model metadata in the previous section.

```json
// Request (client → server)
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

// Prediction (server → client)
{
  "prediction": "setosa",
  "confidence": 0.97
}
```

## What You'll Learn

1. **[FastAPI Fundamentals](./01_fastapi_fundamentals.ipynb):** How to create a web server, define endpoints, handle GET and POST requests, and explore the auto-generated documentation. No ML yet, just building the foundation.
2. **[Serving a Model with FastAPI](./02_serving_a_model_with_fastapi.ipynb):** Loading the `iris_pipeline.joblib` from the previous section and wrapping it in a prediction endpoint. This is where the model persistence section pays off.
3. **[Request Validation with Pydantic](./03_request_validation_with_pydantic.ipynb):** Defining strict input schemas, adding value constraints, handling batch predictions, and returning structured responses. This is what makes your API production-grade.

After completing this section, the `app/` subfolder will contain a working, self-contained FastAPI application that your can run with a single command.