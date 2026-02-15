📊 AI-Augmented Exploratory Data Science Platform

<img width="1762" height="948" alt="1" src="https://github.com/user-attachments/assets/99a33df5-116a-4b73-bd24-1cd9ee5898cb" />

<img width="1763" height="1000" alt="2" src="https://github.com/user-attachments/assets/c4b476a0-d893-4187-8b06-27b006bac7c2" />



🔬 Project Overview

This project is an AI-augmented exploratory data science system that automates:

Exploratory Data Analysis (EDA)

Statistical profiling

Intelligent missing value treatment

Feature diagnostics

Automated visualization generation

Natural language dataset interrogation via LLM agents

The goal of this system is to replicate the early-stage workflow of a data processing for data scientist, analysts and data engineers, where understanding data quality, distribution, and structure is critical before modeling.

🎯 Core Objective

To design a reproducible, intelligent data exploration framework that:

Reduces manual EDA time

Applies statistically informed preprocessing strategies

Surfaces feature-level insights automatically

Integrates LLM-driven reasoning for analytical querying

This mirrors real-world workflows in:

Applied Machine Learning

Predictive Modeling

Data Product Prototyping

Analytics Automation

🧠 Data Science Components
1️⃣ Automated Statistical Profiling

For numeric variables:

Mean

Median

Standard deviation

Min / Max

Quartiles

Distribution shape inspection

For categorical variables:

Frequency inspection

Cardinality awareness

Null analysis

This simulates the exploratory phase prior to feature engineering.

2️⃣ Intelligent Missing Value Strategy

Instead of naive imputation, the system applies distribution-aware logic:

Numeric Features

Median imputation for skewed distributions

Mean imputation for symmetric distributions

Categorical Features

Mode imputation

All cleaning steps are logged and reported.

This reflects best practices used in:

Regression modeling

Tree-based models

Production ML pipelines

3️⃣ Distribution & Outlier Diagnostics

The system automatically generates:

📊 Histograms → Distribution shape

📦 Boxplots → Outlier detection

🔗 Scatter plots → Feature relationships

This supports:

Variance inspection

Skew detection

Non-linearity observation

Potential multicollinearity exploration

4️⃣ AI-Powered Analytical Reasoning

Using OpenAI + LangChain CSV agent, the system enables:

Natural language data interrogation

Automated statistical explanation

On-demand feature analysis

Insight summarization

This mimics an AI-assisted Data Scientist capable of:

Investigating anomalies

Answering statistical questions

Surfacing structural insights

📈 Analytical Value

This platform supports early-stage ML pipeline development:

✔ Data quality assessment

✔ Preprocessing validation

✔ Feature distribution understanding

✔ Relationship exploration

✔ Rapid hypothesis testing


It accelerates:

Dataset readiness for modeling

🛠 Technical Stack

Language	-- Python

Data Processing	--> Pandas

Visualization	--> Matplotlib

Interface	--> Streamlit

AI Orchestration	--> LangChain

LLM	--> OpenAI

Environment Management	--> python-dotenv

🧪 Reproducibility Guide

1. Clone Repository

git clone https://github.com/your-username/CSV-Analyzer.git

cd CSV-Analyzer

2. Create Virtual Environment
python -m venv venv


Activate:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3.Install Dependencies

pip install -r requirements.txt

4.Configure API Key

Create .env:

OPENAI_API_KEY=your_key_here

5. Run Application
streamlit run main.py

🧠 Skills Demonstrated
Statistical Reasoning

Distribution-aware imputation

Outlier diagnostics

Variance analysis

Null pattern inspection

Data Preprocessing

Automated cleaning strategies

Feature typing logic

Null-value policy implementation

Structured transformation pipeline

Exploratory Data Analysis

Automated profiling

Relationship discovery

Structural inspection

Data quality auditing

Applied AI Integration

LLM-based analytical querying

Tool-driven agent orchestration

Prompt engineering for structured reasoning

Production Awareness

Reproducible environment setup

Secure API management

Interactive analytics deployment

Modular architecture


🚀 Potential Future Extensions

Correlation heatmap with multicollinearity detection

Skewness quantification and transformation recommendations

Feature scaling diagnostics

Model-ready dataset export

Auto feature engineering suggestions

ML model integration (baseline regression/classification)

SHAP-based feature importance visualization
