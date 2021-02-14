import sys
read = sys.stdin.readline

n, m, k = map(int, read().rstrip().split())

costs = list(map(int, read().rstrip().split()))
friend_to_cost = list((i, v) for i, v in enumerate(costs))
friend_to_cost.sort(key=lambda x: x[1])

parent = list(range(n))
level = [1]*n


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


for _ in range(m):
    a, b = map(int, read().rstrip().split())
    union(a-1, b-1)

first = friend_to_cost[0][0]
total = 0

for friend in friend_to_cost:
    f, c = friend
    if f == first:
        if k >= c:
            total += c
            k -= c
            continue
        else:
            print("Oh no")
    if find(f) != find(first):
        if k < c:
            print("Oh no")
            break
        else:
            total += c
            k -= c
            union(first, f)
else:
    print(total)