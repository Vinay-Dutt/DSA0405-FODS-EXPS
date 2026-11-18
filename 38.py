
import numpy as np

cities = {
    "Chennai": [30, 32, 35, 31, 29],
    "Delhi": [20, 25, 30, 18, 22],
    "Mumbai": [28, 29, 30, 31, 28],
    "Bangalore": [22, 24, 25, 23, 21]
}

ranges = {}
std_values = {}

for city, temp in cities.items():
    print("\nCity:", city)
    print("Mean Temperature:", np.mean(temp))
    print("Standard Deviation:", np.std(temp))
    print("Temperature Range:", np.ptp(temp))

    ranges[city] = np.ptp(temp)
    std_values[city] = np.std(temp)

print("\nHighest Temperature Range:", max(ranges, key=ranges.get))
print("Most Consistent City:", min(std_values, key=std_values.get))
