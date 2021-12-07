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


horizontal_pos = int(round(np.mean(crab_list)))-1
fuel_used = 0

for crab in crab_list:
    move = abs(crab - horizontal_pos)
    for i in range(1, move + 1):
        fuel_used += i

print(fuel_used)
