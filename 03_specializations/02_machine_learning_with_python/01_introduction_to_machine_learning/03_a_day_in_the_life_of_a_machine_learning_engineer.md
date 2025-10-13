# A Day in the Life of a Machine Learning Engineer

## Project Overview

**Business Goal**: Increase revenue by creating a model that recommends similar products based on customer purchase history.

**User Pain Point**: "As a beauty product customer, I would like to receive recommendations for other products based on my purchase history so that I will be able to address my skincare needs and improve the overall health of my skin."

## Machine Learning Lifecycle in Practice

### Problem Definition
- **Importance**: Ensures the ML solution aligns with client needs
- Critical first step to define the business problem and user requirements

### Data Collection
**Data Sources Identified**:
- **User Data**: Demographics, purchase history, completed transactions
- **Product Data**: Inventory, product functions, ingredients, popularity, customer ratings
- **Behavioral Data**: Saved products, liked products, search history, most visited products

**ETL Process**: Wrangling, aggregating, joining, merging, and mapping data onto one central source to avoid dealing with multiple databases.

### Data Preparation
**This process overlaps with data collection and is time-consuming**

**Key Activities**:
- Cleaning data to filter out irrelevant information
- Removing extreme values that could skew the dataset
- Handling missing values (removing or randomly generating)
- Ensuring proper data formats (dates as dates, strings properly identified)
- Feature engineering

**Feature Engineering Examples**:
- Calculate average duration between transactions for each user
- Identify most frequently purchased products per user
- Create features for skin issues each product targets

**Exploratory Data Analysis**:
- Create plots to visually identify patterns
- Validate data with subject matter experts
- Correlation analysis to identify important features for buying habits
- Plan data splitting strategy for training/testing

**Data Splitting Approach**: Used most recent transaction as test set, ensuring at least one transaction from the same user in training set.

### Model Development

**Strategy**: Leverage pre-existing frameworks rather than building from scratch

**Technique 1: Content-Based Filtering**
- Finds similarity between products based on product content
- Example: If user uses water-rich cleanser → recommend highly moisturizing products
- Creates similarity scores between purchased products and other products
- Considers additional factors (e.g., ingredients user avoids)

**Technique 2: Collaborative Filtering**
- Creates similarities between users based on product interactions
- Groups users into buckets based on characteristics (age, region, skin type, ratings, purchases)
- Uses average ratings from similar users to make recommendations
- Assumes new users will have preferences similar to group averages

**Final Model**: Combination of both techniques

### Model Evaluation

**Two-Phase Approach**:
1. **Initial Testing**: Tuning and testing on reserved test dataset
2. **User Testing**: Experiment with recommendations on user group and collect feedback

**Feedback Metrics**:
- User ratings of recommendations
- Click-through rates on recommended products
- Purchase conversion rates
- Other relevant business metrics

### Model Deployment & Maintenance

**Production**: Integrated into beauty product app and website

**Post-Deployment**:
- Continuous performance tracking
- Monitoring to ensure business requirements are met
- Future iterations may include retraining with new data
- Ongoing model improvement and capability expansion

## Key Takeaways

- Each step in the ML lifecycle is crucial for solution success
- Data preparation and collection are particularly time-intensive processes
- Continuous monitoring and improvement are required after deployment
- Real-world ML engineering involves iterative refinement and user feedback integration

---

**Next:** [Data Scientist vs. AI Engineer](./04_data_scientist_vs_ai_engineer.md)