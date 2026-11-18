
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

study = np.array([1, 2, 3, 4, 5, 6, 7, 8])
scores = np.array([35, 40, 50, 55, 65, 70, 80, 90])

r, p = pearsonr(study, scores)

print("Correlation:", r)
print("P-Value:", p)

if r > 0:
    print("Positive Correlation")
elif r < 0:
    print("Negative Correlation")
else:
    print("No Correlation")

plt.scatter(study, scores)
plt.plot(study, np.polyval(np.polyfit(study, scores, 1), study))
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Scores")
plt.title("Study Time vs Exam Scores")
plt.grid()
plt.show()

plt.bar(study, scores)
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Scores")
plt.title("Study Hours and Scores")
plt.show()
