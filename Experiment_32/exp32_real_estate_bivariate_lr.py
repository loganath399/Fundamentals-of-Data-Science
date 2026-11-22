import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("real_estate_bivariate.csv")

# Bivariate analysis: Correlation between HouseSize and Price
correlation = df['HouseSize'].corr(df['Price'])
print(f"Correlation between HouseSize and Price: {correlation:.4f}")

X = df[['HouseSize']]
y = df['Price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Build Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict & Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Intercept: {model.intercept_:.2f}")
print(f"Slope (Price per sq ft): {model.coef_[0]:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2 Score): {r2:.4f}")

# Plot regression line
plt.scatter(df['HouseSize'], df['Price'], color='blue', label='Actual Data')
plt.plot(df['HouseSize'], model.predict(X), color='red', label='Regression Line')
plt.title("Bivariate Analysis: House Size vs Price")
plt.xlabel("House Size (sq ft)")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.show()
