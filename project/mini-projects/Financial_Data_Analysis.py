import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"E:\Samsung\project\mini-projects\Stock_data.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Display basic information
print("Dataset Information:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Calculate Daily Returns
df['Daily_Return'] = df['Close'].pct_change()

# Calculate Moving Averages
df['MA_20'] = df['Close'].rolling(window=20).mean()
df['MA_50'] = df['Close'].rolling(window=50).mean()

# Plot Closing Price with Moving Averages
plt.figure()
plt.plot(df['Date'], df['Close'], label='Closing Price')
plt.plot(df['Date'], df['MA_20'], label='20-Day Moving Average')
plt.plot(df['Date'], df['MA_50'], label='50-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price Analysis')
plt.legend()
plt.show()

# Plot Daily Returns
plt.figure()
plt.plot(df['Date'], df['Daily_Return'])
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.title('Daily Return Analysis')
plt.show()

# Volume Analysis
plt.figure()
plt.bar(df['Date'], df['Total Trade Quantity'])
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Stock Trading Volume')
plt.show()
