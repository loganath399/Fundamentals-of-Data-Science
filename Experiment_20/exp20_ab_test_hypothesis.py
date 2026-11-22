import pandas as pd
import numpy as np
from scipy.stats import norm

# Read CSV file
df = pd.read_csv("ab_test.csv")

# Calculate conversions
a = df[df['Design'] == 'A']['Converted']
b = df[df['Design'] == 'B']['Converted']
n1, n2 = len(a), len(b)
p1, p2 = a.mean(), b.mean()

# Pooled proportion
p = (a.sum() + b.sum()) / (n1 + n2)

# Z-test
se = np.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
z = (p1 - p2) / se
p_value = 2 * norm.sf(abs(z))

print("Conversion Rate A:", p1)
print("Conversion Rate B:", p2)
print("Z Value:", z)
print("P Value:", p_value)

if p_value < 0.05:
    print("Significant difference")
else:
    print("No significant difference")
