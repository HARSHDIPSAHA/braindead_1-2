# braindead_1-2

[filtered_data.csv](https://www.kaggle.com/datasets/harshdipsaha/arxiv-data-from-2023-25)


# BrainDead Team Project Repository  

This repository contains implementations for two problem statements as part of the **BrainDead** competition:  

- **PS1:** IPL Data Analysis and 2025 Winner Prediction  
- **PS2:** Research Article Summarization Using Advanced NLP Techniques  

## Table of Contents  
- [Overview](#overview)  
- [Problem Statement 1: IPL Data Analysis](#problem-statement-1-ipl-data-analysis)  
- [Problem Statement 2: Research Article Summarization](#problem-statement-2-research-article-summarization)  
- [Repository Structure](#repository-structure)  
- [Setup Instructions](#setup-instructions)  
- [PS1: IPL Analysis Usage](#ps1-ipl-analysis-usage)  
- [PS2: Paper Summarization Usage](#ps2-paper-summarization-usage)  
- [Contributors](#contributors)  

## Overview  
This repository showcases our solutions to two distinct data science challenges:  

- **Cricket analytics** with predictive modeling for IPL 2025  
- **Scientific paper summarization** using hybrid NLP techniques  

## Problem Statement 1: IPL Data Analysis  
An extensive analysis of IPL data (2008-2024) to uncover insights and predict the 2025 IPL winner. The project includes:  

- Comprehensive data cleaning and preprocessing  
- Exploratory data analysis of team and player performance  
- Feature engineering and extraction  
- Ensemble model development for winner prediction  
- Visualization of key metrics and trends  

## Problem Statement 2: Research Article Summarization  
A hybrid extractive-abstractive model for summarizing scientific research papers. Key features include:  

- Processing of multiple research article datasets (**CompScholar, ArXiv, PubMed**)  
- Token length reduction (**95%+ reduction across datasets**)  
- Vocabulary optimization (**10-16% reduction in size, 50%+ improvement in OOV rates**)  
- Data quality enhancement (**elimination of null values and duplicates**)  
- LED-based architecture for long document summarization  

## Repository Structure  











## Setup Instructions  

### Prerequisites  
- Python **3.7+**  
- Git  

### Installation  

###Clone the repository:  
```bash
git clone https://github.com/HARSHDIPSAHA/braindead_1-2.git
cd braindead_1-2
```

### Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Install dependencies for both projects:

```bash
# For PS1: IPL Analysis
pip install pandas numpy matplotlib seaborn scikit-learn xgboost tensorflow

# For PS2: Paper Summarization
pip install torch transformers pandas numpy scikit-learn rouge-score nltk

# For PS2: Download NLTK resources
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

```
PS1: IPL Analysis Usage
Navigate to the PS1 directory:

bash
Copy
Edit
cd ps1
Download the IPL dataset:

bash
Copy
Edit
# Download from the provided link in the problem statement
# Place the matches.csv and deliveries.csv files in the data/ directory
Run the analysis notebook:

bash
Copy
Edit
jupyter notebook notebooks/ipl_analysis.ipynb
For prediction model:

bash
Copy
Edit
jupyter notebook notebooks/ipl_prediction.ipynb
PS2: Paper Summarization Usage
Navigate to the PS2 directory:

bash
Copy
Edit
cd ps2
Download and prepare datasets:

bash
Copy
Edit
# For ArXiv and PubMed datasets
python scripts/download_datasets.py

# For CompScholar dataset (if available)
# Place the dataset in the data/ directory
Run the summarization notebook:

bash
Copy
Edit
jupyter notebook notebooks/paper_summarization.ipynb
Generate summaries for new papers:

python
Copy
Edit
from models.summarizer import generate_summary

# Example usage
paper_text = "..."
summary = generate_summary(paper_text)
print(summary)


