
import numpy as np
from scipy import stats

data = np.array([12, 15, 14, 10, 18, 16, 13, 17, 11, 14])

n = len(data)
mean = np.mean(data)
std = np.std(data, ddof=1)

ci = stats.t.interval(0.95, n-1, loc=mean, scale=stats.sem(data))

print("Sample Size:", n)
print("Point Estimate:", mean)
print("Standard Deviation:", std)
print("95% Confidence Interval:", ci)
