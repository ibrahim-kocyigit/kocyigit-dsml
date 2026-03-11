import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.sidebar.title("Controls")
name = st.sidebar.text_input("Your name")
st.sidebar.slider("Choose a value", 0, 100, 50)


st.title("Hello, Streamlit!")
st.divider()
st.write("This is my first Streamlit app.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Accuracy", "0.97")
with col2:
    st.metric("Precision", "0.95")
with col3:
    st.metric("Recall", "0.96")

# Slider: returns a number
age = st.slider("Age", min_value=0, max_value=120, value=25, step=1)

weight = st.number_input(
    "Weight (kg)", min_value=0.0, max_value=300.0, value=70.0, step=0.1
)

color = st.selectbox("Favorite color", ["Red", "Blue", "Green"])

features = st.multiselect(
    "Select features", ["sepal_length", "sepal_width", "petal_length", "petal_width"]
)

name = st.text_input("Your name", value="Ibrahim")

show_details = st.checkbox("Show details")

if st.button("Predict"):
    st.write("Making a prediction...")

uploaded_file = st.file_uploader("Upload a CSV", type=["csv"])

threshold = st.slider("Threshold", 0.0, 1.0, 0.5)
st.write(f"Current threshold: {threshold:.2f}")


df = pd.DataFrame(
    {"Species": ["setosa", "versicolor", "virginica"], "Count": [50, 50, 50]}
)

# Interactive sortable/filterable table
st.dataframe(df)

# Static table (no interactivity)
st.table(df)

# Metric with delta indicator
st.metric(label="Accuracy", value="97.3%", delta="+2.1%")

# JSON display
st.json({"prediction": "setosa", "confidence": 0.97})

st.success("Model loaded successfully!")
st.warning("Low confidence prediction.")
st.error("Failed to load model.")
st.info("Tip: Adjust the sliders to see different predictions.")


data = np.random.randn(100, 3)
st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)


fig, ax = plt.subplots()
ax.hist(np.random.randn(200), bins=20)
ax.set_title("Distribution")
st.pyplot(fig)

df_2 = px.data.iris()
fig = px.scatter(df_2, x="sepal_length", y="petal_length", color="species")
st.plotly_chart(fig, use_container_width=True)


# Initialize a counter
if "count" not in st.session_state:
    st.session_state.count = 0

# Increment on button click
if st.button("Increment"):
    st.session_state.count += 1

st.write(f"Current count: {st.session_state.count}")
