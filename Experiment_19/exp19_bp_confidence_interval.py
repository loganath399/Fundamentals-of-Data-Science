import pandas as pd
from scipy import stats

# Read CSV file
df = pd.read_csv("blood_pressure.csv")

# Calculate confidence intervals
for column in ['Drug', 'Placebo']:
    data = df[column].dropna()
    mean = data.mean()
    se = stats.sem(data)
    ci = stats.t.interval(
        0.95,
        len(data) - 1,
        loc=mean,
        scale=se
    )
    print(column)
    print("Mean:", mean)
    print("95% Confidence Interval:", ci)
