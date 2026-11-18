
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

control = np.array([20, 22, 21, 19, 23, 20, 22, 21])
treatment = np.array([25, 27, 26, 24, 28, 25, 27, 26])

t, p = stats.ttest_ind(control, treatment)

print("Control Mean:", np.mean(control))
print("Treatment Mean:", np.mean(treatment))
print("T-Statistic:", t)
print("P-Value:", p)

if p < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Accept Null Hypothesis")

plt.boxplot([control, treatment], tick_labels=["Control", "Treatment"])
plt.title("Hypothesis Testing")
plt.show()
