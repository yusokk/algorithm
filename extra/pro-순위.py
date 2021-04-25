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