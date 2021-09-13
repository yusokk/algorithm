dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def second_check(board, row, col, prev):
    prev_row, prev_col = prev
    for i in range(4):
        next_row = row + dx[i]
        next_col = col + dy[i]

        if next_row == prev_row and next_col == prev_col:
            continue

        if 0 <= next_row < 5 and 0 <= next_col < 5 and board[next_row][next_col] == 'P':
            return 0

    return 1


def check(board, row, col):
    if row + 1 < 5 and board[row + 1][col] == 'P':
        return 0
    if col + 1 < 5 and board[row][col + 1] == 'P':
        return 0

    current = (row, col)
    if row + 1 < 5 and board[row + 1][col] == 'O':
        if not second_check(board, row + 1, col, current):
            return 0
    if col + 1 < 5 and board[row][col + 1] == 'O':
        if not second_check(board, row, col + 1, current):
            return 0
    if col - 1 >= 0 and board[row][col - 1] == 'O':
        if not second_check(board, row, col - 1, current):
            return 0

    return 1


def check_place(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] != 'P':
                continue

            if not check(place, i, j):
                return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(check_place(place))

    return answer