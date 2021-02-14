import sys
sys.stdin = open("../test/cabbage.txt", "r")
sys.setrecursionlimit(10**5)
read = sys.stdin.readline
T = int(read())
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs(tup):
    x, y = tup
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (nx, ny) in field and (nx, ny) not in check:
            check[(nx, ny)] = True
            dfs((nx, ny))

for i in range(T):
    N, M, K = map(int, read().rstrip().split())
    field =[]
    for _ in range(K):
        field.append(tuple(map(int, read().rstrip().split())))
    check = {}
    count = 0
    for j in range(K):
        if field[j] not in check:
            count += 1
            check[field[j]] = True
            dfs(field[j])
    print(count)