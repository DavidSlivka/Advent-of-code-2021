with open('input17.txt', 'r') as f:
    vars = [l for l in f.readline().strip().split()]
    xs = [num for num in vars[2].split('..')]
    ys = [num for num in vars[3].split('..')]

    cleanx = [''.join(i) for i in [[i for i in j if i.isdigit() or i == '-'] for j in xs]]
    cleany = [''.join(i) for i in [[i for i in j if i.isdigit() or i == '-'] for j in ys]]

    min_x, max_x = int(min(cleanx)), int(max(cleanx))
    max_y, min_y = int(max(cleany)), int(min(cleany))


def launch(x_val, y_val):
    maxy = max_y
    x, y = 0, 0
    step = 0
    while max_x > x and max_y < y:
        step += 1
        x += x_val
        y += y_val
        if y > maxy:
            maxy = y
        if x_val > 0:
            x_val -= 1

        y_val -= 1
        if min_x <= x <= max_x and max_y <= y <= min_y:
            return maxy, step

    return 0, -1


def solve():
    total = []
    for x in range(0, max_x + 1):
        for y in range(max_y, 100):
            mxy, k = launch(x, y)
            if k >= 0:
                total.append(mxy)
    return len(total), max(total)


length, max_height = solve()
print(max_height)
print(length)
