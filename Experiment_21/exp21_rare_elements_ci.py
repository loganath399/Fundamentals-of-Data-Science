import numpy as np
import pandas as pd
from scipy import stats
import math

# Read CSV file
df = pd.read_csv("rare_elements.csv")
data = df['Concentration'].dropna().values

# User inputs
n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (e.g. 95): "))
precision = float(input("Enter desired precision: "))

# Select sample
sample = data[:n]

# Calculate statistics
mean = np.mean(sample)
std = np.std(sample, ddof=1)

# Confidence interval
alpha = 1 - confidence / 100
t_value = stats.t.ppf(1 - alpha / 2, n - 1)
margin = t_value * std / np.sqrt(n)
lower = mean - margin
upper = mean + margin

# Required sample size (normal approximation)
z = stats.norm.ppf(1 - alpha / 2)
required_n = math.ceil((z * std / precision) ** 2)

print("Sample Mean:", mean)
print("Confidence Interval:", (lower, upper))
print("Margin of Error:", margin)
print("Required Sample Size:", required_n)
