import pandas as pd

order_data = pd.read_csv("orders.csv")
order_data["Order_Date"] = pd.to_datetime(order_data["Order_Date"])

print("Orders per customer:")
print(order_data.groupby("Customer_ID").size())

print("\nAverage quantity per product:")
print(order_data.groupby("Product")["Quantity"].mean())

print("\nEarliest order:", order_data["Order_Date"].min())
print("Latest order:", order_data["Order_Date"].max())