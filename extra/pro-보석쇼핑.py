from collections import deque
dq = deque()
gem_dic = dict()

def solution(gems):
    for i in range(len(gems)):
        if gems[i] not in gem_dic:
            gem_dic[gems[i]] = 0
        gem_dic[gems[i]] += 1

    total = len(gem_dic)

    k = 0
    for i in range(len(gems)):
        if not dq or gems[i] != dq[0][0]:
            dq.append((gems[i], i))
            gem_dic[gems[i]] -= 1
            total -= 1
            if not total:
                break
        elif gems[i] == dq[0][0]:
            dq.popleft()
    if len(dq) == 1:
        answer = [dq[0][1]+1, dq[0][1]+1]
    else:
        answer = [dq[0][1]+1, dq[-1][1]+1]
    first = len(dq)
    min_len = first

    for i in range(k, len(gems)):
        if gems[i] == dq[0][0]:
            dq.append((gems[i], i))
            j = 1
            while dq[0][0] != dq[j][0]:
                dq.popleft()
                gem_dic[gems[i]] -= 1
                j += 1
            min_len = min(min_len, len(dq))
            if not gem_dic[gems[i]]:
                break
    if first > min_len:
        answer = [dq[0][1]+1, dq[-1][1]+1]
    return answer

print(solution(["AA", "AB", "AC", "AA", "AC"]))
