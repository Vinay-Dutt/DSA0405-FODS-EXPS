
import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [20, 2000], [22, 2500], [25, 3000],
    [40, 8000], [42, 8500], [45, 9000],
    [60, 15000], [65, 16000], [70, 18000]
], dtype=float)

k = 3
centers = X[[0, 3, 6]]

for i in range(20):
    distances = np.linalg.norm(X[:, None] - centers, axis=2)
    labels = np.argmin(distances, axis=1)
    new_centers = np.array([
        X[labels == j].mean(axis=0) if np.any(labels == j) else centers[j]
        for j in range(k)
    ])
    if np.allclose(centers, new_centers):
        break
    centers = new_centers

print("Customer Groups:", labels)
print("Cluster Centers:")
print(centers)

plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centers[:, 0], centers[:, 1], marker="X", s=200)
plt.xlabel("Age")
plt.ylabel("Annual Spending")
plt.title("Customer Segmentation")
plt.show()
