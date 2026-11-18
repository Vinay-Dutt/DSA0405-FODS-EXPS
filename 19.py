
import numpy as np
from scipy import stats

drug = np.array([10, 12, 11, 13, 14, 12, 15, 11, 13, 14])
placebo = np.array([5, 6, 7, 5, 8, 6, 7, 5, 6, 8])

drug_ci = stats.t.interval(0.95, len(drug)-1, loc=np.mean(drug), scale=stats.sem(drug))
placebo_ci = stats.t.interval(0.95, len(placebo)-1, loc=np.mean(placebo), scale=stats.sem(placebo))

print("Drug Mean:", np.mean(drug))
print("Drug 95% Confidence Interval:", drug_ci)

print("Placebo Mean:", np.mean(placebo))
print("Placebo 95% Confidence Interval:", placebo_ci)
