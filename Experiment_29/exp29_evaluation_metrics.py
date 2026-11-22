import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load dataset
df = pd.read_csv("model_eval_dataset.csv")
print("Available columns:", list(df.columns))

# User input for feature names and target variable
feat_input = input("Enter feature names separated by commas (e.g., Feature1,Feature2,Feature3): ")
features = [f.strip() for f in feat_input.split(",")]
target = input("Enter target variable name (e.g., Target): ").strip()

X = df[features]
y = df[target]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Calculate evaluation metrics
print("\n--- Model Evaluation Metrics ---")
print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, average='weighted', zero_division=0):.4f}")
print(f"Recall   : {recall_score(y_test, y_pred, average='weighted', zero_division=0):.4f}")
print(f"F1-Score : {f1_score(y_test, y_pred, average='weighted', zero_division=0):.4f}")
