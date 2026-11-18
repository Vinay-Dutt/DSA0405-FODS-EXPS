from collections import Counter

f = open("sample_text.txt", "r")
text = f.read().lower()
f.close()

words = text.split()

freq = Counter(words)

print(freq)
