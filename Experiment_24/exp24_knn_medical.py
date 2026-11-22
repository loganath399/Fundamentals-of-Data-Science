import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Read CSV file
df = pd.read_csv("patients.csv")

# Separate features and target
X = df[['Fever', 'Cough', 'Fatigue']]
y = df['Condition']

# Train KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Get user input
fever = int(input("Enter Fever (0/1): "))
cough = int(input("Enter Cough (0/1): "))
fatigue = int(input("Enter Fatigue (0/1): "))
k = int(input("Enter K value: "))

# Update K value
model.set_params(n_neighbors=k)

# Prediction
input_df = pd.DataFrame([[fever, cough, fatigue]], columns=['Fever', 'Cough', 'Fatigue'])
prediction = model.predict(input_df)

if prediction[0] == 1:
    print("Patient has the medical condition")
else:
    print("Patient does not have the medical condition")
