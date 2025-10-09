# Machine Learning Workflow and Vocabulary

## Learning Goals

- Understand the basic workflow of a machine learning project.
- Review essential machine learning vocabulary.
- Prepare for topics like exploratory data analysis, data cleansing, and statistical inference.

## Prerequisites

- Familiarity with Python libraries: NumPy, Pandas, Jupyter Notebooks
- Basic statistics: probability, moments, Bayes' rule
- Linear algebra foundation is highly recommended

## Common Python Libraries Used

- **NumPy:** Numerical analysis
- **Pandas:** Data manipulation (DataFrames)
- **Matplotlib & Seaborn:** Visualization
- **Scikit-Learn:** Machine learning algorithms
- **TensorFlow & Keras:** Deep learning

## Typical Machine Learning Workflow

1. **Problem Statement:**  
   - Define the problem you want to solve (e.g., image classification of dog breeds).

2. **Data Collection:**  
   - Gather the data needed to solve the problem (e.g., many labeled images from different conditions).

3. **Data Exploration & Preprocessing:**  
   - Clean and explore the data (e.g., check distributions, visualize data, convert images to arrays).
   - Prepare data for modeling (handle missing values, normalization, encoding, etc.).

4. **Modeling:**  
   - Build and train a model to solve the problem.
   - Start with a baseline model and iterate.

5. **Validation:**  
   - Evaluate model performance using a holdout (validation/test) set.
   - Check how well the model generalizes to unseen data.

6. **Decision-Making & Deployment:**  
   - Communicate results to stakeholders.
   - Deploy the model to production if performance is satisfactory.

## Key Machine Learning Vocabulary

- **Target Variable (Target):**  
  The value you are trying to predict (e.g., species in the iris dataset).

- **Features (Explanatory Variables):**  
  The input variables used to predict the target (e.g., sepal length, sepal width, petal length, petal width).

- **Example / Observation:**  
  A single row in your dataset; one instance of data (e.g., one flower's measurements).

- **Label:**  
  The value of the target variable for a specific example (e.g., "versicolor" for one flower).

---

**Next:** [Retrieving Data from CSV and JSON Files]()