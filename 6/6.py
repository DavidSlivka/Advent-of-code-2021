
lantern_fish = []

with open('./input6.txt', 'r') as f:
    for record in f:
        lantern_fish = ''
        for i in record.split(','):
            lantern_fish += str(i)


def calc_fish(lantern_fish, days):
    counts = {'0': 0,
              '1': 0,
              '2': 0,
              '3': 0,
              '4': 0,
              '5': 0,
              '6': 0,
              '7': 0,
              '8': 0}

    for j in range(9):
        counts[str(j)] = lantern_fish.count(str(j))

    for day in range(days):
        side_var = counts['0']
        for j in range(8):
            counts[str(j)] = counts[str(j+1)]

        counts['8'] = side_var
        counts['6'] += side_var

    total = 0
    for i in range(9):
        total += counts[str(i)]

    return total


print(calc_fish(lantern_fish, 80))
print(calc_fish(lantern_fish, 256))