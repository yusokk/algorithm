import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())

small_stones = list(int(read()) for _ in range(M))
dx = [1, 0, -1]
check = dict()
dq = deque()


def bfs():
    dq.append((1, 0))
    dq.append(-1)
    count = 0
    while dq:
        if dq[0] == -1:
            if len(dq) == 1:
                return -1
            else:
                dq.popleft()
                dq.append(-1)
                count += 1
        current_stone, distance = dq.popleft()
        if current_stone == N:
            return count
        for i in range(3):
            next_distance = distance + dx[i]
            if next_distance > 0:
                next_stone = current_stone + next_distance
            else:
                break
            if next_distance not in check.get(next_stone, []) and next_stone not in small_stones:
                if next_stone not in check:
                    check[next_stone] = [next_distance]
                else:
                    check[next_stone].append(next_distance)
                dq.append((next_stone, next_distance))


print(bfs())