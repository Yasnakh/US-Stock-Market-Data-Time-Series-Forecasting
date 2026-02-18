This project focuses on analyzing and forecasting financial time series data from selected S&P 500 stocks using classical statistical models.

The main objective was to:
-------------------------------------------------------------------------
1. Analyze stationarity of stock price data

2. Apply ARIMA, SARIMA, and GARCH models

3. Compare short-term and long-term forecasting performance

4. Evaluate volatility behavior in high-growth stocks

This project was developed as my Bachelor's Final Year Project.

-------------------------------------------------------------------------

Data Source: 
-------------------------------------------------------------------------
Yahoo Finance


-------------------------------------------------------------------------
Selected Stocks:
-------------------------------------------------------------------------
AAPL

MSFT

GOOG

AMZN

META

TSLA

AMD

NFLX

BRK-B

MINT

NVDA

PLTR



-------------------------------------------------------------------------
Forecast Horizons:
-------------------------------------------------------------------------
1 day

7 days

30 days

-------------------------------------------------------------------------
Forecasting Models
-------------------------------------------------------------------------
🔹 ARIMA

Used for non-seasonal time series forecasting.

🔹 SARIMA

Extended ARIMA with seasonal components (weekly seasonality s=7 for daily stock data).

🔹 GARCH

Used for modeling conditional volatility and short-term fluctuations.

-------------------------------------------------------------------------



Key Results:
-------------------------------------------------------------------------
1- Short-Term Forecasting (1-day)

  🔹GARCH performed best for high-volatility stocks (AAPL, MSFT)

  🔹ARIMA and SARIMA worked well for stable assets (MINT)

2- Medium-Term Forecasting (7-day)


🔹SARIMA outperformed ARIMA in presence of seasonal patterns

🔹GARCH performance decreased in longer horizons

3- Long-Term Forecasting (30-day)


🔹SARIMA provided better stability in seasonal data

🔹ARIMA struggled with long-term trends

🔹GARCH predictions flattened due to volatility mean reversion
