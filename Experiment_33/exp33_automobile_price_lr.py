import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("automobile_prices.csv")
features = ['EngineSize', 'Horsepower', 'FuelEfficiency']
X = df[features]
y = df['Price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Fit Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"Mean Absolute Error (MAE): ${mean_absolute_error(y_test, y_pred):,.2f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.4f}")

# Feature importance insights
print("\n--- Marketing Insights: Influential Factors ---")
for feat, coef in zip(features, model.coef_):
    print(f"{feat}: Coefficient = {coef:.2f}")
