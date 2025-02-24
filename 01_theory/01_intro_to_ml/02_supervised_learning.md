# Supervised Learning

Supervised learning's tasks are well-defined and can be applied to a multitude of scenarios -like identifying spam or predicting precipitation. Supervised machine learning is based on the following core concepts:

1. Data
2. Model
3. Training
4. Evaluating
5. Inference

## 1. Data
Data is the driving force of ML. Data comes in the form of words and numbers stored in tables, or as the values of pixels and waveforms captured in images and audio files. We store related data in datasets. For example, we might have a dataset for the following:
* Images of cats
* Housing prices
* Weather information

Datasets are made of individual [examples](https://developers.google.com/machine-learning/glossary#example) that contain [features](https://developers.google.com/machine-learning/glossary#feature) and a [label](https://developers.google.com/machine-learning/glossary#label). You could think of an example as analogous to a single row in a spreadsheet. Features are the values that a supervised model uses to predict the label. The label is the "answer", or the value we want the model to predict. In a weather model that predicts the rainfall, the features could be _latitude, longitude, temperature, humidity, cloud coverage, wind direction,_ and _atmospheric pressure_. The label would be _rainfall amount_. 

Examples that contain both features and a label are called [labeled examples](https://developers.google.com/machine-learning/glossary#labeled-example).

**Two labeled examples:**  

![](https://developers.google.com/static/machine-learning/intro-to-ml/images/labeled_example.png)

In contrast, unlabeled examples contain features, but no label. After you create the model, the model predicts the label from the features.

**Two unlabeled examples:** 
![](https://developers.google.com/static/machine-learning/intro-to-ml/images/unlabeled_example.png)

### Dataset Characteristics

#### Characterization by size and diversity:**  
A dataset is characterized by its size and diversity. Size indicates the number of examples. Diversity indicates the range those examples cover. Good datasets are both large and highly diverse.

Some datasets are both large and diverse. However, some datasets are large but have low diversity, and some are small but highly diverse. In other words, a large dataset doesn't guarantee sufficient diversity, and a dataset that is highly diverse doesn't guarantee sufficient examples.

For instance, a dataset might contain 100 years worth of data, but only for the month of July. Using this dataset to predict rainfall in January would produce poor predictions. Conversely, a dataset might cover only a few years but contain every month. This dataset might produce poor predictions because it doesn't contain enough years to account for variability.

#### Characterization by number of features:**  
A dataset can also be characterized by the number of its features.


## 2. Model