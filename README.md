# Kocyigit-DSML 🤖

### A structured, end-to-end learning repository for Data Science and Machine Learning - from mathematical foundations to production deployment.

This repository is the result of a year-long, self-directed curriculum consolidating curated Data Science and Machine Learning resources into a single, structured knowledge base. It is organized into **five pillars** that cover the full spectrum - from the math that powers the algorithms to deploying and monitoring models in production.

The repository contains detailed lecture notes, Jupyter Notebooks, from-scratch Python implementations of core algorithms, hands-on labs, and reusable project templates.

| Pillar | What It Covers |
| :--- | :--- |
| **[Math](./01_math/)** | High School Math, Linear Algebra, Calculus, Probability & Statistics - the mathematical foundations of DS and ML. |
| **[Toolkit](./02_toolkit/)** | Python for Data Science, NumPy, Pandas, Matplotlib, Seaborn - the hands-on libraries for data work. |
| **[Specializations](./03_specializations/)** | Statistical Modeling, Machine Learning (classical) - from inference to prediction. |
| **[MLOps](./04_mlops/)** | Model persistence, FastAPI, Docker, cloud deployment, Streamlit dashboards, monitoring, and architecture - targeted at freelance data science projects. |
| **[Methodology](./05_methodology/)** | A 10-stage project lifecycle framework based on the Foundational Methodology for Data Science by **John B. Rollins**. |

## Table of Contents

### 1. Math
1. [High School Math](./01_math/01_high_school_math/)
2. [Linear Algebra](./01_math/02_linear_algebra_for_ml_and_ds/)
3. [Calculus](./01_math/03_calculus_for_ml_and_ds/)
4. [Probability & Statistics](./01_math/04_probability_and_statistics_for_ml_and_ds/)

### 2. Toolkit
1. [Python for Data Science](./02_toolkit/01_python_for_data_science/)
2. [NumPy Fundamentals](./02_toolkit/02_numpy_fundamentals/)
3. [Pandas Fundamentals](./02_toolkit/03_pandas_fundamentals/)
4. [Matplotlib Fundamentals](./02_toolkit/04_matplotlib_fundamentals/)
5. [Seaborn Fundamentals](./02_toolkit/05_seaborn_fundamentals/)

### 3. Specializations
1. [Fitting Statistical Models to Data with Python](./03_specializations/01_fitting_statistical_models_to_data_with_python/)
2. [Machine Learning with Python](./03_specializations/02_machine_learning_with_python/)
3. Deep Learning Specialization *(Scheduled for Q3 2026)*

### 4. MLOps
1. [Model Persistence](./04_mlops/01_model_persistence/) 
2. [API Development](./04_mlops/02_api_development/) 
3. [Containerization](./04_mlops/03_containerization/) 
4. [Cloud Deployment](./04_mlops/04_cloud_deployment/) 
5. [Interactive Dashboards](./04_mlops/05_interactive_dashboards/) 
6. [Monitoring & Maintenance](./04_mlops/06_monitoring_and_maintenance/) 

### 5. Methodology
1. [Business Understanding](./05_methodology/01_business_understanding.md) 
2. [Analytic Approach](./05_methodology/02_analytic_approach.md)
3. [Data Requirements](./05_methodology/03_data_requirements.md)
4. [Data Collection](./05_methodology/04_data_collection.md)
5. [Data Understanding](./05_methodology/05_data_understanding.md)
6. [Data Preparation](./05_methodology/06_data_preparation.md)
7. [Modeling](./05_methodology/07_modeling.md)
8. [Evaluation](./05_methodology/08_evaluation.md)
9. [Deployment](./05_methodology/09_deployment.md)
10. [Feedback](./05_methodology/10_feedback.md)

## Highlights

- 📐 **From-scratch implementations** of core ML algorithms (AdaBoost, PCA, KNN, Naive Bayes, and more) in pure NumPy - theory notes paired with code.
- 🧪 **Hands-on ML labs** using scikit-learn and other industry libraries to explore real-world implementations of models including Logistic Regression, Decision Trees, SVMs, KNN, Random Forests, XGBoost, and clustering algorithms.
- 🚀 **Full MLOps pipeline**: a single Iris classification model carried from a Jupyter Notebook through a FastAPI service, Docker container, cloud deployment (Railway + GitHub Actions CI/CD), Streamlit dashboard, and monitoring setup.
- 📘 **10-stage project methodology** with reusable templates, checklists, and decision frameworks for freelance data science work.
- 📄 **Cheat sheets** included — quick-reference PDFs for key concepts for each pillar.

## Getting Started

```bash
# Clone the repository
git clone https://github.com/ibrahim-kocyigit/kocyigit-dsml.git
cd kocyigit-dsml

# Install dependencies with uv
uv sync
```

## License

This project is licensed under the [MIT License](./LICENSE).

