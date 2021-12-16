dct = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

BITS = ''
with open('input16.txt', 'r') as f:
    for symbol in f.readline().strip():
        BITS += dct[symbol]

pos = 0
version = 0


def convert():
    global pos
    global version
    packet_version = int(BITS[pos:pos + 3], 2)
    packet_type_id = int(BITS[pos + 3:pos + 6], 2)
    pos += 6
    version += packet_version
    value = 0

    if packet_type_id == 4:
        literal_value = int(BITS[pos + 1:pos + 5], 2)
        value = int(BITS[pos + 1:pos + 5], 2)
        pos += 5
        while BITS[pos - 5:pos - 4] == '1':
            literal_value += int(BITS[pos + 1:pos + 5], 2)
            value = value * 16 + literal_value
            pos += 5

    else:
        sub_packets = []
        index = BITS[pos:pos + 1]
        pos += 1
        if index == '1':
            count = int(BITS[pos:pos + 11], 2)
            pos += 11
            for j in range(count):
                sub_packets.append(convert())
        else:
            length = int(BITS[pos:pos + 15], 2)
            pos += 15
            final_pos = pos + length
            while pos < final_pos:
                sub_packets.append(convert())

        if packet_type_id == 0:
            return sum(sub_packets)

        elif packet_type_id == 1:
            final = 1
            for item in sub_packets:
                final *= item
            return final

        elif packet_type_id == 2:
            return min(sub_packets)

        elif packet_type_id == 3:
            return max(sub_packets)

        elif packet_type_id == 5:
            return 1 if sub_packets[0] > sub_packets[1] else 0

        elif packet_type_id == 6:
            return 1 if sub_packets[0] < sub_packets[1] else 0

        elif packet_type_id == 7:
            return 1 if sub_packets[0] == sub_packets[1] else 0

    return value


print(convert())
print(version)
