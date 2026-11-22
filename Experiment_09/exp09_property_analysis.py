import pandas as pd

property_data = pd.read_csv("properties.csv")

print("Average price by location:")
print(property_data.groupby("Location")["Price"].mean())

print("\nProperties with more than 4 bedrooms:")
print(property_data[property_data["Bedrooms"] > 4])

print("\nProperty with the largest area:")
print(property_data.loc[property_data["Area"].idxmax()])