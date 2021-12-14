polymer_rules = {}
original = ''

with open('input14.txt', 'r') as f:
    for line in f:
        if len(line.strip().split(' -> ')) == 2:
            polymer, new_polymer = line.strip().split(' -> ')
            polymer_rules[polymer] = new_polymer

        elif len(line.strip().split(' -> ')) == 1:
            if line.strip() != '':
                original = line.strip()


def get_pairs():
    pair_counts = {}
    for elem in range(len(original) - 1):
        if original[elem] + original[elem + 1] not in pair_counts:
            pair_counts[original[elem] + original[elem + 1]] = 0
        pair_counts[original[elem] + original[elem + 1]] += 1

    return pair_counts


def get_new_pairs(n, pair_counts):
    for i in range(n):
        new_pairs = {}
        for pair in pair_counts:
            if pair in polymer_rules:
                if pair[0] + polymer_rules[pair] not in new_pairs:
                    new_pairs[pair[0] + polymer_rules[pair]] = 0

                new_pairs[pair[0] + polymer_rules[pair]] += pair_counts[pair]

                if polymer_rules[pair] + pair[1] not in new_pairs:
                    new_pairs[polymer_rules[pair] + pair[1]] = 0

                new_pairs[polymer_rules[pair] + pair[1]] += pair_counts[pair]

        pair_counts = new_pairs

    return pair_counts


def output(pair_counts):
    counts = {}

    for pair in pair_counts:
        if pair[0] not in counts:
            counts[pair[0]] = 0

        counts[pair[0]] += pair_counts[pair]
        if original[-1] not in counts:
            counts[original[-1]] = 1

    maximum = 0
    minimum = 1e12
    for key in counts:
        if counts[key] > maximum:
            maximum = counts[key]

        if counts[key] < minimum:
            minimum = counts[key]

    return maximum-minimum


p = get_new_pairs(10, get_pairs())
print(output(p))
p = get_new_pairs(40, get_pairs())
print(output(p))
