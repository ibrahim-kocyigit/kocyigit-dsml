# Unsupervised Learning

Unsupervised learning aims to discover hidden patterns and structures within data without the aid of labeled examples. It's akin to exploring an unknown territory, seeking inherent groupings or relationships. Unsupervised machine learning is based on the following core concepts:

1.  Data
2.  Model
3.  Training
4.  Evaluating
5.  Discovery

## 1. Data

Data in unsupervised learning, like its supervised counterpart, is the foundation. It comprises words, numbers, images, and audio, stored in datasets. However, a key difference is that these datasets consist of **unlabeled examples**. This means each example contains features, but there are no corresponding labels indicating a "correct" answer or category. For example:

* A collection of customer purchase histories.
* A set of network traffic logs.
* A library of images without predefined categories.

Each example in these datasets is a set of features, but the underlying structure or relationships are unknown.

**Two unlabeled examples:**

<img src="https://developers.google.com/static/machine-learning/intro-to-ml/images/unlabeled_example.png" alt="" style="width:800px;"/>

### Dataset Characteristics

#### Characterization by size and diversity
Similar to supervised learning, size and diversity are crucial. A large and diverse dataset allows the model to uncover more robust and generalizable patterns. However, in unsupervised learning, diversity takes on a different meaning. It refers to the variety of inherent structures and relationships within the data, rather than the range of labeled outcomes.

#### Characterization by number of features
The number of features impacts the complexity of the patterns the model can discover. More features can reveal finer-grained structures, but can also lead to increased computational cost and potential noise.

## 2. Model

In unsupervised learning, a model is designed to find inherent structure in the data. This structure might be in the form of clusters, associations, or reduced dimensionality. The model aims to learn representations of the data that highlight these underlying patterns.

## 3. Training

Training an unsupervised learning model involves feeding it the unlabeled dataset and allowing it to discover patterns. The model adjusts its internal parameters to better represent the data's structure. For example, a clustering model might iteratively group similar data points together, while a dimensionality reduction model might find a lower-dimensional representation that preserves the most important information.

The model does not compare its output to any known "correct" answer, as there are no labels. Instead, it seeks to optimize an objective function that measures the quality of the discovered structure. This might involve minimizing the distance between data points within the same cluster or maximizing the variance of the projected data in a lower-dimensional space.

## 4. Evaluating

Evaluating an unsupervised learning model is different from evaluating a supervised model. Since there are no labels, traditional metrics like accuracy are not applicable. Instead, evaluation focuses on assessing the quality and usefulness of the discovered patterns. This can involve:

* **Visual inspection:** Examining the clusters or reduced-dimensional representations to see if they make intuitive sense.
* **Internal validation:** Measuring the compactness and separation of clusters.
* **External validation:** Using external information (if available) to assess the quality of the discovered patterns.
* **Domain expertise:** Consulting with experts in the field to determine if the discovered patterns are meaningful and useful.

## 5. Discovery

The "inference" stage in unsupervised learning is more accurately described as "discovery." Once the model has learned the data's structure, it can be used to:

* **Identify clusters:** Group similar data points together.
* **Detect anomalies:** Identify data points that deviate significantly from the learned patterns.
* **Reduce dimensionality:** Find a lower-dimensional representation of the data that preserves its essential information.
* **Discover associations:** Identify relationships between different features.

These discoveries can provide valuable insights and lead to new understandings of the data.