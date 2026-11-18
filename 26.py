
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([[1000], [1200], [1500], [1800], [2000], [2200]])
y = np.array([20, 25, 30, 36, 40, 45])

model = LinearRegression()
model.fit(X, y)

pred = model.predict(X)

print("Predicted Prices:", pred)
print("Mean Squared Error:", mean_squared_error(y, pred))
print("R2 Score:", r2_score(y, pred))

area = np.array([[1600]])
print("Predicted House Price:", model.predict(area)[0])
