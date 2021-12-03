
gamma = ''
epsilon = ''
total_lines = 0
dict_with_positions = {}

with open('input3.txt', 'r') as f:
    for line in f:
        total_lines += 1
        for s in range(len(line)-1):
            if f'index_{s}' not in dict_with_positions:
                dict_with_positions[f'index_{s}'] = 0

            if line[s] == '1':
                dict_with_positions[f'index_{s}'] += 1


keys = dict_with_positions.keys()

for key in keys:
    if dict_with_positions[key] > total_lines // 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'


print(int(gamma, 2) * int(epsilon, 2))


def get_wanted_num_for_oxygen(records, pos):
    zeros = 0
    ones = 0

    for rec in records:
        if rec[pos] == '0':
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        return 0
    else:
        return 1


def get_wanted_num_for_CO(records, pos):
    zeros = 0
    ones = 0

    for rec in records:
        if rec[pos] == '0':
            zeros += 1
        else:
            ones += 1

    if zeros <= ones:
        return 0
    else:
        return 1


remaining_list = []
oxygen = 0

co = 0


with open('input3.txt', 'r') as f:
    for line in f:
        remaining_list.append(str(line).rstrip('\n'))


for i in range(len(remaining_list[0])):
    oxygen_list = []
    wanted_num = get_wanted_num_for_oxygen(remaining_list, i)

    for record in remaining_list:
        if int(record[i]) == int(wanted_num):
            oxygen_list.append(record)

    if len(oxygen_list) == 1:
        oxygen = oxygen_list[0]
        break

    remaining_list = oxygen_list


remaining_list = []
with open('input3.txt', 'r') as f:
    for line in f:
        remaining_list.append(str(line).rstrip('\n'))


for i in range(len(remaining_list[0])):
    CO_list = []
    wanted_num = get_wanted_num_for_CO(remaining_list, i)

    for record in remaining_list:
        if int(record[i]) == int(wanted_num):
            CO_list.append(record)

    if len(CO_list) == 1:
        co = CO_list[0]
        break

    remaining_list = CO_list


print(int(oxygen, 2) * int(co, 2))
