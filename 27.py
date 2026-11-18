
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = np.array([
    [1, 20], [2, 30], [3, 40], [4, 50],
    [5, 60], [6, 70], [7, 80], [8, 90],
    [2, 25], [3, 35], [6, 75], [7, 85]
])

y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Predicted Churn:", pred)
print("Actual Churn:", y_test)
print("Accuracy:", accuracy_score(y_test, pred))

new_customer = np.array([[5, 65]])
print("New Customer Prediction:", model.predict(new_customer))
