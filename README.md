## Task 2: Technical Indicator Analysis using TA-Lib

In this task, we used historical stock data to generate key technical indicators that help assess market trends and momentum.

### Process:
- Loaded historical data for AAPL, AMZN, GOOG, META, MSFT, NVDA, and TSLA from `.csv` files.
- Parsed dates and sorted the data for each stock.
- Used [TA-Lib](https://github.com/TA-Lib/ta-lib-python) to calculate:
  - **Simple Moving Average (SMA 20)**: A short-term trend indicator.
  - **Relative Strength Index (RSI 14)**: Identifies overbought/oversold conditions.
  - **MACD (12, 26, 9)**: Detects momentum shifts via convergence/divergence of moving averages.
- Visualized indicators for AAPL using `matplotlib`:
  - Line plot of Close price with 20-day SMA
  - RSI chart with overbought/oversold reference lines
  - MACD and Signal line comparison

These features will be essential for correlation analysis in Task 3, where we integrate sentiment data with technical signals.

All processed stock data is ready for merging and analysis.
