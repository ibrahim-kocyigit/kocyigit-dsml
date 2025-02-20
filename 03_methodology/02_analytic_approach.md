# Stage 2: Analytic Approach

_"Once the business problem has been clearly stated, the data scientist can define the analytic approach to solving the problem. This stage entails expressing the problem in the context of statistical and machine-learning techniques, so the organization can identify the most suitable ones for the desired outcome. For example, if the goal is to predict a response such as “yes” or “no,” then the analytic approach could be defined as building, testing and implementing a classification model."_ - **John B. Rollins**

## Step 1: Frame the Problem Technically
Based on the business problem and objectives (from Stage 1), translate the problem into one or more potential machine learning or statistical tasks. For example, is this a classification, regression, clustering, anomaly detection, or time series forecasting problem? Consider multiple possible framings.

## Step 2: Identify Potential Models/Techniques
List potential machine learning models or statistical techniques that are appropriate for the problem type(s) identified in Step 1. Consider the solution requirements (from Stage 1) – are there constraints on model complexity, interpretability, or scalability?

## Step 3: Assess Data Suitability
Briefly consider (at a high level) whether the data *likely* to be available (we'll confirm this in later stages) will be suitable for the techniques identified. Are there likely to be enough features? Are the features likely to be predictive? This is a preliminary assessment, not a deep dive.

## Step 4: Select the Primary Approach
Choose the *primary* analytic approach that you will pursue. This doesn't mean you can't explore other approaches later, but it's important to have a primary focus. Document the rationale for your choice.

## Step 5: Document and Justify
* Detail the selected analytical methodology, alternative options evaluated, and the rationale behind your choice in the [Analytic Approach Report](./stage-report-templates/02_analytic_approach_report.md). Clearly articulate why the chosen method best addresses the business problem and aligns with project objectives.
* Store any relevant research papers, articles, or documentation supporting your methodology or alternatives in the `references` folder.