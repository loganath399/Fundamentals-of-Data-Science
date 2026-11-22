import pandas as pd

# Read customer dataset
df = pd.read_csv("customer_data.csv")

# Calculate age frequency
frequency = df["Age"].value_counts().sort_index()

# Display result
print("Customer Age Frequency Distribution")
print("------------------------------------")
print(frequency)