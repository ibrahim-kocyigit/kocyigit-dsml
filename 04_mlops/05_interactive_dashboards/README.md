# Interactive Dashboards

## A Visual Front-End for Your Model

APIs are powerful, but they are invisible. A non-technical client can't open a terminal, type a `curl` command, and evaluate your model. What they *can* do is open a web page, move a few sliders, and see a prediction update in real time.

That's what **interactive dashboards** give you: a visual, clickable front-end that turns your ML model into something anyone can understand and interact with, without writing a single line of code on their end.

## Why Dashboards Matter for Freelancers

| **Scenario** | **API Only** | **API + Dashboard** |
| :--- | :--- | :--- |
| Client demo | You share a cURL command or Swagger link | You share a URL with sliders and charts |
| Stakeholder buy-in | Technical people get it, managers don't | Everyone can interact with the model |
| Portfolio piece | Recruiters see code | Recruiters see a live, working product |
| Prototype delivery | Clients needs a developer to integrate | Client can test the model immediately |

A dashboard is often the difference between *"Nice model"* and *"This is exactly what we needed, let's move forward."* 

## Why Streamlit?

There are several Python dashboard frameworks. For ML prototyping and freelance delivery, **Streamlit** is the standard:

| **Feature** | **Streamlit** | **Dash (Plotly)** | **Gradio** |
| :---- | :---- | :---- | :---- |
| **Learning curve** | Very low: Pure Python, no HTML/CSS/JS | Medium: Callback-based, more boilerplate | Very low, but limited to ML demos |
| **Best for** | Data apps, ML dashboards, client demos | Production dashboards, complex layouts | Quick model demos, Hugging Face spaces |
| **Interactivity** | Built-in widgets (sliders, buttons, file uploaders) | Callback system (more powerful but verbose) | Auto-generated from function signatures |
| **Deployment** | Streamlit Community Cloud (free), or any platform | Standard web hosting | Hugging Face Spaces (free) |
| **Community** | Massive, growing fast | Established, enterprise-focused | ML/AI focused |

Streamlit hits the sweet spot: **minimal code, maximum visual impact, easy deployment**. You can go from a trained model to a shareable demo in under 50 lines of Python. 

## Architecture: Dashboard ↔ API

A dashboard can interact with you model in two ways:

### Option A: Direct Model Loading (Simple)

```
Streamlit App → loads iris_pipeline.joblib → predicts directly
```

The dashboard loads the model file into memory and calls `pipeline.predict()`. Simple, self-contained, no API needed.

### Option B: API Client (Production)

```
Streamlit App → sends HTTP request to FastAPI → receives prediction
```

The dashboard is a *client* of your API. This is the production pattern: The model lives behing the API, and the dashboard is just one of many possible consumers.

**For this section, we'll use Option A** (direct loading) because it's simpler and self-contained. In a real production setup, you'd switch to Option B.

## What You'll Learn
1. **[Streamlit Fundamentals](./01_streamlit_fundamentals.ipynb):** The core Streamlit concepts: Layout, widgets, state, data display, and charts. Everything you need to build any data app.
2. **[Building an ML Dashboard](./02_building_an_ml_dashboard.ipynb):** Building a complete Iris Prediction Dashboard that loads our saved Pipeline, accepts input via sliders, display predictions with confidence bars, and visualizes the decision space.

