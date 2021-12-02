horizontal = 0
depth = 0

commands = {'up': -1,
            'down': 1}

with open('./input2.txt', 'r') as f:
    for line in f:
        command, value = line.split(' ')
        if command in commands:
            depth += int(value) * commands[command]
        else:
            horizontal += int(value)


print(depth * horizontal)

aim = 0
horizontal = 0
depth = 0

with open('./input2.txt', 'r') as f:
    for line in f:
        command, value = line.split(' ')
        if command in commands:
            aim += int(value) * commands[command]
        else:
            horizontal += int(value)
            depth += aim * int(value)

print(depth * horizontal)