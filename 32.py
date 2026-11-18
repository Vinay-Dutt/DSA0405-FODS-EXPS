
import numpy as np
import matplotlib.pyplot as plt

size = np.array([1000, 1200, 1400, 1600, 1800, 2000])
price = np.array([20, 25, 28, 32, 36, 40])

slope, intercept = np.polyfit(size, price, 1)
pred = slope * size + intercept

mse = np.mean((price - pred) ** 2)
r2 = 1 - np.sum((price - pred) ** 2) / np.sum((price - np.mean(price)) ** 2)

print("Slope:", slope)
print("Intercept:", intercept)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

new_size = 1500
print("Predicted House Price:", slope * new_size + intercept)

plt.scatter(size, price, label="Actual Prices")
plt.plot(size, pred, color="red", label="Regression Line")
plt.xlabel("House Size")
plt.ylabel("House Price")
plt.title("House Price Prediction")
plt.legend()
plt.show()
