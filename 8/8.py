lines = []
count = 0

with open('./input8.txt', 'r') as f:
    for line in f:
        lines.append(line)
        for word in line.split(" | ")[1].split():
            if len(word) in [2, 3, 4, 7]:
                count += 1

print(count)


def part2(line):
    records = line.split(" | ")[0].split()

    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    zero = []

    for record in records:
        if len(record) == 2:
            for l in record:
                one.append(l)
        if len(record) == 3:
            for l in record:
                seven.append(l)
        if len(record) == 4:
            for l in record:
                four.append(l)
        if len(record) == 7:
            for l in record:
                eight.append(l)

    # 2, 3, 5
    for record in records:
        if len(record) == 5:
            if all(l in record for l in one):
                for l in record:
                    three.append(l)

            else:
                count_for_five = 0
                for l in record:
                    if l in four:
                        count_for_five += 1

                if count_for_five == 3:
                    for l in record:
                        five.append(l)

                else:
                    for l in record:
                        two.append(l)

    # 0, 6, 9
    for record in records:
        if len(record) == 6:
            if not all(l in record for l in one):
                for l in record:
                    six.append(l)

            if all(l in record for l in three):
                for l in record:
                    nine.append(l)

            if not all(l in record for l in five):
                for l in record:
                    zero.append(l)

    records_to_numbers = {
        "".join(sorted(zero)): "0",
        "".join(sorted(one)): "1",
        "".join(sorted(two)): "2",
        "".join(sorted(three)): "3",
        "".join(sorted(four)): "4",
        "".join(sorted(five)): "5",
        "".join(sorted(six)): "6",
        "".join(sorted(seven)): "7",
        "".join(sorted(eight)): "8",
        "".join(sorted(nine)): "9",
    }
    total_sum_for_line = ''
    for d in line.split(" | ")[1].split():
        total_sum_for_line += "".join(records_to_numbers["".join(sorted(d))])

    return int(total_sum_for_line)


print(sum(part2(line) for line in lines))
