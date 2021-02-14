import sys
read = sys.stdin.readline
n = int(read())
m = int(read())

parent = list(range(n))
graph = list(list(map(int, read().rstrip().split())) for _ in range(n))
level = [1] * n

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if level[a] < level[b]:
        a, b = b, a
    if level[a] == level[b]:
        level[a] += 1
    parent[b] = a


for i in range(n):
    for j in range(i, n):
        if graph[i][j] == 1:
            union(i, j)

cities = map(int, read().rstrip().split())
answer = set()
for city in cities:
    answer.add(find(city-1))

if len(answer) > 1:
    print("NO")
else:
    print("YES")