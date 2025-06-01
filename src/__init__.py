
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title="Stock Sentiment Analysis", layout="wide")


@st.cache_data
def load_data():
    df = pd.read_csv(r"https://drive.google.com/file/d/1oQP1TnpbBxCV9dc8d9obWqwuzxkl2qc3/view?usp=sharing", parse_dates=['date'])

    return df

df = load_data()


st.sidebar.title("🔍 Filter Options")
tickers = df['ticker'].unique().tolist()
selected_ticker = st.sidebar.selectbox("Select Ticker", tickers)
sentiments = ['positive', 'neutral', 'negative', 'all']
selected_sentiment = st.sidebar.radio("Sentiment Filter", sentiments)

if selected_sentiment != 'all':
    df = df[df['sentiment_label'] == selected_sentiment]

df_filtered = df[df['ticker'] == selected_ticker]


st.title("📈 News Sentiment vs Stock Price Movement")
st.markdown("""
This dashboard explores the relationship between financial news sentiment and stock price movement.


- Data: News headlines + yfinance stock prices
- Techniques: VADER sentiment, stock return analysis, correlation
""")


st.subheader("🧾 Data Preview")
st.dataframe(df_filtered[['date', 'headline', 'sentiment_label', 'Close', '1d_return']].sort_values(by='date', ascending=False).head(10))

# --- Section 3: Line Plot: Sentiment vs Price Over Time3 -
st.subheader(f"📉 Stock Price vs Sentiment Over Time ({selected_ticker})")

fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(data=df_filtered, x='date', y='Close', ax=ax, label='Close Price')
sns.scatterplot(data=df_filtered, x='date', y='Close', hue='sentiment_label', palette='Set2', ax=ax)
plt.legend()
st.pyplot(fig)

# --- Section 4: Bar Plot: Average Return by Sentiment ---
st.subheader("📊 Average Return by Sentiment")
avg_returns = df.groupby('sentiment_label')['1d_return'].mean().reset_index()

fig2, ax2 = plt.subplots()
sns.barplot(data=avg_returns, x='sentiment_label', y='1d_return', palette='coolwarm', ax=ax2)
ax2.set_ylabel("Avg 1-Day Return")
st.pyplot(fig2)


