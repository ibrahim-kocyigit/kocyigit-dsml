# Candidate Models Guide

### Table of Contents
1. [Simple Linear Regression](#simple-linear-regression)
2. [Multiple Linear Regression](#multiple-linear-regression)
3. [Polynomial Regression](#polynomial-regression)
4. [Logistic Regression](#logistic-regression)
5. [Softmax Regression (Multi-Class)](#softmax-regression-multi-class)
6. [Decision Trees (Classification)](#decision-trees-classification)
7. [Regression Trees](#regression-trees)
8. [Support Vector Machines (SVM)](#support-vector-machines-svm)
9. [K-Nearest Neighbors (KNN)](#k-nearest-neighbors-knn)
10. [Naive Bayes](#naive-bayes)
11. [Random Forest](#random-forest)
12. [AdaBoost / Gradient Boosting (XGBoost)](#adaboost--gradient-boosting-xgboost)
13. [K-Means Clustering](#k-means-clustering)
14. [DBSCAN](#dbscan)
15. [HDBSCAN](#hdbscan)
16. [PCA](#pca)
17. [t-SNE](#t-sne)
18. [UMAP](#umap)


> 💡 Click on the model's name for a link to the detailed theory and implementation guide for that specific model.

### [Simple Linear Regression](./02_linear_and_logistic_regression/02_simple_linear_regression_theory.md)
A good candidate for establishing a **quick baseline** on regression problems with a **single feature**. Extremely fast, computationally cheap, and highly interpretable — ideal when you need to explain the relationship between one predictor and a continuous target to non-technical stakeholders. 

**Assumptions:**
1. **Linear relationship** between the predictor and the target *(Can still be used with feature transformations like `log(x)`, `sqrt(x)`, or by switching to Polynomial Regression)*
2. **Independence of residuals** — errors are not correlated with each other *(**Cannot** remain a candidate model if the data is sequential/time-series — use ARIMA instead)*
3. **Homoscedasticity** — constant variance of residuals across all values of `x` *(Can still be used with target variable transformations like `log(y)` or `sqrt(y)` to stabilize variance)*
4. **Normality of residuals** *(Can still be used with large datasets thanks to the Central Limit Theorem, or by removing outliers)* 
5. **Not too many outliers** — OLS minimizes squared errors, so outliers have outsized influence *(Can still be used with outlier removal, or by switching to a robust regression model)*

### [Multiple Linear Regression](./02_linear_and_logistic_regression/05_multiple_linear_regression_theory.md)
A good candidate to use as a **baseline regression model** when you have **multiple features** and need a fast, interpretable starting point. It establishes a reliable first threshold that more complex models should beat. Excellent when stakeholders need to understand **how much each feature independently contributes** to the prediction (coefficients are directly interpretable).

**Assumptions:**
1. **Linear relationship** between features and target *(Can still be used with feature transformations like `log`, `sqrt`, or polynomial terms like $x^2$)* 
2. **Independence of residuals** *(**Cannot** remain a candidate model if the data is sequential/time-series — use ARIMA, SARIMA, or RNNs instead)*
3. **Homoscedasticity** *(Can still be used with target transformations, Weighted Least Squares (WLS), or Robust Standard Errors)* 
4. **Normality of residuals** *(Can still be used with large datasets (thanks to Central Limit Theorem), outlier removal, or transformations)*
5. **No multicollinearity** — features should not be highly correlated with each other *(Can still be used by removing one of the correlated features, combining them, or using Ridge Regression / regularization)*


### [Polynomial Regression](../02_machine_learning_with_python/03_non-linear_and_ensemble_models/02_polynomial_regression_theory.md) 
A good candidate for regression problems where the scatter plot reveals a **clear curved (non-linear) relationship** but you still want to stay within the linear-regression family for interpretability and simplicity. Ideal as a **step up from linear regression** before jumping to tree-based or ensemble models.

**Assumptions:**
1. **Linearity in the parameters** (coefficients) — not in the original features *(This is inherently satisfied by the polynomial feature transformation trick)*
2. **Independence of residuals** *(**Cannot** remain a candidate model if the data is sequential/time-series)*
3. **Homoscedasticity** *(Can still be used with target variable transformations)*
4. **No multicollinearity** — polynomial terms ($x$, $x^2$, $x^3$) are naturally correlated *(Can still be used with centering features before generating polynomial terms (i.e., using `x - mean(x)`) to reduce correlation, or with regularization (Ridge/Lasso) to stabilize coefficients)*
5. **Correct degree selection** — wrong degree leads to underfitting or overfitting *(Can still be used with cross-validation to select the optimal polynomial degree)*


### [Logistic Regression](../02_machine_learning_with_python/02_linear_and_logistic_regression/08_logistic_regression_theory.md)
A good candidate to use as the **baseline model for binary classification** problems. Fast, computationally cheap, and highly interpretable — the coefficients directly reveal the direction and strength of each feature's influence on the predicted class. Ideal when you need a **reliable first threshold** before trying more complex classifiers, or when **model explainability** is a requirement (e.g., healthcare, finance). *(For 3+ classes, see Softmax Regression below, which is the multinomial generalization.)*

**Assumptions:**
1. **Binary outcome** — target variable has exactly 2 classes *(**Cannot** remain a candidate model if more than 2 classes — use Softmax/Multinomial Logistic Regression, Decision Trees, etc.)*
2. **Independence of observations** *(**Cannot** remain a candidate model if the data is time-series or clustered — use LSTMs, mixed-effects models, or GEE)*
3. **Linearity of log-odds** — linear relationship between features and the log-odds of the outcome *(Can still be used with feature engineering: polynomial features, interaction terms, or log/sqrt transformations)* 
4. **No high multicollinearity** *(Can still be used with removing correlated features, combining them, or using L1/L2 regularization)* 
5. **No strong outliers in feature space** — unlike linear regression, logistic regression is more robust to outliers in `y` (since `y` is binary), but extreme outliers in `X` can still distort the decision boundary *(Can still be used with outlier removal or L1/L2 regularization)*

### [Softmax Regression (Multi-Class)](../02_machine_learning_with_python/03_non-linear_and_ensemble_models/05_multi-class_classification_theory.md)
A good candidate for multi-class classification problems where you need a **fast, interpretable baseline** — the natural extension of Logistic Regression to 3+ classes. Ideal when the decision boundary between classes is approximately linear and you want a probabilistic output (predicted probability per class).

**Assumptions:**
1. **Mutually exclusive classes** — each sample belongs to exactly one class *(**Cannot** remain a candidate model if samples can belong to multiple classes — use Multi-Label Classification instead)* 
2. **Independence of observations** *(**Cannot** remain a candidate model if data is sequential/time-series)* 
3. **Linearity of log-odds ratios** — the log-odds ratio between any two classes ($\log \frac{P(\text{class}_j)}{P(\text{class}_k)}$) is a linear function of the features (inherited from Logistic Regression) *(Can still be used with polynomial features, interaction terms, or non-linear transformations)* 
4. **No high multicollinearity** *(Can still be used with regularization or feature removal)*

### [Decision Trees (Classification)](./03_non-linear_and_ensemble_models/08_decision_trees_theory.md)
A good candidate for classification problems where **interpretability is the top priority** — the model is a human-readable flowchart of if/else rules that can be shown directly to stakeholders. Excellent when the dataset contains a **mix of numerical and categorical features** with no need for preprocessing (scaling, encoding). Also a great choice for **exploratory analysis** to understand which features matter most (features near the root are most informative).

**Assumptions:**
1. **No strong assumptions** about data distribution, linearity, or feature scaling — non-parametric model ✅
2. **Sufficient data at each split** — needs enough samples to make meaningful splits *(Can still be used if/with pruning, setting `min_samples_split` / `min_samples_leaf` hyperparameters)*
3. **Features with many thresholds may be preferred** (biased splits) *(Can still be used if/with using Gini or Entropy criteria carefully and controlling `max_features`)*
4. **Assumes axis-aligned decision boundaries** — standard decision trees split on one feature at a time, creating rectangular partitions *(Can still be used with feature engineering to create combined features, or consider Oblique Decision Trees if diagonal boundaries are needed)*

⚠�� **Main risk:** High variance (overfitting) *(Can still be used if/with pruning, depth limits, or switching to ensemble methods like Random Forest)*

### [Regression Trees](./03_non-linear_and_ensemble_models/11_regression_trees_theory.md)
A good candidate for regression problems where the relationship between features and the target is **highly non-linear or involves complex interactions**, and you still want a **white-box, interpretable model**. Ideal when the data has a mix of feature types and you want to avoid preprocessing. Also useful as the **building block** for understanding ensemble methods (Random Forest, Gradient Boosting).

**Assumptions:**
1. **No strong assumptions** about data distribution, linearity, or feature scaling — non-parametric model ✅
2. **Sufficient data at each split** *(Can still be used if/with pre-pruning constraints: `max_depth`, `min_samples_split`, `min_samples_leaf`)*
3. **Target must be within the observed training range** — trees cannot extrapolate beyond seen values *(**Cannot** remain a candidate model if predictions outside the training range are needed — use a parametric model like Linear Regression instead)*

⚠️ **Main risk:** High variance *(Can still be used if/with cost-complexity pruning or ensemble methods)*

### [Support Vector Machines (SVM)](./03_non-linear_and_ensemble_models/14_support_vector_machines_theory.md)
A good candidate for **binary classification** on **small-to-medium sized datasets** where you need **high accuracy** and the decision boundary may be **non-linear** (via the Kernel Trick). Particularly strong when the number of features is **large relative to the number of samples** (e.g., text classification, genomics). Not ideal when interpretability is needed (black-box model).

**Assumptions:**
1. **Approximate linear separability** (for linear SVM) — data should be *roughly* linearly separable for good performance; the soft margin formulation (controlled by `C`) allows some misclassifications, so perfect separability is not required *(Can still be used if/with the Kernel Trick — RBF, Polynomial kernels — to handle non-linear boundaries, or with soft margin (smaller `C`) to tolerate some misclassification)*
2. **Features have the same scale** — SVM maximizes geometric (Euclidean) distance, so large-scale features dominate *(Can still be used if/with `StandardScaler` or `MinMaxScaler`)*
3. **IID** — independent and identically distributed data *(**Cannot** remain a candidate model if data has strong sequential/temporal dependencies)*
4. **Not too many outliers/noise** — large `C` forces the model to classify outliers correctly, ruining the boundary *(Can still be used if/with tuning `C` to a smaller value (Soft Margin) to allow some misclassifications for a wider, more robust margin)*
5. **Not suitable for very large datasets** — training time complexity is approximately $O(n^2)$ to $O(n^3)$ for kernel SVMs *(Can still be used with `LinearSVC` which uses a different solver and scales much better, or with `SGDClassifier(loss='hinge')` for very large datasets)*

### [K-Nearest Neighbors (KNN)](./03_non-linear_and_ensemble_models/17_knn_theory.md)
A good candidate for **small datasets** with **low dimensionality** where the decision boundary is **highly irregular** and hard to define with a parametric model. Ideal for quick prototyping since there is no training phase. Also useful for **regression** (averaging neighbors' values). Simple to understand and explain, but **not suitable for production on large datasets** due to slow prediction time ($O(N)$ per query).

**Assumptions:**
1. **Proximity equals similarity** — points close in distance share the same label *(**Cannot** remain a candidate model if distance in the feature space is not meaningful for the problem)*
2. **Features have the same scale** — distance calculation is dominated by large-magnitude features *(Can still be used if/with `StandardScaler` or `MinMaxScaler` — this is **mandatory**)*
3. **All features are relevant** — irrelevant/noisy features corrupt the distance metric *(Can still be used if/with feature selection or dimensionality reduction like PCA)*
4. **Low dimensionality** — suffers from the Curse of Dimensionality in high dimensions *(Can still be used if/with PCA or feature selection to reduce dimensions)*
5. **Computationally expensive at prediction time** — must compute distances to all training points for each prediction *(Can still be used with KD-trees or Ball Trees for speedup, but these also degrade in high dimensions)*

### [Naive Bayes](./03_non-linear_and_ensemble_models/20_naive_bayes_theory.md)
A good candidate for **text classification** problems (spam detection, sentiment analysis, document categorization) where the feature space is **very high-dimensional** (thousands of word features) and the dataset may be **small**. Extremely fast to train and predict, works well even with limited data, and handles high dimensionality gracefully. A strong **baseline for NLP tasks**.

**Assumptions:**
1. **Feature independence** (given the class) — all features are conditionally independent of each other *(Can still be used even if/with correlated features — the model performs surprisingly well in practice despite this violation, especially for text classification)*
2. **IID** — independent and identically distributed samples *(**Cannot** remain a candidate model if the data has strong temporal/sequential dependencies)*
3. **Appropriate likelihood distribution must be chosen** — Gaussian NB assumes features are normally distributed; Multinomial NB assumes count/frequency features; Bernoulli NB assumes binary features *(Can still be used by selecting the correct variant for your data type)*
4. **Outputs poorly calibrated probabilities** — the predicted probabilities are often pushed toward 0 and 1 due to the independence assumption *(Can still be used with probability calibration via `CalibratedClassifierCV` if well-calibrated probabilities are needed)*

### [Random Forest](./03_non-linear_and_ensemble_models/23_bias_variance_and_ensemble_models_theory.md)
A good candidate for **general-purpose classification and regression** when you want **high accuracy without much tuning**. Excellent default choice when interpretability is not the top priority. Robust to overfitting (unlike a single Decision Tree), handles mixed feature types, and provides built-in **feature importance** rankings. Ideal when you need a strong, reliable model with minimal preprocessing and hyperparameter sensitivity.

**Assumptions:**
1. **No strong assumptions** about data distribution, linearity, or feature scaling — ensemble of Decision Trees ✅
2. **Sufficient diversity among trees** — relies on bootstrap sampling and random feature subsets *(This is handled internally by the algorithm)*
3. **Cannot extrapolate beyond the training range** (inherited from Decision Trees) — predictions are bounded by the min/max of the training target values *(**Cannot** remain a candidate model if out-of-range predictions are needed — use linear models or gradient boosting with linear base learners)*

⚠️ Trees individually assume sufficient data per split, but the ensemble **mitigates** overfitting through averaging/voting.

### [AdaBoost / Gradient Boosting (XGBoost)](./03_non-linear_and_ensemble_models/23_bias_variance_and_ensemble_models_theory.md)
A good candidate for **competition-winning accuracy** on structured/tabular data when you want to **squeeze out every last bit of performance**. XGBoost is the go-to model for Kaggle competitions and real-world production systems on tabular data. Ideal when you are willing to invest time in **hyperparameter tuning** (learning rate, number of estimators, max depth) and interpretability is secondary to predictive power. Also strong when the initial models underfit (high bias) — boosting is specifically designed to **reduce bias**.

**Assumptions:**
1. **No strong assumptions** about data distribution, linearity, or feature scaling — ensemble of weak learners ✅
2. **Weak learners are slightly better than random** — applies primarily to **AdaBoost**: each base model must have >50% accuracy for binary classification. For **Gradient Boosting / XGBoost**, this constraint is relaxed since learners fit residuals/gradients rather than being weighted by accuracy *(Can still be used if/with increasing the number of boosting rounds or tuning learning rate)*

⚠️ **Main risk:** Can overfit if too many boosting rounds or learning rate too high *(Can still be used if/with early stopping, learning rate reduction, or regularization parameters)*

### [K-Means Clustering](./04_building_unsupervised_learning_models/02_k-means_clustering_theory.md)
A good candidate for **unsupervised partitioning** when you expect the data to form **roughly spherical, evenly-sized groups** and need a **fast, scalable** algorithm. Ideal as the **first clustering method to try** — it's simple, intuitive, and scales well to large datasets. Common use cases: customer segmentation, image compression (color quantization), and market segmentation.

**Assumptions:**
1. **Clusters are convex (spherical/blob-shaped)** *(**Cannot** remain a candidate model if clusters have arbitrary shapes like crescents, spirals, or rings — use DBSCAN/HDBSCAN instead)*
2. **Clusters are roughly balanced in size** *(Can still be used if/with careful initialization like K-Means++ and manual post-analysis)*
3. **Number of clusters `k` is known** *(Can still be used if/with the Elbow Method, Silhouette Analysis, or Davies-Bouldin Index to estimate `k`)*
4. **Sensitive to outliers** — the mean (centroid) is pulled by extreme values *(Can still be used if/with outlier removal before clustering)*
5. **Uses Euclidean distance** — features must be numerical and on the same scale *(Can still be used with `StandardScaler` before clustering; cannot remain a candidate model for categorical features — use K-Modes or K-Prototypes instead)*

### [DBSCAN](./04_building_unsupervised_learning_models/05_dbscan_and_hdbscan_clustering_theory.md)
A good candidate for clustering problems where clusters have **arbitrary, non-spherical shapes** (crescents, spirals, elongated blobs) and you **don't know the number of clusters** in advance. Excellent when the data contains **noise/outliers** that should be explicitly excluded rather than forced into a cluster. Common use cases: geospatial data (finding dense regions on a map), anomaly detection, and any data where cluster geometry is complex.

**Assumptions:**
1. **Clusters have approximately uniform density** *(**Cannot** remain a candidate model if clusters have varying densities — use HDBSCAN instead)*
2. **Appropriate `epsilon` and `min_samples` can be defined** *(Can still be used if/with the k-distance plot to estimate `epsilon`)*

✅ Does **not** assume convex shapes, does **not** need `k` pre-specified, and handles outliers natively.

### [HDBSCAN](./04_building_unsupervised_learning_models/05_dbscan_and_hdbscan_clustering_theory.md)
A good candidate for **complex, real-world clustering** where clusters have **varying densities**, arbitrary shapes, and the data contains noise. The most **robust, general-purpose density-based** clustering algorithm — essentially a "set it and forget it" upgrade over DBSCAN. Ideal when you have **no prior knowledge** about the number, shape, or density of clusters and want the algorithm to figure it out.

**Assumptions:**
1. **Minimal assumptions** — handles varying densities, arbitrary shapes, and outliers ✅
2. **`min_cluster_size` must be specified** *(Can still be used if/with experimenting on a range of values for this single hyperparameter)*

### [PCA](./04_building_unsupervised_learning_models/09_dimension_reduction_algorithms_theory.md)
A good candidate for **dimensionality reduction as a preprocessing step** before feeding data into another model (e.g., to combat the Curse of Dimensionality for KNN or to speed up training). Also excellent for **data visualization** (projecting high-dimensional data to 2D/3D) when relationships are linear, and for **noise reduction** by discarding low-variance components. Fast, deterministic, and well-understood.

**Assumptions:**
1. **Features are linearly correlated** — captures only linear relationships *(**Cannot** remain a candidate model if the data has complex non-linear structure — use t-SNE or UMAP for visualization)*
2. **Features have the same scale** — variance-based method is dominated by large-scale features *(Can still be used if/with `StandardScaler` before applying PCA)*
3. **High variance = high information** — PCA equates maximum variance with most important directions *(**Cannot** remain a candidate model if the most informative directions are not the highest-variance ones)*
4. **Features should be numerical and continuous** — PCA on categorical or binary features is not meaningful *(**Cannot** remain a candidate model for categorical data — use MCA (Multiple Correspondence Analysis) instead)*

### [t-SNE](./04_building_unsupervised_learning_models/09_dimension_reduction_algorithms_theory.md)
A good candidate for **visualizing high-dimensional data in 2D/3D** when you want to reveal **local cluster structure** — e.g., seeing whether classes form distinct groups in image embeddings, word embeddings, or genomic data. Ideal for **exploratory analysis and presentations** where you need a striking, cluster-separated plot. **Not suitable** as a general-purpose dimensionality reduction step before another model (results are stochastic, slow, and don't preserve global distances).

**Assumptions:**
1. **Local structure is more important than global structure** — inter-cluster distances in the output are often meaningless *(**Cannot** remain a candidate model if you need to preserve or interpret the relative distances/positions between clusters — use UMAP or PCA instead)*
2. **Perplexity hyperparameter is set appropriately** — loosely controls the effective number of neighbors; wrong values distort the visualization *(Can still be used if/with experimenting across a range of perplexity values, typically 5–50)*
3. **Dataset is not too large** — exact t-SNE has $O(N^2)$ time complexity *(Can still be used if/with the Barnes-Hut approximation ($O(N \log N)$, default in scikit-learn) or with subsampling the data)*
4. **Results are stochastic** — different runs produce different layouts *(Can still be used if/with setting a fixed `random_state` seed for reproducibility)*

### [UMAP](./04_building_unsupervised_learning_models/09_dimension_reduction_algorithms_theory.md)
A good candidate for **general-purpose non-linear dimensionality reduction** that balances **local and global structure** preservation. Superior to t-SNE in most practical scenarios: faster, more scalable, and produces layouts where the relative positions between clusters are more meaningful. Ideal for both **visualization** (2D/3D plots) and as a **preprocessing/feature-extraction step** before feeding data into a downstream model (e.g., clustering, classification). The modern default choice for non-linear dimensionality reduction.

**Assumptions:**
1. **Data lies on a low-dimensional manifold** embedded in high-dimensional space *(**Cannot** remain a candidate model if the data has no meaningful lower-dimensional structure — the projection will be arbitrary)*
2. **`n_neighbors` and `min_dist` hyperparameters are set appropriately** — `n_neighbors` controls local vs. global balance, `min_dist` controls how tightly points cluster *(Can still be used if/with systematic tuning of these two parameters)*
3. **Results are stochastic** — different runs may produce slightly different layouts *(Can still be used if/with setting a fixed `random_state` seed for reproducibility)*