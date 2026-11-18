
import numpy as np
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([
    [2018, 50000],
    [2019, 40000],
    [2020, 30000],
    [2021, 25000],
    [2022, 20000],
    [2023, 15000],
    [2017, 60000],
    [2016, 70000]
])

y = np.array([5, 6, 8, 10, 12, 15, 4, 3])

model = DecisionTreeRegressor(max_depth=3, random_state=42)
model.fit(X, y)

pred = model.predict(X)

print("Actual Prices:", y)
print("Predicted Prices:", pred)
print("Mean Squared Error:", mean_squared_error(y, pred))
print("R2 Score:", r2_score(y, pred))

new_car = np.array([[2022, 18000]])
print("Predicted Car Price:", model.predict(new_car)[0])

print("Decision Tree Rules:")
print(export_text(model, feature_names=["Year", "Kilometers"]))
