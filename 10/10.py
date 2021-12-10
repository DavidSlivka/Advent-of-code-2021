with open('input10.txt', 'r') as f:
    lines = [line.strip() for line in f]

mistakes_values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

adding_values = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

match_brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def get_mistakes(line, mistakes):
    current = ''
    corrupted = False
    for elem in line:
        if elem in match_brackets.keys():
            current += elem

        else:
            if elem != match_brackets[current[-1]]:
                mistakes += elem
                corrupted = True
                break
            else:
                current = current[0:-1]

    return mistakes, corrupted, current


mistakes = ''
non_corrupted = []
for line in lines:
    m, res, remaining = (get_mistakes(line, ''))
    mistakes += m
    if res is False:
        non_corrupted.append(remaining)

print(sum(mistakes_values[m] for m in mistakes))

added_counts = []
for remaining in non_corrupted:
    total = 0
    needed_to_be_added = ''
    for bracket in remaining[::-1]:
        needed_to_be_added += match_brackets[bracket]

    for bracket in needed_to_be_added:
        total += adding_values[bracket]
        total *= 5
    total /= 5
    added_counts.append(total)


print(int(sorted(added_counts)[len(added_counts)//2]))