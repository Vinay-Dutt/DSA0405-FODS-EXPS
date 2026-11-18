
import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [100, 10],
    [120, 12],
    [150, 15],
    [180, 18],
    [200, 20],
    [220, 22]
], dtype=float)

price = np.array([5, 6, 8, 10, 12, 14], dtype=float)

X1 = np.column_stack((np.ones(len(X)), X))
coef = np.linalg.lstsq(X1, price, rcond=None)[0]

pred = X1 @ coef

mse = np.mean((price - pred) ** 2)
r2 = 1 - np.sum((price - pred) ** 2) / np.sum((price - np.mean(price)) ** 2)

print("Intercept:", coef[0])
print("Engine Size Coefficient:", coef[1])
print("Horsepower Coefficient:", coef[2])
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

new_car = np.array([1, 160, 16])
print("Predicted Car Price:", new_car @ coef)

plt.scatter(price, pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Car Price Prediction")
plt.show()
