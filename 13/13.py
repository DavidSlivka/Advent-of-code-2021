width = 0
height = 0
folds = []
positions = []

with open('input13.txt', 'r') as f:
    for line in f:
        if len(line.strip().split(',')) == 2:
            x, y = line.strip().split(',')
            positions.append([int(x), int(y)])
            if int(x) > width:
                width = int(x)

            if int(y) > height:
                height = int(y)

        elif len(line.strip().split(' ')) == 3:
            fold, along, value = line.strip().split(' ')
            folds.append(value)

transparent_map = [['.' for i in range(width+1)] for j in range(height+1)]
for pos in positions:
    transparent_map[pos[1]][pos[0]] = '#'

for fold in folds:
    pos, line = int(fold[2:]), fold[0]

    counter = 2
    if line == 'y':
        for i in range(pos+1, len(transparent_map)):
            for j in range(len(transparent_map[0])):
                if transparent_map[i][j] == '#':
                    transparent_map[i-counter][j] = transparent_map[i][j]
            counter += 2
        transparent_map = transparent_map[:pos+1]

    elif line == 'x':
        for i in range(pos+1, len(transparent_map[0])):
            for j in range(len(transparent_map)):
                if transparent_map[j][i] == '#':
                    transparent_map[j][i-counter] = transparent_map[j][i]
            counter += 2

        tmp = []
        for j in range(len(transparent_map)):
            tmp.append([])
        count = 0
        for i in range(len(transparent_map)):
            for j in range(pos):
                tmp[count].append(transparent_map[i][j])
            count = count + 1

        transparent_map = tmp

count = 0
for row in range(len(transparent_map)):
    for col in range(len(transparent_map[0])):
        if transparent_map[row][col] == '#':
            count += 1

print(count)
print(transparent_map)