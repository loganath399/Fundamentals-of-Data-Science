import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("housing_prices.csv")

# Features and target
X = df[['Area', 'Bedrooms', 'LocationScore']]
y = df['Price']

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# User input for new house
area = float(input("Enter Area (sq ft): "))
bedrooms = int(input("Enter Number of Bedrooms: "))
location = float(input("Enter Location Score (1-10): "))

# Predict price
input_data = pd.DataFrame([[area, bedrooms, location]], columns=['Area', 'Bedrooms', 'LocationScore'])
predicted_price = model.predict(input_data)

print(f"Predicted House Price: ${predicted_price[0]:,.2f}")
