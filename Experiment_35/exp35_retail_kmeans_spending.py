import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("retail_transactions.csv")
features = ['TotalAmountSpent', 'VisitFrequency']

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Segment'] = kmeans.fit_predict(X_scaled)

print("Customer Segments based on Spending Patterns:")
print(df)

print("\nAverage Metrics per Segment:")
print(df.groupby('Segment')[features].mean().round(2))

# Scatter plot
plt.scatter(df['VisitFrequency'], df['TotalAmountSpent'], c=df['Segment'], cmap='viridis', s=100)
plt.title("Retail Customer Segments")
plt.xlabel("Visit Frequency")
plt.ylabel("Total Amount Spent ($)")
plt.colorbar(label='Segment')
plt.grid(True)
plt.show()
