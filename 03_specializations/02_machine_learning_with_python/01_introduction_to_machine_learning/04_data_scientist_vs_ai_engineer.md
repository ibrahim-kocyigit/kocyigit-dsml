# Data Scientist vs. AI Engineer

## Industry Context

The emergence of **generative AI** has split off into its own distinct field called **AI engineering**, creating a new role alongside traditional data science.

## Key Differences

### Use Cases

#### Data Scientist: Data Storyteller
- **Descriptive Analytics**: Describes the past through:
  - Exploratory Data Analysis (EDA) - graphing data and statistical inference
  - Clustering - grouping similar data points (e.g., customer segmentation)
- **Predictive Analytics**: Predicts what comes next using:
  - Regression models - predict numeric values (temperature, revenue)
  - Classification models - predict categorical values (success/failure)

#### AI Engineer: AI System Builder
- **Prescriptive Use Cases**: Chooses the best course of action through:
  - Decision optimization - selecting optimal paths based on requirements
  - Recommendation engines - suggesting targeted marketing campaigns
- **Generative Use Cases**: Creates new content using foundation models for:
  - Intelligent assistants (coding assistants, digital advisors)
  - Chatbots with conversational search and content summarization

### Data Types

#### Data Scientist
- Primarily works with **structured/tabular data**
- Datasets range from hundreds to hundreds of thousands of observations
- Requires extensive cleaning and preprocessing:
  - Removing outliers
  - Joining and filtering tables
  - Feature engineering

#### AI Engineer
- Primarily works with **unstructured data**:
  - Text, images, videos, audio files
- Massive scale: billions to trillions of tokens for LLM training
- Much larger data requirements than traditional ML models

### Models

#### Data Science Toolbox
- Hundreds of different models and algorithms
- Each use case requires different datasets and model training
- **Narrow scope**: Harder to generalize beyond training domain
- **Smaller size**: Fewer parameters, less compute power
- **Faster training**: Seconds to hours

#### Generative AI Toolbox
- Primarily **foundation models**
- **Revolutionary capability**: One model generalizes to wide range of tasks without retraining
- **Wide scope**: Broad generalization capabilities
- **Massive scale**: Billions of parameters
- **Intensive resources**: Hundreds to thousands of GPUs
- **Long training**: Weeks to months

### Development Processes

#### Data Science Process
1. Start with use case
2. Pick and prepare data
3. Train and validate model using:
   - Feature engineering
   - Cross-validation
   - Hyperparameter tuning
4. Deploy model to cloud endpoint for real-time prediction

#### Generative AI Process
1. Start with use case
2. **Skip to pre-trained models** via AI democratization (open-source communities like Hugging Face)
3. **Prompt engineering**: Interact with foundation models using natural language
4. Build larger AI systems using frameworks:
   - Chaining prompts together
   - Parameter-efficient fine-tuning (PEFT) on domain-specific data
   - Retrieval-augmented generation (RAG) to ground answers in truth
   - Creating autonomous agents for complex multi-step problems
5. Embed AI in larger systems/workflows:
   - Assistants or virtual agents
   - Applications with UI
   - Automation systems

## Overlap and Evolution

- **Field Overlap**: Data scientists still work on prescriptive cases; AI engineers still work with structured data
- **Rapid Evolution**: Both fields evolving quickly with new research, models, and tools emerging daily
- **Shared Foundation**: Both leverage data, AI, and creativity to build solutions

---

**Next:** [Tools for Machine Learning](./05_tools_for_machine_learning.md)