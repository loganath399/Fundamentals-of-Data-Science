import pandas as pd
from scipy import stats

# Read CSV file
df = pd.read_csv("customer_reviews.csv")
ratings = df['Rating'].dropna()

# Calculate mean
mean = ratings.mean()

# Calculate standard error
se = stats.sem(ratings)

# Calculate confidence interval
ci = stats.t.interval(
    0.95,
    len(ratings) - 1,
    loc=mean,
    scale=se
)

print("Mean Rating:", mean)
print("95% Confidence Interval:", ci)
