
def get_grid_and_coordinates():
    coordinates = []
    count = 0

    with open('./input5.txt', 'r') as f:
        for line in f:
            l = (line.rstrip('\n').split(' -> '))
            coordinates.append([])
            for coords in l:
                co = [int(c) for c in coords.split(',')]
                coordinates[count].append(co)
            count += 1

    map = []
    count = 0
    for i in range(1000):
        map.append([])
        for j in range(1000):
            map[count].append(0)
        count += 1

    return coordinates, map


def get_final_count(map):
    final_count = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] >= 2:
                final_count += 1

    return final_count


coordinates, map = get_grid_and_coordinates()

for coords in coordinates:
    x1 = coords[0][0]
    y1 = coords[0][1]
    x2 = coords[1][0]
    y2 = coords[1][1]

    if x1 == x2:
        y_movement = abs(y1 - y2)
        for i in range(y_movement+1):
            if y1 > y2:
                map[y2+i][x1] += 1
            else:
                map[y1+i][x1] += 1

    elif y1 == y2:
        x_movement = abs(x1 - x2)
        for i in range(x_movement+1):
            if x1 > x2:
                map[y1][x2+i] += 1
            else:
                map[y1][x1+i] += 1


print(get_final_count(map))

coordinates, map = get_grid_and_coordinates()


for coords in coordinates:
    x1 = coords[0][0]
    y1 = coords[0][1]
    x2 = coords[1][0]
    y2 = coords[1][1]

    if x1 == x2:
        y_movement = abs(y1 - y2)
        for i in range(y_movement+1):
            if y1 > y2:
                map[y2+i][x1] += 1
            else:
                map[y1+i][x1] += 1

    elif y1 == y2:
        x_movement = abs(x1 - x2)
        for i in range(x_movement+1):
            if x1 > x2:
                map[y1][x2+i] += 1
            else:
                map[y1][x1+i] += 1

    elif abs(x1 - x2) == abs(y1 - y2):
        if x1 > x2 and y2 > y1:
            movement = abs(x1 - x2)
            for i in range(movement+1):
                map[y1+i][x1-i] += 1

        elif x1 < x2 and y2 > y1:
            movement = abs(x1 - x2)
            for i in range(movement + 1):
                map[y1 + i][x1 + i] += 1

        elif x1 > x2 and y1 > y2:
            movement = abs(x1 - x2)
            for i in range(movement+1):
                map[y1-i][x1-i] += 1

        elif x1 < x2 and y1 > y2:
            movement = abs(x1 - x2)
            for i in range(movement+1):
                map[y1-i][x1+i] += 1


print(get_final_count(map))
