import sys
from collections import deque
read = sys.stdin.readline

def solution ():
    n = int(read())
    indegrees = list(0 for _ in range(n))
    graph = {i : [0] for i in range(n)}
    build_times = list(0 for _ in range(n))
    for i in range(n):
        temp = list(map(int, read().rstrip().split()))
        for index in range(len(temp)):
            if index == 0:
                graph[i][0] += temp[index]
                build_times[i] = temp[index]
            elif index < len(temp) - 1:
                graph[temp[index]-1].append(i)
                indegrees[i] += 1
            else:
                continue
    que = deque([])
    for i in range(n):
        if indegrees[i] == 0:
            que.append(i)
    while que:
        pop = que.popleft()
        for i in range(1, len(graph[pop])):
            build_times[graph[pop][i]] = max(build_times[graph[pop][i]], graph[graph[pop][i]][0]+build_times[pop])
            indegrees[graph[pop][i]] -= 1
            if indegrees[graph[pop][i]] == 0:
                que.append(graph[pop][i])

    for i in range(n):
        print(build_times[i])
solution()
