points = {}

with open('input12.txt', 'r') as f:
    for line in f:
        from_point, to_point = (line.strip().split('-'))
        if from_point not in points:
            points[from_point] = []
        if to_point not in points:
            points[to_point] = []

        points[from_point].append(to_point)
        points[to_point].append(from_point)



def part1(path):
    global total
    if path[-1] == 'end':
        total += 1
        return ''

    not_in_path = []
    for x in points[path[-1]]:
        if x.isupper() or x not in path:
            not_in_path.append(x)

    for x in not_in_path:
        part1(path + [x])


def paths2(path, double=''):
    global total
    if path[-1] == 'end':
        total += 1
        return ''

    for x in points[path[-1]]:
        if x.isupper() or x not in path:
            paths2(path + [x], double)

    if double == '':
        for x in points[path[-1]]:
            if x.islower() and x in path and x != 'start':
                paths2(path + [x], x)


total = 0
part1(['start'])
print(total)

total = 0
paths2(['start'], '')
print(total)