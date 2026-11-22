import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("monthly_sales.csv")

months = data["Month"]
sales = data["Sales"]

# Line plot
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

# Bar plot
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
