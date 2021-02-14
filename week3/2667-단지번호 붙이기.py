import sys
sys.stdin = open("../test/danji.txt", "r")
read = sys.stdin.readline
N = int(read())
square = list()
for _ in range(N):
    square.append(list(map(int, list(read().rstrip()))))
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

stack = list()

def dfs(x, y):
    stack.append((x, y))
    square[x][y] = -1
    count = -1
    while stack:
        pop_x, pop_y = stack.pop()
        for i in range(4):
            nx = pop_x + dx[i]
            ny = pop_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if square[nx][ny] == 1:
                    count -= 1
                    square[nx][ny] = count
                    stack.append((nx, ny))
    # for i in range(N):
    #     print(*square[i])
    # print()
    # print()
    return -count


answers = []
for x in range(N):
    for y in range(N):
        if square[x][y] == 1:
            answers.append(dfs(x, y))


print(len(answers))
answers.sort()
for ans in answers:
    print(ans)