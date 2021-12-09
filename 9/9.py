import numpy

with open('./input9.txt', 'r') as f:
    map = [[int(elem) for elem in line.strip()] for line in f]

lowest = []


def get_points(line, elem):
    return ([line, abs(elem - 1)], [line, abs(elem + 1)], [abs(line + 1), elem], [abs(line - 1), elem])


for current_line in range(1, len(map)-1):
    for current_col in range(1, len(map[current_line])-1):
        if all(map[current_line][current_col] < map[x][y] for x, y in [(abs(current_line - 1), current_col), (current_line + 1, current_col), (current_line, abs(current_col - 1)), (current_line, current_col + 1)]):
            lowest.append(map[current_line][current_col])


for elem in range(1, len(map[0])-1):
    if all(map[0][elem] < map[x][y] for x, y in [(0, elem - 1), (0, elem + 1), (1, elem)]):
        lowest.append(map[0][elem])

for elem in range(1, len(map[99])-1):
    if all(map[99][elem] < map[x][y] for x, y in [(99, elem - 1), (99, elem + 1), (98, elem)]):
        lowest.append(map[99][elem])

for line in range(1, len(map)-1):
    if all(map[line][0] < map[x][y] for x, y in [(line-1, 0), (line+1, 0), (line, 1)]):
        lowest.append(map[line][0])

for line in range(1, len(map)-1):
    if all(map[line][99] < map[x][y] for x, y in [(line-1, 99), (line+1, 99), (line, 98)]):
        lowest.append(map[line][99])


print(sum(int(low)+1 for low in lowest))

field = []
for line in range(len(map)):
    for col in range(len(map[0])):
        if map[line][col] < 9:
            field.append([line, col])

basins = []


def get_basin(current_line, current_col):
    if [current_line, current_col] not in field:
        return 0
    field.remove([current_line, current_col])
    return 1 + sum(get_basin(x, y) for x, y in [[current_line - 1, current_col], [current_line + 1, current_col], [current_line, current_col - 1], [current_line, current_col + 1]])


while len(field) != 0:
    x, y = field[0]
    basins.append(get_basin(x, y))

print(numpy.prod(sorted(basins)[-3:]))



