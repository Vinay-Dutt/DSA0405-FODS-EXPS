import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

text = " ".join(df['feedback']).lower()
words = re.findall(r'\b[a-z]+\b', text)

stop = ['the', 'and', 'is', 'a', 'to', 'of']
words = [w for w in words if w not in stop]

freq = Counter(words)

n = int(input("Enter N: "))
top = freq.most_common(n)

print(top)

plt.bar([x[0] for x in top], [x[1] for x in top])
plt.show()
