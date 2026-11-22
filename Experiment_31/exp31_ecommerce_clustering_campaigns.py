import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("customer_behavior.csv")
features = ['Age', 'AnnualIncome', 'BrowsingMinutes', 'TotalPurchases']

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

print("Customer Segments Summary:")
print(df.groupby('Cluster')[features].mean().round(2))

# Visualize segments
plt.figure(figsize=(8, 5))
for cluster_id in sorted(df['Cluster'].unique()):
    subset = df[df['Cluster'] == cluster_id]
    plt.scatter(subset['AnnualIncome'], subset['TotalPurchases'], label=f'Segment {cluster_id}', s=80)

plt.title("Customer Segmentation: Annual Income vs Total Purchases")
plt.xlabel("Annual Income ($)")
plt.ylabel("Total Purchases")
plt.legend()
plt.grid(True)
plt.show()
