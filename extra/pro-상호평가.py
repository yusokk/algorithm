from collections import Counter


def getGrade(score):
    score //= 10
    print(score)
    if score == 10 or score == 9:
        return 'A'
    elif score == 8:
        return 'B'
    elif score == 7:
        return 'C'
    elif score == 6 or score == 5:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    scores = list(list(score[i] for score in scores) for i in range(len(scores)))

    for i in range(len(scores)):
        score_list = scores[i]
        counter = sorted(Counter(score_list).items(), key=lambda x: -x[0])

        if counter[0][1] == 1 and counter[0][0] == score_list[i]:
            score_list.pop(i)
        elif counter[-1][1] == 1 and counter[-1][0] == score_list[i]:
            score_list.pop(i)

        answer += getGrade(sum(score_list) / len(score_list))

    return answer