import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Load dataset (BrandCode: 0=Economy, 1=Standard, 2=Premium, 3=Luxury; EngineType: 0=Petrol, 1=Hybrid, 2=Electric)
df = pd.read_csv("used_cars.csv")
feature_names = ['Mileage', 'Age', 'BrandCode', 'EngineType']
X = df[feature_names]
y = df['Price']

# Train CART Regression Tree
cart_model = DecisionTreeRegressor(max_depth=4, random_state=42)
cart_model.fit(X, y)

# User input for new car
mileage = float(input("Enter Car Mileage (miles): "))
age = int(input("Enter Car Age (years): "))
brand = int(input("Enter Brand Code (0=Economy, 1=Standard, 2=Premium, 3=Luxury): "))
engine = int(input("Enter Engine Type (0=Petrol, 1=Hybrid, 2=Electric): "))

new_car = pd.DataFrame([[mileage, age, brand, engine]], columns=feature_names)
predicted_price = cart_model.predict(new_car)[0]

print(f"\nPredicted Used Car Price: ${predicted_price:,.2f}")

# Display Decision Path
print("\nDecision Path:")
tree = cart_model.tree_
node_indicator = cart_model.decision_path(new_car)
leaf_id = cart_model.apply(new_car)[0]
node_index = node_indicator.indices[node_indicator.indptr[0]:node_indicator.indptr[1]]

for node_id in node_index:
    if leaf_id == node_id:
        print(f" -> Leaf Node {node_id}: Predicted Value = ${tree.value[node_id][0][0]:,.2f}")
    else:
        feat_idx = tree.feature[node_id]
        threshold = tree.threshold[node_id]
        val = new_car.iloc[0, feat_idx]
        sign = "<=" if val <= threshold else ">"
        print(f" -> Node {node_id}: {feature_names[feat_idx]} ({val}) {sign} {threshold:.2f}")
