# Methodology

A successful data science project is more than just code; it's a disciplined process. This pillar outlines the structured methodology used for every project within this repository, ensuring a clear path from a business idea to a deployed, value-generating solution.

The framework adopted here is the **Foundational Methodology for Data Science** by **John B. Rollins**. It is a comprehensive 10-stage lifecycle that covers a project from inception to feedback, emphasizing clear communication, iterative development, and alignment with business goals.

Each stage is documented in its own file within this folder. These files serve as both an explanation of the process and as practical, reusable templates to be filled out for any new project.

## Adapting the Methodology to Your Project

The 10-stage lifecycle is comprehensive, but not every project will require the same level of depth in every stage. The framework is flexible and can be adapted based on the project's primary goal.

### The Data Analysis Roadmap

  * **Goal:** To understand the past and present by answering "what happened and why?"
  * **Path:** This roadmap has a heavy focus on **Stages 1-6**.
      * **Stage 7 (Modeling):** This stage may not involve a predictive machine learning model. Instead, it focuses on constructing the final analysis, creating polished visualizations, and applying statistical tests to validate insights.
      * **Stage 9 (Deployment):** The "deployment" is the delivery of the final report, presentation, or dashboard to stakeholders.

### The Data Science Roadmap

  * **Goal:** To explain relationships and make predictions, often with a focus on interpretability.
  * **Path:** This roadmap follows all 10 stages.
      * **Stage 7 (Modeling):** This involves building an actual predictive model, often an interpretable one (like Linear/Logistic Regression), to understand the key drivers behind an outcome.
      * **Stage 9 (Deployment):** The deliverable could be a detailed report on the model's findings *or* a simple prototype application (e.g., a Streamlit dashboard).

### The Machine Learning Roadmap

  * **Goal:** To engineer a robust, scalable predictive system for a production environment.
  * **Path:** This roadmap follows all 10 stages with a heavy technical focus on the later stages.
      * **Stage 7 (Modeling):** This stage focuses on maximizing predictive performance, often involving complex models and extensive hyperparameter tuning.
      * **Stage 9 (Deployment) & 10 (Feedback):** These stages are highly technical, involving the full MLOps lifecycle of packaging the model in an API, containerizing it, and monitoring its performance in production.


## The 10 Stages of the Data Science Lifecycle

This lifecycle represents a repeatable process for delivering robust and effective analytic solutions.

1.  **[Business Understanding](./01_business_understanding.md)**: Defining the problem, objectives, and requirements from a purely business perspective.

2.  **[Analytic Approach](./02_analytic_approach.md)**: Translating the business problem into a formal data science framework, including selecting the ML problem type and technical success metrics.

3.  **[Data Requirements](./03_data_requirements.md)**: Specifying the exact data needed—including fields, formats, and sources—to execute the analytic approach.

4.  **[Data Collection](./04_data_collection.md)**: Gathering the required data from all identified sources into a central location.

5.  **[Data Understanding](./05_data_understanding.md)**: Performing Exploratory Data Analysis (EDA) to assess data quality, discover initial patterns, and validate assumptions.

6.  **[Data Preparation](./06_data_preparation.md)**: Executing all data cleaning, transformation, and feature engineering tasks to create the final dataset for modeling.

7.  **[Modeling](./07_modeling.md)**: Training, tuning, and selecting the best-performing model based on the cross-validation results from the training data.

8.  **[Evaluation](./08_evaluation.md)**: Performing a final, unbiased evaluation of the champion model on the held-back test set to measure its real-world performance.

9.  **[Deployment](./09_deployment.md)**: Integrating the validated model into the production environment to deliver business value.

10. **[Feedback](./10_feedback.md)**: Monitoring the deployed model's performance and impact to guide future iterations and ensure its value is maintained over time.