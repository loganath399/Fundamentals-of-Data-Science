import numpy as np

house_data = np.loadtxt(
    "house_data.csv", delimiter=",", skiprows=1
)

bedrooms = house_data[:, 0]
sale_prices = house_data[:, 2]

selected_prices = sale_prices[bedrooms > 4]

average_price = np.mean(selected_prices)

print("Average Sale Price of Houses with More Than 4 Bedrooms:",
      round(average_price, 2))