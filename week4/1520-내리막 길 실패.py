import sys
read = sys.stdin.readline
m, n = map(int, read().rstrip().split())

field = list(list(map(int, read().rstrip().split())) for _ in range(m))
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

# dp에 경로 개수 저장
dp = [[0]*n for _ in range(m)]


def recur(x, y):
    max_dp = 0
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < m and 0 <= next_y < n and field[x][y] > field[next_x][next_y]:
            dp[next_x][next_y] += 1


ans = recur(0, 0)
print(ans)