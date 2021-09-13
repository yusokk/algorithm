import sys
read = sys.stdin.readline

n = int(read())
area = list(list(map(int, read().rstrip().split())) for _ in range(n))

max_area = -1

left, right = 1, 100
while left <= right:
    h = (left+right) // 2
    count = 0
    check = [0 for _ in range(n ** n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] <= h or check[i * n + j]:
                continue
            count += 1
            stack = [(i, j)]
            while stack:
                r, c = stack.pop()
                check[r*n + c] = 1
                if r-1 >= 0 and not check[(r-1) * n + c] and area[r-1][c] > h:
                    stack.append((r-1, c))
                if c-1 >= 0 and not check[r * n + (c-1)] and area[r][c-1] > h:
                    stack.append((r, c-1))
                if r+1 < n and not check[(r+1) * n + c] and area[r+1][c] > h:
                    stack.append((r+1, c))
                if c+1 < n and not check[r * n + (c+1)] and area[r][c+1] > h:
                    stack.append((r, c+1))
    if max_area != 0 and max_area <= count:
        max_area = count
        left = h+1
    else:
        right = h-1


print(max_area)