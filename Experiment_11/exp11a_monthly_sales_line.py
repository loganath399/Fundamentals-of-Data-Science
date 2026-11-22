import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("monthly_sales1.csv")

plt.plot(df["Month"], df["Sales"], marker='o')

plt.title("Monthly Product Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()