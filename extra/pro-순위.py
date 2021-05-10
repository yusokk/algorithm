def solution(n, results):
    answer = 0
    win_dic = dict()
    lose_dic = dict()

    for result in results:
        w, l = result
        if w not in win_dic:
            win_dic[w] = set()
        if l not in lose_dic:
            lose_dic[l] = set()
        win_dic[w].add(l)
        lose_dic[l].add(w)

    for i in range(1, n + 1):
        if i in win_dic:
            for loser in win_dic[i]:
                if loser not in lose_dic:
                    lose_dic[loser] = set()
                if i in lose_dic:
                    lose_dic[loser] |= lose_dic[i]
        if i in lose_dic:
            for winner in lose_dic[i]:
                if winner not in win_dic:
                    win_dic[winner] = set()
                if i in win_dic:
                    win_dic[winner] |= win_dic[i]

    for i in range(1, n + 1):
        if i not in lose_dic and i in win_dic and len(win_dic[i]) == n - 1:
            answer += 1
        elif i not in win_dic and i in lose_dic and len(lose_dic[i]) == n - 1:
            answer += 1
        elif i in lose_dic and i in win_dic and len(lose_dic[i]) + len(win_dic[i]) == n - 1:
            answer += 1
    return answer

# 유니온 파인드
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