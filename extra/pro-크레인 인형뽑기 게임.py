def solution(board, moves):
    answer = 0
    board_length = len(board)
    top_floor = [-1 for i in range(board_length)]
    stack = []

    for move in moves:
        current = move - 1
        if top_floor[current] == -1:
            for i in range(board_length):
                if board[i][current] != 0:
                    top_floor[current] = i
                    break
            else:
                top_floor[current] = -1
        if top_floor[current] == board_length:
            continue
        else:
            target = board[top_floor[current]][current]
            board[top_floor[current]][current] = 0
            top_floor[current] += 1
            if stack and stack[-1] == target:
                stack.pop()
                answer += 2
            else:
                stack.append(target)
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],	[1,5,3,5,1,2,1,4])