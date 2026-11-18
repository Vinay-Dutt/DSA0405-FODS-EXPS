
from scipy import stats

A = [20, 22, 25, 23, 21, 24, 26, 22]
B = [25, 27, 28, 26, 29, 30, 27, 28]

t, p = stats.ttest_ind(A, B)

print("Mean of A:", sum(A)/len(A))
print("Mean of B:", sum(B)/len(B))
print("T-Statistic:", t)
print("P-Value:", p)

if p < 0.05:
    print("Significant difference")
else:
    print("No significant difference")
