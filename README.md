Stock Sentiment Analysis
Overview
This project analyzes the relationship between financial news sentiment and stock price movements. Using historical stock price data combined with natural language processing on news headlines, the project explores how market sentiment impacts stock performance.

It includes three main tasks:

Task 1: Exploratory Data Analysis (EDA) of financial news data

Task 2: Technical Analysis of stock price trends

Task 3: Sentiment Analysis of news headlines using VADER

Project Structure
graphql
stock-sentiment-analysis/
├── notebooks/          # Jupyter notebooks for EDA, analysis, and visualization
├── raw_data/           # Source CSV files for news and stock prices
├── scripts/            # Utility scripts (if any)
├── tests/              # Unit and integration tests
├── requirements.txt    # Python dependencies
├── README.md           # This documentation file
Setup Instructions
Clone the repository:


git clone https://github.com/kalebab98/stock-sentiment-analysis.git
cd stock-sentiment-analysis
Create and activate a virtual environment (optional but recommended):


python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Run the notebooks in the notebooks/ folder to perform the analysis.

Usage
Start with notebooks/01_eda.ipynb for exploratory data analysis of news data.

Proceed to notebooks/02_technical_analysis.ipynb for stock price trends.

Use notebooks/03_sentiment_analysis.ipynb for applying sentiment scoring on headlines.

Visualizations and CSV outputs are saved in the respective notebook directories.


