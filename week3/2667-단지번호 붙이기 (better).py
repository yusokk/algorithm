import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)


def dfs(x, y, count):
    count -= 1              # 첫번째 집 중복 제외하기 위해 -를 넣어
    board[x][y] = count
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] == 1:
                count = dfs(nx, ny, count)
    return count

N = int(read())
board = list(list(map(int, list(read().rstrip()))) for _ in range(N))

ans_list = []
for x in range(N):
    for y in range(N):
        if board[x][y] == 1:
            ans_list.append(-dfs(x, y, 0))
ans_list.sort()
print(len(ans_list))
for ans in ans_list:
    print(ans)