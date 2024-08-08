# Sentiment Analysis API

A Flask-based API for sentiment analysis using a fine-tuned BERT model. This API takes text input and predicts its sentiment as either "negative," "neutral," or "positive."

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview

This project provides a comprehensive framework for sentiment analysis, encompassing training and fine-tuning various models, including distilbert-base-uncased, Intel/dynamic_tinybert, microsoft/MiniLM-L12-H384-uncased, SVC (linear), and MultinomialNB. It includes scripts for training and fine-tuning these models, comparing their performance, and a Flask API for inference. The API allows for real-time sentiment analysis of textual data using the fine-tuned models, facilitating easy integration and deployment.

## Setup

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)
- An active internet connection for downloading model files and dependencies

### Installation

1. **Clone the Repository**
skip downloading larger files
   ```bash
   GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/sanskruti0ise/fin_news_sentiment.git
for the larger files
   ```bash
   git lfs pull
2. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m virtualenv venv
3. **Activate Virtual Environment**

   ```bash
   source venv/bin/activate

| Model                               | Negative Precision | Negative Recall | Negative F1-Score | Neutral Precision | Neutral Recall | Neutral F1-Score | Positive Precision | Positive Recall | Positive F1-Score | Accuracy | Macro Avg Precision | Macro Avg Recall | Macro Avg F1-Score | Weighted Avg Precision | Weighted Avg Recall | Weighted Avg F1-Score |
|-------------------------------------|--------------------|-----------------|-------------------|-------------------|----------------|------------------|--------------------|-----------------|-------------------|----------|---------------------|------------------|--------------------|----------------------|---------------------|----------------------|
| Intel/dynamic_tinybert              | 0.77               | 0.71            | 0.74              | 0.94              | 0.80           | 0.87             | 0.69               | 0.93            | 0.79              | 0.83     | 0.80                | 0.81             | 0.80               | 0.85                 | 0.83                | 0.83                 |
| distilbert-base-uncased             | 0.62               | 0.83            | 0.71              | 0.96              | 0.73           | 0.83             | 0.69               | 0.93            | 0.79              | 0.80     | 0.76                | 0.83             | 0.78               | 0.84                 | 0.80                | 0.80                 |
| microsoft/MiniLM-L12-H384-uncased   | 0.59               | 0.83            | 0.69              | 0.94              | 0.77           | 0.84             | 0.73               | 0.87            | 0.79              | 0.80     | 0.75                | 0.82             | 0.78               | 0.83                 | 0.80                | 0.81                 |
| SVC (linear, random state 42)       | 0.67               | 0.44            | 0.53              | 0.76              | 0.92           | 0.83             | 0.69               | 0.48            | 0.56              | 0.74     | 0.71                | 0.61             | 0.64               | 0.73                 | 0.74                | 0.72                 |
| MultinomialNB                       | 0.68               | 0.09            | 0.16              | 0.70              | 0.96           | 0.81             | 0.66               | 0.36            | 0.46              | 0.69     | 0.68                | 0.47             | 0.48               | 0.68                 | 0.69                | 0.64                 |

   source venv/bin/activate  # On Windows use: venv\Scripts\activate

   
