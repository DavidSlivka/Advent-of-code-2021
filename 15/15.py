with open('input15.txt', 'r') as f:
    matrix = [list(map(int, line)) for line in f.read().splitlines()]

cost_to = {(0, 0): 0}
height = len(matrix)
width = len(matrix[0])
to_visit = [[0, 0]]
visited = []


def get_neighbors(i, j):
    if [i, j] not in visited:
        for x, y in [(i + 1, j), (i, j + 1)]:
            if 0 <= x < height and 0 <= y < width and [x, y] not in visited:
                if [x, y] not in to_visit:
                    to_visit.append([x, y])
                visited.append([i, j])
                if (x, y) not in cost_to:
                    cost_to[(x, y)] = cost_to[(i, j)] + matrix[x][y]

                else:
                    if cost_to[(i, j)] + matrix[x][y] < cost_to[(x, y)]:
                        cost_to[(x, y)] = cost_to[(i, j)] + matrix[x][y]


for i in to_visit:
    get_neighbors(i[0], i[1])


print(cost_to[(width-1, height-1)])
