import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("monthly_sales.csv")

plt.bar(df["Month"], df["Sales"], color='green')

plt.title("Monthly Product Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()