import sys; read = sys.stdin.readline
from collections import deque
N, K = map(int, read().rstrip().split())
dq = deque()
visited = [1 for _ in range(100001)]


def bfs(start_v):
    dq.append(start_v)
    dq.append(-1)
    count = 0
    while dq:
        v = dq.popleft()
        if v == K:
            return count
        if v < 0:
            count += 1
            dq.append(-1)
        else:
            if v+1 <= 100000 and visited[v+1]:
                visited[v+1] = 0
                dq.append(v+1)
            if 0 <= v-1 and visited[v-1]:
                visited[v-1] = 0
                dq.append(v-1)
            if v*2 <= 100000 and visited[v*2]:
                visited[v*2] = 0
                dq.append(v*2)


print(bfs(N))