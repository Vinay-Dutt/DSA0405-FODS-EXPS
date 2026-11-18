
import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [1000, 2], [1500, 3], [2000, 4],
    [5000, 6], [5500, 7], [6000, 8],
    [9000, 12], [9500, 15], [10000, 18]
], dtype=float)

centers = X[[0, 3, 6]]

for i in range(20):
    distances = np.linalg.norm(X[:, None] - centers, axis=2)
    labels = np.argmin(distances, axis=1)

    new_centers = np.array([
        X[labels == j].mean(axis=0) if np.any(labels == j) else centers[j]
        for j in range(3)
    ])

    if np.allclose(centers, new_centers):
        break

    centers = new_centers

print("Cluster Labels:", labels)
print("Cluster Centers:")
print(centers)

plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centers[:, 0], centers[:, 1], marker="X", s=200)
plt.xlabel("Amount Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Clustering")
plt.show()
