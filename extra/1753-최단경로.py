import heapq
import sys
read = sys.stdin.readline

V, E = map(int, read().rstrip().split())
K = int(read())


def set_w(E, graph):
    for _ in range(E):
        u, v, w = map(int, read().rstrip().split())
        if not graph.get(u, False):
            graph[u] = []
        graph[u].append([v, w])



def dijkstra(V, E, K):
    que = []
    graph = {}

    set_w(E, graph)
    distances = {node: float('inf') for node in graph}

    heapq.heappush(que, ([K, 0]))
    while que:
        dest, dist = heapq.heappop(que)
        if distances[dest] < dist:
            continue

        if not graph.get(dest, 0):
            continue

        for v, w in graph[dest]:
            new_cost = dist + w
            if not distances.get(v, 0):
                distances[v] = float('inf')
            if new_cost < distances[v]:
                distances[v] = new_cost
                heapq.heappush(que, [v, new_cost])

    for node in sorted(distances):
        if node == K:
            print(0)
        elif distances[node] == float('inf'):
            print('INF')
        else:
            print(distances[node])


dijkstra(V, E, K)