def calculate_win_rate(record):
    if record.count('N') == len(record):
        return 0

    total = record.count('L') + record.count('W')

    return record.count('W') / total


def count_win_over_weight(index, record, weights):
    count = 0

    for i in range(len(record)):
        if record[i] == 'W' and weights[i] > weights[index]:
            count += 1
    return count


def sort_key(index, condition1, condition2, condition3):
    return (-condition1[index], -condition2[index], -condition3[index], index)


def solution(weights, head2head):
    answer = [i for i in range(1, len(weights) + 1)]

    win_rate = list(map(calculate_win_rate, head2head))
    over_weight = list(map(lambda x: count_win_over_weight(x[0], x[1], weights), enumerate(head2head)))

    answer = list(
        map(lambda x: x[1], sorted(enumerate(answer),key=lambda x: sort_key(x[0], win_rate, over_weight, weights))))

    print(answer)
    return answer

solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"])