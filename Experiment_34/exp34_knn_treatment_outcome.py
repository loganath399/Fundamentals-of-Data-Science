import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load dataset (Gender: 1=Male, 0=Female)
df = pd.read_csv("medical_treatment_knn.csv")
features = ['Age', 'Gender', 'BloodPressure', 'Cholesterol']
X = df[features]
y = df['Outcome']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train KNN Classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# Predict on test set
y_pred = knn.predict(X_test_scaled)

# Evaluate performance
print("--- KNN Classification Performance ---")
print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, pos_label='Good', zero_division=0):.4f}")
print(f"Recall   : {recall_score(y_test, y_pred, pos_label='Good', zero_division=0):.4f}")
print(f"F1-Score : {f1_score(y_test, y_pred, pos_label='Good', zero_division=0):.4f}")

# Display test predictions
results = X_test.copy()
results['Actual'] = y_test
results['Predicted'] = y_pred
print("\nTest Set Predictions:")
print(results)
