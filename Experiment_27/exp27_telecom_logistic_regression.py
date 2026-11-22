import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Load dataset
df = pd.read_csv("telecom_churn.csv")

# Features and target
X = df[['UsageMinutes', 'ContractMonths', 'Age']]
y = df['Churn']

# Train Logistic Regression model
model = make_pipeline(StandardScaler(), LogisticRegression())
model.fit(X, y)

# User input for new customer
usage = float(input("Enter Monthly Usage Minutes: "))
contract = int(input("Enter Contract Duration (months): "))
age = int(input("Enter Customer Age: "))

# Predict churn
input_data = pd.DataFrame([[usage, contract, age]], columns=['UsageMinutes', 'ContractMonths', 'Age'])
prediction = model.predict(input_data)

if prediction[0] == 1:
    print("Prediction: Customer will CHURN (1)")
else:
    print("Prediction: Customer will NOT churn (0)")
