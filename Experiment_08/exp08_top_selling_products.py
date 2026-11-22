import pandas as pd

sales_data = pd.read_csv("sales.csv")
sales_data["Date"] = pd.to_datetime(sales_data["Date"])

end_date = pd.Timestamp("2026-10-21")
start_date = end_date - pd.DateOffset(months=1)

monthly_sales = sales_data[
    (sales_data["Date"] > start_date) &
    (sales_data["Date"] <= end_date)
]

top5 = (
    monthly_sales.groupby("Product")["Quantity_Sold"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("Top 5 Best-Selling Products:")
print(top5)