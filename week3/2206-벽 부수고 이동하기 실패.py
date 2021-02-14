import sys
from collections import deque
sys.stdin = open("../test/break-wall.txt", "r")
read = sys.stdin.readline
dq = deque()
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)


def bfs():
    count = 1
    dq.append((0, 0, False, count))
    while dq:
        x, y, use_b, cnt, visited = dq.popleft()
        print(visited)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx == N-1 and ny == M-1:
                return cnt+1
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny]:
                    if not use_b:
                        dq.append((nx, ny, True, cnt+1))
                else:
                    dq.append((nx, ny, use_b, cnt+1))
    return -1


N, M = map(int, read().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int, list(read().rstrip()))))

print(bfs())