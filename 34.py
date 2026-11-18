
import numpy as np
from collections import Counter

X = np.array([
    [25, 110, 180], [30, 120, 190],
    [35, 130, 200], [40, 140, 210],
    [45, 150, 220], [50, 160, 230],
    [28, 115, 185], [38, 135, 205],
    [48, 155, 225], [55, 165, 240],
    [26, 112, 182], [32, 125, 195],
    [42, 145, 215], [52, 162, 235],
    [29, 118, 188], [47, 152, 222]
], dtype=float)

y = np.array([
    "Good", "Good", "Good", "Bad",
    "Bad", "Bad", "Good", "Good",
    "Bad", "Bad", "Good", "Good",
    "Bad", "Bad", "Good", "Bad"
])

X_train = X[:12]
X_test = X[12:]
y_train = y[:12]
y_test = y[12:]

def predict(point):
    distances = np.linalg.norm(X_train - point, axis=1)
    nearest = np.argsort(distances)[:3]
    return Counter(y_train[nearest]).most_common(1)[0][0]

pred = np.array([predict(point) for point in X_test])

tp = np.sum((pred == "Good") & (y_test == "Good"))
tn = np.sum((pred == "Bad") & (y_test == "Bad"))
fp = np.sum((pred == "Good") & (y_test == "Bad"))
fn = np.sum((pred == "Bad") & (y_test == "Good"))

accuracy = (tp + tn) / len(y_test)
precision = tp / (tp + fp) if tp + fp else 0
recall = tp / (tp + fn) if tp + fn else 0
f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0

print("Actual:", y_test)
print("Predicted:", pred)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
