from collections import deque


def setDict(a, b, dic):
    if not dic.get(a, 0):
        dic[a] = []
    dic[a].append(b)


def solution(n, edge):
    answer = 0
    vertex_dict = {}

    for a, b in edge:
        setDict(a, b, vertex_dict)
        setDict(b, a, vertex_dict)

    visited = [0] * n
    que = deque(vertex_dict.get(1))
    visited[0] = 1
    for second in que:
        visited[second - 1] = 1
    while que:
        answer = len(que)
        for _ in range(len(que)):
            pop = que.popleft()
            for next_node in vertex_dict.get(pop, []):
                if visited[next_node - 1]:
                    continue
                visited[next_node - 1] = 1
                que.append(next_node)

    return answer