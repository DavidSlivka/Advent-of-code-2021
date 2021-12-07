import numpy as np

with open('input7.txt', 'r') as f:
    for line in f:
        crab_list = [int(i) for i in line.split(',')]


crab_list = np.array(crab_list)
horizontal_pos = int(np.median(crab_list))
fuel_used = 0

for crab in crab_list:
    fuel_used += abs(crab - horizontal_pos)

print(fuel_used)

horizontal_pos = int(np.mean(crab_list))
fuel_used = 1000000000

for p in range(horizontal_pos - 1, horizontal_pos + 2):
    s = 0
    for crab in crab_list:
        s += abs(crab - p) * (abs(crab - p) + 1) // 2

    if s < fuel_used:
        fuel_used = s

print(fuel_used)
