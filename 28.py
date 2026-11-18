
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = np.array([
    [20, 20], [22, 25], [25, 30],
    [40, 50], [42, 55], [45, 60],
    [60, 80], [65, 85], [70, 90]
])

model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(X)

labels = model.labels_

print("Cluster Labels:", labels)
print("Cluster Centers:", model.cluster_centers_)

plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(model.cluster_centers_[:, 0],
            model.cluster_centers_[:, 1],
            marker="X", s=200)
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()
