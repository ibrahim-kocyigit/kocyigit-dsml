# Introduction to Core Data Concepts

Core data concepts are the fundamental ideas and vocabulary used to describe and understand data. These concepts are essential for working with data in any field, especially data science. They helps us categorize, analyze, and interpret the information we collect.

## Use Cases
* **Data Analysis:** Understanding data types and properties is the _first stage_ in any data analysis project.
* **Choosing Appropriate Methods:** Knowing the characteristics of your data helps you select the correct statistical methods and machine learning algorithms. (For example, you wouldn't use a method designed for continuous data on categorical data.)
* **Communication:** Using the correct terminology allows you to communicate clearly and effectively with other data scientists, researchers, and stakeholders.
* **Data Quality:** Recognizing different types of data helps in identifying and handling data quality issues (e.g., incorrect data types, missing values).
* **Feature Engineering:** Many machine learning techniques require specific data types. Understanding these concepts helps you transform your data appropriately (e.g., converting categorical data to numerical representations.)

## Key Data Concepts

### Continuous vs. Discrete Data
**Continuous data** can take _any_ value withing a given range. There are infinitely many values between any two values. Examples: height, weight, temperature.

**Discrete (categorical) data** can only take _specific_ values. There are gaps between possible values. Examples: number of cars in a parking lot, the result of a dice roll, categories (e.g., car models). **Note** that discrete data can be numeric (like a dice roll) or non-numeric (like car models).

### Nominal vs. Ordinal Data
These terms apply to _categorical_ (discrete) data:

**Nominal data** is categories with _no inherent order_ or ranking. Examples: colors (red, blue, green), types of animals (dog, cat, bird). You can't sort nominal data in a meaningful way. 

**Ordinal data** is categories with a _meaningful order_ or ranking. Examples: education levels (high school, bachelor's, master's, PhD), customer satisfaction ratings (very dissatisfied, dissatisfied, neutral, satisfied, very satisfied), airline passenger classes (first, second, third).

### Structured vs Unstructured Data
**Structured data** is organized in a predefined format, typically rows and columns (like a table or spreadsheet). It is easy to search and analyze. Examples: data in a relational database, CSV files, Excel spreadsheets.

**Unstructured data** does _not_ have a predefined format. It's more difficult to analyze directly. Examples: text documents (emails, articles), images, audio files, video files. **Note** that unstructured data can be _encoded_ in a structured file format (like a JPEG image), but the _content_ itself is unstructured.

### Population vs Sample Data
**Population data** is the data of the _entire_ group of individuals or items that you are interested in studying. Example: The exam scores of _all_ students in a school.

**Sample data** is the data of a _subset_ of the population that is selected for study. Example: A survey of 100 students school of 1.000 students. Samples are used when it's impractical or impossible to collect data on the entire population. A good sample should be _representative_ of the population.


