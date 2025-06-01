import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stock Sentiment Analysis", layout="wide")

@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?export=download&id=1oQP1TnpbBxCV9dc8d9obWqwuzxkl2qc3"
    try:
        df = pd.read_csv(url)
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
        else:
            st.error("⚠️ 'date' column not found in the CSV.")
        return df
    except Exception as e:
        st.error(f"❌ Failed to load data: {e}")
        return pd.DataFrame()

df = load_data()

if df.empty or 'ticker' not in df.columns:
    st.stop()

st.sidebar.title("🔍 Filter Options")
tickers = df['ticker'].dropna().unique().tolist()
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

# Section: Data Preview
st.subheader("🧾 Data Preview")
columns_to_show = ['date', 'headline', 'sentiment_label', 'Close', '1d_return']
available_columns = [col for col in columns_to_show if col in df_filtered.columns]
st.dataframe(df_filtered[available_columns].sort_values(by='date', ascending=False).head(10))

# Section: Line Plot
if 'Close' in df_filtered.columns and 'date' in df_filtered.columns:
    st.subheader(f"📉 Stock Price vs Sentiment Over Time ({selected_ticker})")
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=df_filtered, x='date', y='Close', ax=ax, label='Close Price')
    sns.scatterplot(data=df_filtered, x='date', y='Close', hue='sentiment_label', palette='Set2', ax=ax)
    ax.legend()
    st.pyplot(fig)
else:
    st.warning("Missing 'Close' or 'date' column for plotting.")

# Section: Bar Plot
if '1d_return' in df.columns and 'sentiment_label' in df.columns:
    st.subheader("📊 Average Return by Sentiment")
    avg_returns = df.groupby('sentiment_label')['1d_return'].mean().reset_index()
    fig2, ax2 = plt.subplots()
    sns.barplot(data=avg_returns, x='sentiment_label', y='1d_return', palette='coolwarm', ax=ax2)
    ax2.set_ylabel("Avg 1-Day Return")
    st.pyplot(fig2)
else:
    st.warning("Missing '1d_return' or 'sentiment_label' for bar plot.")
