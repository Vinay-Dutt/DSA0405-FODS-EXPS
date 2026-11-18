
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

age = np.array([23, 25, 28, 30, 32, 35, 38, 40, 42])
fat = np.array([15, 18, 20, 22, 24, 25, 27, 29, 30])

print("Mean Age:", np.mean(age))
print("Mean Body Fat:", np.mean(fat))

print("Median Age:", np.median(age))
print("Median Body Fat:", np.median(fat))

print("Standard Deviation of Age:", np.std(age, ddof=1))
print("Standard Deviation of Body Fat:", np.std(fat, ddof=1))

plt.boxplot([age, fat], tick_labels=["Age", "Body Fat"])
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()

plt.scatter(age, fat)
plt.xlabel("Age")
plt.ylabel("Body Fat")
plt.title("Age vs Body Fat")
plt.grid()
plt.show()

stats.probplot(age, dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")
plt.show()

stats.probplot(fat, dist="norm", plot=plt)
plt.title("Q-Q Plot of Body Fat")
plt.show()
