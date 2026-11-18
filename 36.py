
import csv
import numpy as np
import matplotlib.pyplot as plt

data = [
    ["Date", "Close"],
    ["01-01-2026", 100],
    ["02-01-2026", 105],
    ["03-01-2026", 102],
    ["04-01-2026", 110],
    ["05-01-2026", 108],
    ["06-01-2026", 115],
    ["07-01-2026", 112]
]

with open("stock_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

prices = []

with open("stock_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        prices.append(float(row["Close"]))

prices = np.array(prices)

print("Average Price:", np.mean(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))
print("Price Range:", np.ptp(prices))
print("Standard Deviation:", np.std(prices))

plt.plot(prices, marker="o")
plt.title("Stock Price Variability")
plt.xlabel("Trading Day")
plt.ylabel("Closing Price")
plt.grid()
plt.show()
