from collections import deque

def make_path(p, p_dict):
    for a, b in p:
        if not p_dict.get(a, 0):
            p_dict[a] = []
        if not p_dict.get(b, 0):
            p_dict[b] = []
        p_dict[a].append(b)
        p_dict[b].append(a)


def make_order(o, o_dict, c_dict):
    for a, b in o:
        o_dict[a] = b
        c_dict[b] = 1


def solution(n, path, order):
    answer = True
    path_dict = {}
    visited = list(0 for _ in range(n))
    order_dict = {}
    closed_dict = {}

    make_path(path, path_dict)
    make_order(order, order_dict, closed_dict)

    q = deque([0])

    while q:
        v = q.popleft()

        if visited[v]:
            continue
        visited[v] = 1

        if closed_dict.get(v, 0):
            continue

        next_v = order_dict.get(v)
        if next_v:
            closed_dict[next_v] = 0
            if visited[next_v]:
                q.append(next_v)
                visited[next_v] = 0

        for u in path_dict[v]:
            q.append(u)

    for is_closed in closed_dict.values():
        if is_closed:
            answer = False
            break

    return answer