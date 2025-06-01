# 📊 Task 3: Stock Sentiment Streamlit Dashboard

## Overview

This task implements a **Streamlit-based dashboard** that visualizes the relationship between financial news sentiment and stock price movement. It uses preprocessed data and focuses solely on building an interactive frontend.

---

## 🚀 Features

- Interactive dashboard built with **Streamlit**
- Filters for stock ticker and sentiment
- Time-series plot: **Stock Close Price vs Sentiment Labels**
- Bar chart: **Average 1-Day Return by Sentiment**
- Data preview section

---

## 📁 Files

- `notebooks/app.py`: Main Streamlit app file
- `requirements.txt`: Lists required Python packages
- `src/__init__.py`: Logic for loading and processing data
- `notebooks/processed_news_sentiment.csv`: Data source (not included in repo due to size)

---

## 🛠️ Tech Stack

- Streamlit
- Pandas
- Seaborn
- Matplotlib
- Gdown (optional, for fetching Google Drive CSVs)

---

## 📦 Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/kalebab98/stock-sentiment-analysis.git
    cd stock-sentiment-analysis
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run Streamlit app:
    ```bash
    streamlit run notebooks/app.py
    ```

---

## 🌐 Live App

> Hosted on Streamlit Cloud (add link when available)

---

## 🔍 Insights

- Real-time filtering enables interactive analysis of sentiment trends
- Visuals help highlight how sentiment may influence short-term price movement
- Encourages data-driven observation of news impact on the market
