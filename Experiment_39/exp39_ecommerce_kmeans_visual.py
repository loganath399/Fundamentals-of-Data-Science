import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load transaction data
df = pd.read_csv("ecommerce_buying_patterns.csv")
features = ['TotalAmountSpent', 'ItemsPurchased']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# Build K-Means clustering model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

print("Clustered Customer Data:")
print(df)

# Visualize clusters
plt.figure(figsize=(8, 5))
colors = ['red', 'blue', 'green']
for i in range(3):
    cluster_data = df[df['Cluster'] == i]
    plt.scatter(cluster_data['ItemsPurchased'], cluster_data['TotalAmountSpent'],
                color=colors[i], label=f'Segment {i}', s=90)

plt.title("Customer Buying Behavior Segments")
plt.xlabel("Number of Items Purchased")
plt.ylabel("Total Amount Spent ($)")
plt.legend()
plt.grid(True)
plt.show()
