def get_input():
    positions_with_values = {}
    with open('input11.txt', 'r') as f:
        lines = [line.strip() for line in f]
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                positions_with_values[i, j] = int(lines[i][j])

    return positions_with_values


def flash(positions_with_values):
    flashes = 0
    need_to_flash = []
    extinct = []
    for indices in positions_with_values:
        positions_with_values[indices] += 1
        if positions_with_values[indices] == 10:
            need_to_flash.append(indices)

    while need_to_flash:
        flashes += 1
        indices = need_to_flash.pop()
        extinct.append(indices)
        for x in range(-1, 2):
            for j in range(-1, 2):
                if (indices[0] + x, indices[1] + j) in positions_with_values and (x, j) != (0, 0):
                    if positions_with_values[(indices[0] + x, indices[1] + j)] == 9:
                        need_to_flash.append((indices[0] + x, indices[1] + j))
                    if positions_with_values[(indices[0] + x, indices[1] + j)] < 10:
                        positions_with_values[(indices[0] + x, indices[1] + j)] += 1

    for indices in extinct:
        positions_with_values[indices] = 0

    return flashes


def part1():
    positions_with_values = get_input()
    flashes = 0
    for i in range(100):
        flashes += flash(positions_with_values)

    return flashes


def part2():
    positions_with_values = get_input()
    step = 0
    all_flash = False
    while not all_flash:
        step += 1
        _ = flash(positions_with_values)

        if all(positions_with_values[indices] == 0 for indices in positions_with_values):
            all_flash = True

    return step


print(part1())
print(part2())