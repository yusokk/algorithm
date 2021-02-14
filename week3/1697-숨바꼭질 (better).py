# 가장 빠른 시간 -> bfs
# 중복 체크 -> 100001개 배열에 -로 카운트 해주자...?

import sys
from collections import deque
read = sys.stdin.readline
dq = deque()
check = list(0 for _ in range(100001))


def bfs(start_v, end_v):
    count = 0
    dq.append((start_v, count))
    while dq:
        v, cnt = dq.popleft()
        check[v] = cnt
        if v == end_v:
            return cnt
        cnt -= 1
        if 0 <= v-1 and not check[v-1]:
            dq.append((v-1, cnt))
        if v+1 < 100001 and not check[v+1]:
            dq.append((v+1, cnt))
        if v*2 < 100001 and not check[v*2]:
            dq.append((v*2, cnt))


N, K = map(int, read().rstrip().split())
print(-bfs(N, K))