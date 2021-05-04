from itertools import permutations

def is_match(users, bans):
    for i in range(len(users)):
        if len(users[i]) != len(bans[i]):
            return False
        for j in range(len(bans[i])):
            if bans[i][j] == '*':
                continue
            elif bans[i][j] != users[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    for com_set in permutations(user_id, len(banned_id)):
        if is_match(com_set, banned_id):
            ans_set = set(com_set)
            if ans_set not in answer:
                answer.append(ans_set)
    return len(answer)