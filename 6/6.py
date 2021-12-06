with open('./input6.txt', 'r') as f:
    lanternfish = ''
    for record in f:
        for i in record.split(','):
            lanternfish += str(i)


def calc_fish(lanternfish, days):
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
        counts[str(j)] = lanternfish.count(str(j))

    for day in range(days):
        fish_to_create_new = counts['0']
        for j in range(8):
            counts[str(j)] = counts[str(j+1)]

        counts['8'] = fish_to_create_new
        counts['6'] += fish_to_create_new

    total = 0
    for i in range(9):
        total += counts[str(i)]

    return total


print(calc_fish(lanternfish, 80))
print(calc_fish(lanternfish, 256))