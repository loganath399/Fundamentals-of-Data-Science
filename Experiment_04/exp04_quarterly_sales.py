import numpy as np

sales_data = np.loadtxt(
    "quarterly_sales.csv", delimiter=",",
    skiprows=1, usecols=1
)

total_sales = np.sum(sales_data)

percentage_increase = (
    (sales_data[3] - sales_data[0]) / sales_data[0]
) * 100

print("Total Annual Sales:", total_sales)
print("Percentage Increase from Q1 to Q4:",
      round(percentage_increase, 2), "%")