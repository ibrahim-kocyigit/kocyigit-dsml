# Where Do Data Come From?

## Why Does Data Origin Matter?

- Understanding where data come from is crucial for choosing the right statistical approach.
- The process that generated the data affects which analytic procedures are valid.

## Two Key Types of Data

### 1. Organic (Process) Data

- Generated naturally as a result of ongoing processes, often by computerized systems or sensors.
- Examples:
  - Financial transactions, stock market exchanges
  - Netflix viewing history
  - Web browser activity (pages visited, time spent)
  - Sporting event outcomes and player statistics
  - Temperature and pollution sensor data
- Characteristics:
  - Often massive ("big data")
  - Generated over time, sometimes at high frequency
  - Require significant computational resources to process and prepare for analysis

### 2. Designed Data Collection

- Data collected through a planned study or survey to address specific research questions.
- Examples:
  - Surveys/interviews of a sampled population
  - Extracting and coding specific tweets for sentiment analysis
- Characteristics:
  - Typically smaller datasets
  - Easier to work with computationally
  - Data are collected for a specific purpose, not as a byproduct of a process

## Big Data

- "Big data" usually refers to large, organically generated datasets (e.g., transactions, sensor data).
- Processing and preparing big data for analysis is a major challenge and an active area of research.

## The Importance of i.i.d. (Independent and Identically Distributed) Data

- **i.i.d.** stands for **independent and identically distributed**:
  - **Independent:** Each observation does not influence or depend on others.
  - **Identically distributed:** All observations come from the same statistical distribution.
- Many statistical procedures assume data are i.i.d.
- Example: Final exam scores in a large class, where each student's score is independent and all scores follow the same distribution (e.g., normal/bell curve).

### Why i.i.d. Matters

- If data are i.i.d., we can estimate features like the mean, variance, and percentiles with known precision.
- If data are **not** i.i.d., standard statistical procedures may not be valid.

## Examples of Non-i.i.d. Data

- **Dependence:** Students cheat off each other, so their scores are correlated.
- **Non-identical distributions:** Males and females have different score distributions; students from different discussion sections have different means.
- **Clustered data:** Students in the same section or group may have similar outcomes.

- In these cases, special analytic procedures are needed to account for dependencies or different distributions.

## Key Takeaways

- Always ask: **Where did the data come from?**
  - Was it generated organically (process data) or through a designed collection?
  - Could the process have introduced dependencies or non-identical distributions?
- Before analysis, determine if your data can be considered i.i.d.
- The origin and structure of your data determine which statistical methods are appropriate.

---

**Next:** [Variable Types](./02_variable_types.md)