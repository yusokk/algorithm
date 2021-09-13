d = [1, -1, 0, 0]
answer = 9

def move(locArr, turn, board, count):
    global answer
    loc = locArr[turn]
    board[loc[0]][loc[1]] = 0
    print(loc,turn, board, count)

    for i in range(4):
        r = loc[0] + d[i]
        c = loc[1] + d[3 - i]

        if locArr[0] != locArr[1] and 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == 1:
            if turn:
                move([locArr[0], [r, c]], 0, board, count + 1)
            else:
                move([[r, c], locArr[1]], 1, board, count + 1)
        else:
            answer = min(answer, count)

    board[loc[0]][loc[1]] = 1

def solution(board, aloc, bloc):
    global answer
    move([aloc, bloc], 0, board, 1)

    print(answer)

    return answer

solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],[1, 0], [1, 2]	)