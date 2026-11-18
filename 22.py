
import numpy as np
from scipy import stats

ratings = np.array([5, 4, 3, 5, 4, 2, 5, 4, 3, 5])

print("Total Reviews:", len(ratings))
print("Average Rating:", np.mean(ratings))
print("Median Rating:", np.median(ratings))
print("Minimum Rating:", np.min(ratings))
print("Maximum Rating:", np.max(ratings))
print("Standard Deviation:", np.std(ratings, ddof=1))

ci = stats.t.interval(
    0.95,
    len(ratings)-1,
    loc=np.mean(ratings),
    scale=stats.sem(ratings)
)

print("95% Confidence Interval:", ci)

print("Positive Reviews:", np.sum(ratings >= 4))
print("Negative Reviews:", np.sum(ratings <= 2))
