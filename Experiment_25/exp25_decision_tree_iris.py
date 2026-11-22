from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load Iris dataset
iris = load_iris()

# Features and target
X = iris.data
y = iris.target

# Train Decision Tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Get user input
sl = float(input("Enter Sepal Length: "))
sw = float(input("Enter Sepal Width: "))
pl = float(input("Enter Petal Length: "))
pw = float(input("Enter Petal Width: "))

# Predict species
prediction = model.predict([[sl, sw, pl, pw]])
print("Predicted Iris Species:", iris.target_names[prediction[0]])
