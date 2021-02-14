import sys
from itertools import combinations
from copy import deepcopy
read = sys.stdin.readline
row, col = map(int, sys.stdin.readline().rstrip().split())
matrix = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(row))

count_2, count_1 = 0, 0
list_0 = []
for i in range(row):
    for j in range(col):
        if matrix[i][j] == 2:
            count_2 += 1
        elif matrix[i][j] == 1:
            count_1 += 1
        else:
            list_0.append((i, j))
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


# dfs 함수 - 2에서 출발 0이면 고 하면서 2로 바꿈
def dfs(matrix, comb):
    copy = deepcopy(matrix)
    for coord in comb:
        x, y = coord
        copy[x][y] = 1
    min_virus = row * col
    count = 0
    stack = []
    for r in range(row):
        for c in range(col):
            if copy[r][c] == 2:
                stack.append((r, c))
            while stack:
                x, y = stack.pop()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < row and 0 <= ny < col:
                        if copy[nx][ny] == 0:
                            copy[nx][ny] = 1
                            count += 1
                            stack.append((nx, ny))
    return count


# matrix 경우의 수
comb_3 = tuple(combinations(list_0, 3))
min_v = row * col
for comb in comb_3:
     min_v = min(dfs(matrix, comb), min_v)

ans = row*col - count_1 - count_2 - 3 - min_v
print(ans)