import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import plotly.express as px
import streamlit as st
from pathlib import Path
import joblib

# -------- Page configuration --------
st.set_page_config(
    page_title="Iris Prediction Dashboard",
    page_icon="🌸",
    layout="wide",
)

# --------- Constants and model loading --------
MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "01_model_persistence"
    / "models"
    / "iris_pipeline.joblib"
)
TARGET_NAMES = ["setosa", "versicolor", "virginica"]


@st.cache_resource
def load_model():
    """Load the Iris Pipeline once and cache it."""
    return joblib.load(MODEL_PATH)


# -------- Sidebar for input controls --------
st.sidebar.header("🌸 Input Features")
st.sidebar.markdown("Adjust the sliders to change the flower measurements.")

sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.1, 0.1)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.5, 0.1)
petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.4, 0.1)
petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2, 0.1)


# -------- Model prediction --------
pipeline = load_model()

# Build the feature array
features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Make prediction
prediction_id = int(pipeline.predict(features)[0])
probabilities = pipeline.predict_proba(features)[0]
prediction_name = TARGET_NAMES[prediction_id]
confidence = probabilities[prediction_id]

# --------- Display results --------
st.title("🌸 Iris Prediction Dashboard")
st.markdown(
    "Predict the species of an Iris flower based on sepal and petal measurements."
)
st.divider()

# --- Prediction Result ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Predicted Species", value=prediction_name.capitalize())
with col2:
    st.metric(label="Confidence", value=f"{confidence:.1%}")
with col3:
    st.metric(label="Class ID", value=str(prediction_id))

st.divider()

st.subheader("Prediction Probabilities")

prob_df = pd.DataFrame(
    {
        "Species": [name.capitalize() for name in TARGET_NAMES],
        "Probability": probabilities,
    }
)

fig = px.bar(
    prob_df,
    x="Species",
    y="Probability",
    color="Species",
    color_discrete_map={
        "Setosa": "lightblue",
        "Versicolor": "lightgreen",
        "Virginica": "salmon    ",
    },
    range_y=[0, 1],
)
fig.update_layout(showlegend=False, yaxis_title="Probability", xaxis_title="")
st.plotly_chart(fig, use_container_width=True)


# --------- Feature Context ---------
@st.cache_data
def load_iris_data():
    """Load the Iris dataset as a DataFrame (cached)."""
    data = load_iris()
    df = pd.DataFrame(data=data.data, columns=data.feature_names)
    df["species"] = [data.target_names[t] for t in data.target]
    return df


st.divider()
st.subheader("Feature Context")

iris_df = load_iris_data()

# Scatter: petal length vs petal width, colored by species
fig2 = px.scatter(
    iris_df,
    x="petal length (cm)",
    y="petal width (cm)",
    color="species",
    opacity=0.6,
    title="Petal Length vs Petal Width",
)

# Add the current input as a large star marker
fig2.add_scatter(
    x=[petal_length],
    y=[petal_width],
    mode="markers",
    marker=dict(size=18, symbol="star", color="red", line=dict(width=2, color="black")),
    name="Your Input",
)
st.plotly_chart(fig2, use_container_width=True)

# --------- Prediction History ---------
# Initialize history
if "history" not in st.session_state:
    st.session_state.history = []

# Add current prediction
if st.sidebar.button("💾 Save Prediction"):
    st.session_state.history.append(
        {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
            "predicted_species": prediction_name,
            "confidence": f"{confidence:.2%}",
        }
    )

# Display history
if st.session_state.history:
    st.divider()
    st.subheader("Prediction History")
    history_df = pd.DataFrame(st.session_state.history)
    st.dataframe(history_df)
