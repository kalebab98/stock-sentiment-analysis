# 📈 Stock Sentiment Analysis
**Streamlit link : https://stock-sentiment-analysis-ezp794a4tpsxw46e8mdt89.streamlit.app/**


**🔍 Overview**
This project investigates the relationship between financial news sentiment and stock price movements. By combining historical stock price data with natural language processing (NLP) on news headlines, we analyze how market sentiment influences stock performance.

**The project is divided into three key tasks:**
Task 1: Exploratory Data Analysis (EDA) of financial news data

Task 2: Technical Analysis of stock price trends

Task 3: Sentiment Analysis of news headlines using VADER


**🚀 Setup Instructions**
cd stock-sentiment-analysis
Create and activate a virtual environment (recommended):

## 💻 Task Notebooks

| Task | Notebook | Description |
|------|----------|-------------|
| Task 1 | [`01_eda.ipynb`](notebooks/01_eda.ipynb) | Load and explore news data: article counts, publisher trends |
| Task 2 | [`02_AAPL_Analysis.ipynb,AMZN_Analysis.ipynb,GOOG_Analysis.....`] | Analyze stock price trends with moving averages |
| Task 3 | [`03_sentiment_analysis.ipynb`](notebooks/03_sentiment_analysis.ipynb) | Run VADER sentiment analysis on headlines |


**🎯 Usage Guide**

**-Begin with notebooks/01_eda.ipynb:**
-Explore and clean the financial news data.

-Continue to notebooks/02_technical_analysis.ipynb:
-Analyze historical stock price trends and technical indicators.

-Proceed to notebooks/03_sentiment_analysis.ipynb:
-Perform sentiment scoring on news headlines using VADER and link sentiment to stock movement.

-All visualizations and CSV outputs are saved in the corresponding notebook directories for easy access.

**📦 Data Sources**
-News Headlines:
-File: data/raw_analyst_ratings.csv
-Format: headline, publisher, date, stock, url

-Stock Prices:
-Folder: data/yfinance_data/
=Files: One CSV per ticker (e.g., AAPL, TSLA, GOOG, etc.)
-Format: Date, Open, Close, Volume, etc.


**🧠 Requirements**
Make sure requirements.txt includes (or manually install):

-pandas
-numpy
-matplotlib
-seaborn
-vaderSentiment
-yfinance
-ta-lib
-jupyter

**On macOS/Linux:**

python -m venv .venv
source .venv/bin/activate
On Windows:

**powershell**

python -m venv .venv
.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt
Run the notebooks inside the notebooks/ directory to perform the analyses.
Flask

**🌐 Live Demo**
-You can view the interactive dashboard here (if deployed):
**Streamlit link : https://stock-sentiment-analysis-ezp794a4tpsxw46e8mdt89.streamlit.app/**
-[🔗 Streamlit App
](https://stock-sentiment-analysis-ezp794a4tpsxw46e8mdt89.streamlit.app/)



![image](https://github.com/user-attachments/assets/0e718dd8-6f65-440b-9e9f-2025a529bfde)


