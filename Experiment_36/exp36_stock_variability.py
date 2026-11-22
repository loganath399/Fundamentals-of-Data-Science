import pandas as pd
import numpy as np

# Read stock data
df = pd.read_csv("stock_prices.csv")
prices = df['ClosingPrice']

# Calculate variability metrics
mean_price = prices.mean()
std_dev = prices.std()
variance = prices.var()
price_range = prices.max() - prices.min()
df['DailyReturn'] = prices.pct_change() * 100

print("--- Stock Price Variability Analysis ---")
print(f"Mean Closing Price : ${mean_price:.2f}")
print(f"Standard Deviation : ${std_dev:.2f}")
print(f"Variance           : {variance:.2f}")
print(f"Price Range        : ${price_range:.2f} (Min: ${prices.min():.2f}, Max: ${prices.max():.2f})")
print(f"Avg Daily Return   : {df['DailyReturn'].mean():.2f}%")

if std_dev / mean_price < 0.05:
    print("Insight: Stock shows relatively low volatility and steady movement.")
else:
    print("Insight: Stock shows moderate to high volatility.")
