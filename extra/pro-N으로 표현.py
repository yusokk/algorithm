def solution(N, number):
    dp = {}
    case = [[]]
    for i in range(1, 9):
        new = 0
        for n in range(i):
            new += N*(10**n)
        dp[new] = i
        case.append([new])
        for j in range(1, i):
            for a in case[j]:
                for b in case[i-j]:
                    temp = [a+b, a-b, a*b]
                    if b != 0:
                        temp.append(a//b)
                    for t in temp:
                        if t not in dp:
                            if t == number:
                                return i
                            dp[t] = i
                            case[i].append(t)
    return -1