from collections import deque


def solution(board):
    cost_board = {}
    n = len(board)
    answer = 500*n*n

    # row, col, cost, direction(row: 0, col: 1)
    q = deque([(0, 0, 0, 0), (0, 0, 0, 1)])
    while q:
        r, c, cost, from_side = q.popleft()
        key = n * r + c

        if r == n - 1 and c == n - 1:
            answer = min(answer, cost)
            continue
        if not (0 <= r < n and 0 <= c < n):
            continue
        if board[r][c] == 1:
            continue
        if cost_board.get(key, False):
            if cost_board[key][from_side] < cost:
                continue
        else:
            cost_board[key] = [500*n*n, 500*n*n]

        cost_board[key][from_side] = cost
        if not (r == 0 and c == 0 and from_side):
            q.append((r + 1, c, cost + (100 if not from_side else 600), 0))
            q.append((r - 1, c, cost + (100 if not from_side else 600), 0))
        if not (r == 0 and c == 0 and not from_side):
            q.append((r, c + 1, cost + (100 if from_side else 600), 1))
            q.append((r, c - 1, cost + (100 if from_side else 600), 1))

    return answer