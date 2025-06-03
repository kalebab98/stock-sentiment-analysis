# 🧪 Task 1: Exploratory Data Analysis (EDA)

## 🔍 Overview

In this notebook, we perform exploratory data analysis on the raw financial news dataset to understand:

- How frequently articles are published
- Which publishers are most active
- How article frequency changes over time
- Ticker-level mentions and basic structure of the dataset

This step lays the foundation for sentiment scoring and stock-sentiment correlation later in the project.

---

## 📁 Input Data

**Source:** `../data/raw_analyst_ratings.csv`

This dataset contains financial news headlines along with metadata.

| Column | Description |
|--------|-------------|
| `headline` | Title of the news article |
| `url` | Link to the article |
| `publisher` | Name of the publishing source |
| `date` | Timestamp of publication |
| `stock` | Associated stock ticker (e.g., AAPL, TSLA, etc.) |

---

## 📊 Key Analyses

1. **Article Volume Over Time**  
   - Time series plot of articles published per day

2. **Top Publishers**  
   - Bar chart showing article count by publisher

3. **Stock Mentions**  
   - Analysis of how often each stock is mentioned

4. **Date Parsing & Formatting**  
   - Converted string timestamps into datetime objects with timezone handling

---

## 📤 Outputs

| File | Description |
|------|-------------|
| `publisher_article_counts.csv` | Count of articles published by each publisher |
| `articles_per_day.csv` | Daily count of articles for time series analysis |

All outputs are saved to the `notebooks/` folder and used in later tasks (e.g., sentiment analysis and stock correlation).

---


