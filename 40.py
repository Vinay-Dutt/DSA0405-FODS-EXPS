
import csv
import matplotlib.pyplot as plt
from collections import Counter

players = [
    ["Name", "Age", "Position", "Goals", "Salary"],
    ["John", 25, "Forward", 30, 50000],
    ["David", 28, "Midfielder", 15, 40000],
    ["Mike", 23, "Defender", 5, 30000],
    ["Alex", 27, "Forward", 25, 55000],
    ["Robert", 30, "Midfielder", 18, 45000],
    ["James", 24, "Forward", 22, 60000],
    ["Daniel", 29, "Defender", 8, 35000],
    ["Peter", 32, "Goalkeeper", 2, 25000]
]

with open("players.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(players)

with open("players.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

top_goals = sorted(data, key=lambda x: int(x["Goals"]), reverse=True)[:5]
top_salary = sorted(data, key=lambda x: int(x["Salary"]), reverse=True)[:5]

print("Top 5 Players by Goals:")
for p in top_goals:
    print(p["Name"], p["Goals"])

print("\nTop 5 Players by Salary:")
for p in top_salary:
    print(p["Name"], p["Salary"])

ages = [int(p["Age"]) for p in data]
avg_age = sum(ages) / len(ages)

print("\nAverage Age:", avg_age)
print("Players Above Average Age:")

for p in data:
    if int(p["Age"]) > avg_age:
        print(p["Name"])

positions = Counter(p["Position"] for p in data)

plt.bar(positions.keys(), positions.values())
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.title("Players by Position")
plt.show()
