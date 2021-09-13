def solution(s: str):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        compressed = ''
        target = ''
        count = 1
        for j in range(0, len(s), i):
            currentUnit = s[j:j+i] if j+i <= len(s) else s[j:]
            if target == currentUnit:
                count += 1
                continue

            if (count > 1):
                compressed += str(count)

            target = s[j:j + i]
            compressed += target
            count = 1

        if (count > 1):
            compressed += str(count)

        answer = min(answer, len(compressed))

    # print(answer)
    return answer

#
# print(solution("aabbaccc") == 7)
# print(solution("ababcdcdababcdcd") == 9)
# print(solution("abcabcdede") == 8)
# print(solution("abcabcabcabcdededededede") == 14)
# print(solution("xababcdcdababcdcd") == 17)

