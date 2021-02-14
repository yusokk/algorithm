import sys
read = sys.stdin.readline
n, m = map(int, read().split())

parent = []
level = []
for i in range(n+1):
    parent.append(i)
    level.append(1)

def find_parent(a):
    if parent[a] == a:
        return a
    parent[a] = find_parent(parent[a])
    return parent[a]


def merge(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return
    if level[a] < level[b]:
        a, b = b, a
    parent[b] = a
    if level[a] == level[b]:
        level[a] += 1
    return


def compare(a, b):
    if find_parent(a) == find_parent(b):
        print("YES")
    else:
        print("NO")


for _ in range(m):
    f, a, b = map(int, read().split())
    if f == 0:
        merge(a, b)
    else:
        compare(a, b)