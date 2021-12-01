f = open('./input1.txt', 'r')

input_list = [int(i) for i in f.read().splitlines()]
increased = 0

for i in range(0, len(input_list) - 1):
    if input_list[i] < input_list[i + 1]:
        increased += 1

print(increased)

increased = 0
for i in range(0, len(input_list) - 3):
    if sum(input_list[i:i+3]) < sum(input_list[i+1:i+4]):
        increased += 1

print(increased)
