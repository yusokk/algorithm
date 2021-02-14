# 가중치 합이 가장 큰 경로 -> 지름
# a, b, child -> a: 부모 노드 번호, b: 자식 노드, child: 가중치
# 부모 노드로 정렬되서 입력 됨.
import sys
sys.stdin = open("../test/input.txt", "r")
from collections import deque
read = sys.stdin.readline

# 자식 길이 중 긴 길이를 부모에 합쳐줌?
# max로 최대 항상 유지?
# 위상 정렬? 장조림하고 비슷한듯 한데...

n = int(read())
indegree = [0] * (n+1)
graph = {}
dq = deque()
# graph 형식: 1. 키: 자식 2. 밸류: [부모, 가중치], 왼쪽 자식, 오른쪽 자식
for _ in range(n-1):
    temp_parent, temp_child, temp_weight = map(int, read().rstrip().split())
    if temp_child not in graph:
        graph[temp_child] = []
    graph[temp_child].append([temp_parent, temp_weight])
    indegree[temp_parent] += 1
graph[1] = [[0, 1]]

print(graph)
def topology_sort():
    for i in range(1, n+1):
        if not indegree[i]:
            dq.append(i)
            graph[i].append(0)
    max_len = 0
    while dq:
        vertex = dq.popleft()
        parent, weight = graph[vertex][0]
        if len(graph[vertex]) > 2:
            print(vertex, parent, weight, graph)
            max_len = max(max_len, graph[vertex][1]+graph[vertex][2])
            if vertex == 1:
                break
            if graph[vertex][1] < graph[vertex][2] and vertex != 1:
                graph[parent].append(weight + graph[vertex][2])
            elif graph[vertex][1] > graph[vertex][2] and vertex != 1:
                graph[parent].append(weight + graph[vertex][1])
        else:
            print(vertex, parent, weight, graph)
            max_len = max(max_len, graph[vertex][1])
            if vertex == 1:
                break
            graph[parent].append(weight + graph[vertex][1])
        indegree[parent] -= 1
        if indegree[parent] == 0:
            dq.append(parent)
    return max_len


print(topology_sort())