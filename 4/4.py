
def get_nums_and_boards():
    generated_nums = []
    boards = []
    board_index = 0

    with open('./input4.txt', 'r') as f:
        for line in f:
            if len(generated_nums) == 0:
                for num in line.strip().split(','):
                    generated_nums.append(int(num))
            else:
                if len(boards) == 0 and len(line.strip()) == 0:
                    continue

                if (line.strip()) == '':
                    board_index += 1
                    continue

                if board_index == len(boards):
                    boards.append([])

                boards[board_index].append([int(num) for num in line.split()])

    return boards, generated_nums


def check_winner(board):
    for i in range(5):
        if sum(board[i]) == -5:
            return True

        if board[0][i] + board[1][i] + board[2][i] + board[3][i] + board[4][i] == -5:
            return True

    return False


boards, generated_nums = get_nums_and_boards()


for num in generated_nums:
    for board in boards:
        for row in board:
            for index in range(len(row)):
                if row[index] == num:
                    row[index] = -1

        if check_winner(board):
            sum_of_unmarked = 0
            for row in board:
                for index in range(len(row)):
                    if row[index] != -1:
                        sum_of_unmarked += row[index]
            print(sum_of_unmarked * num)
            break
    else:
        continue
    break

boards, generated_nums = get_nums_and_boards()

for num in generated_nums:
    for bd_index in range(len(boards)-1, -1, -1):
        for row in boards[bd_index]:
            for index in range(len(row)):
                if row[index] == num:
                    row[index] = -1

        if check_winner(boards[bd_index]):
            if len(boards) != 1:
                boards.remove(boards[bd_index])

            else:
                sum_of_unmarked = 0
                for row in boards[bd_index]:
                    for index in range(len(row)):
                        if row[index] != -1:
                            sum_of_unmarked += row[index]
                print(sum_of_unmarked * num)
                break
    else:
        continue
    break

