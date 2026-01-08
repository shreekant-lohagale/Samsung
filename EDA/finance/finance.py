import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", start = "2020-01-01", end = "2021-01-01")
print(data.head())
# check columns
print(data.columns)

# plot closing price
plt.figure(figsize=(10,6))
plt.plot(data.index, data['Close'], label='AAPL Close Price')
plt.title("AAPL Closing Price in 2020")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()

#Daily returns
data['Daily Return'] = data['Close'].pct_change()
plt.figure(figsize=(10,6))
plt.plot(data.index, data['Daily Return'], label='AAPL Daily Return', color='orange')
plt.title("AAPL Daily Returns in 2020")
plt.xlabel("Date")
plt.ylabel("Daily Return")
plt.legend()
plt.grid(True)
plt.show()