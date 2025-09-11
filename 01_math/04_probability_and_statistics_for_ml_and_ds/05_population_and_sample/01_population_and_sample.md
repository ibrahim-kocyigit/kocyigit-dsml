# Population and Sample

## Introduction

In statistics and machine learning, two foundational concepts are **population** and **sample**. Understanding the difference between them is essential for analyzing data and drawing valid conclusions.

- **Population:** The entire group of individuals or items you want to study.
- **Sample:** A smaller subset of the population that you actually observe or measure.

## Example: Statistopia

Imagine you are a data scientist on the island of Statistopia. Your task is to find the average height of its residents.

- **Population:** All 10,000 people living on Statistopia.
- **Sample:** A manageable subset, such as 100 randomly selected people.

Since measuring everyone is impractical, you use a sample to estimate the population’s average height.

## Sampling Methods

Suppose Statistopia has only 10 people for illustration. You want to select 4 for your study. There are two ways:

1. **Random Sampling:** Pick 4 people at random.  
   - This method is preferred because it gives a representative sample.
2. **Ordered Sampling:** Pick the first 4 people in a line sorted by height.  
   - This method is biased and likely underestimates the average height.

**Key Point:**  
Always use random sampling to avoid bias.

## Independence and Identical Distribution

When taking multiple samples:
- Each sample should be **independent** (the selection of one does not affect the others).
- Each sample should be **identically distributed** (selected using the same rule).

If you sample without replacement (not allowing repeats), later samples depend on earlier ones, which is not ideal. Sampling with replacement ensures independence.

## Real-World Example: Avocado Prices

Suppose you want to study avocado prices in the US after the avocado toast trend.

- **Population:** All avocados sold in the US.
- **Sample:** Avocados sold by four randomly selected stores.

## Implications in Machine Learning

In machine learning, every dataset you work with is actually a sample, not the population—even if it’s very large.

**Example:**  
If you train a model to classify cat images, your dataset is a sample from all possible images of cats and non-cats.

**Importance of Representativeness:**  
A representative sample means your dataset’s distribution matches the population’s. If your cat images all have grass backgrounds, your model may incorrectly associate grass with cats and fail on other backgrounds.

## Formal Definitions

- **Population:** The entire set of individuals or elements you want to study.
- **Sample:** A subset of the population used to draw conclusions about the whole.
- **N:** Population size.
- **n:** Sample size.

## Key Takeaways

- Populations are the full group you want to study; samples are the observed subset.
- Random, independent, and identically distributed samples are crucial for valid statistical inference.
- In machine learning, your dataset is always a sample, so representativeness matters.

--- 

**Next:** [Sample Mean](./02_sample_mean.md)