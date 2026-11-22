import numpy as np

sales_data = np.loadtxt(
    "product_sales.csv", delimiter=",", skiprows=1
)

average_price = np.mean(sales_data)

print("Average Price of All Products:", round(average_price, 2))