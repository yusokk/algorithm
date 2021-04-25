def solution(n, computers):
    parent = [i for i in range(n)]
    def get_parent(a):
        if parent[a] == a: return a
        parent[a] = get_parent(parent[a])
        return parent[a]

    def merge(a, b):
        if get_parent(a) == get_parent(b):
            return
        a = get_parent(a)
        b = get_parent(b)
        parent[a] = b

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                merge(i, j)

    parent_set = set()
    for i in range(n):
        parent_set.add(get_parent(i))
    answer = len(parent_set)
    return answer