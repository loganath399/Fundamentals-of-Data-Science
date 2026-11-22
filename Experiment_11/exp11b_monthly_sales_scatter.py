import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("monthly_sales1.csv")

plt.scatter(df["Month"], df["Sales"], color='red', s=80)

plt.title("Monthly Product Sales - Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()