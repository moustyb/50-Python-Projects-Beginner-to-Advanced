# Sentiment Analyzer

A simple sentiment analysis tool that classifies text as positive, negative, or neutral using classical machine learning.

## Features
- Text preprocessing (lowercasing, basic cleaning)
- TF-IDF feature extraction
- Supervised classification using Logistic Regression
- Command-line prediction script

# Project structure
  40-sentiment-analyzer/
├── README.md
├── requirements.txt
├── data/
│   └── sentiment_dataset.csv
├── models/
│   └── sentiment_model.joblib        # created after training
├── train.py
└── predict.py


## Tech Stack
- Python
- scikit-learn
- pandas
- joblib

## Setup

```bash
git clone <your-repo-url>
cd sentimentscope
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
