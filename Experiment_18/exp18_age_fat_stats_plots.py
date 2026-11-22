import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Read CSV file
df = pd.read_csv("age_fat.csv")

# Statistical calculations
print("Mean:\n", df.mean())
print("\nMedian:\n", df.median())
print("\nStandard Deviation:\n", df.std())

# Boxplots
df[['Age', 'Fat']].plot(
    kind='box',
    subplots=True,
    layout=(1, 2),
    figsize=(8, 4)
)
plt.show()

# Scatter plot
plt.scatter(df['Age'], df['Fat'])
plt.title("Age vs Body Fat")
plt.xlabel("Age")
plt.ylabel("Body Fat (%)")
plt.grid()
plt.show()

# Q-Q plots
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")

plt.subplot(1, 2, 2)
stats.probplot(df['Fat'], dist="norm", plot=plt)
plt.title("Q-Q Plot of Body Fat")
plt.tight_layout()
plt.show()
