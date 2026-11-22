import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("ecommerce_customers.csv")
features = ['AnnualSpend', 'PurchaseFrequency', 'AvgOrderValue']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# Train K-Means model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Segment'] = kmeans.fit_predict(X_scaled)

print("Existing Customer Segments Overview:")
print(df.groupby('Segment')[features].mean().round(2))

# User input for new customer
spend = float(input("\nEnter Annual Spend ($): "))
freq = float(input("Enter Purchase Frequency (orders/year): "))
aov = float(input("Enter Average Order Value ($): "))

new_cust = pd.DataFrame([[spend, freq, aov]], columns=features)
new_cust_scaled = scaler.transform(new_cust)
cluster = kmeans.predict(new_cust_scaled)[0]

print(f"The new customer belongs to Segment: {cluster}")
