from collections import Counter

reviews = ["good product", "very good product", "bad product"]

words = " ".join(reviews).lower().split()

print(Counter(words))
