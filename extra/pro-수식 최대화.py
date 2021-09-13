from itertools import permutations


def split_expression(str):
    split_list = []
    index = 0

    for i in range(len(str)):
        c = str[i]
        if c != '*' and c != '-' and c != '+':
            continue
        split_list.append(int(str[index:i]))
        split_list.append(c)
        index = i + 1

    split_list.append(int(str[index:]))

    return split_list


def calculate(exp_list, operations):
    last_list = exp_list
    for operation in operations:
        temp_list = []

        for i in range(len(last_list)):
            if last_list[i - 1] == operation: continue

            if last_list[i] != operation:
                temp_list.append(last_list[i])

            else:
                if operation == '*':
                    temp_list[-1] *= last_list[i + 1]
                elif operation == '-':
                    temp_list[-1] -= last_list[i + 1]
                elif operation == '+':
                    temp_list[-1] += last_list[i + 1]

        last_list = temp_list

    if last_list[0] < 0:
        return -last_list[0]
    else:
        return last_list[0]


def solution(expression):
    answer = 0
    split_exp = split_expression(expression)
    operator_pers = list(permutations(['*', '-', '+']))

    for operators in operator_pers:
        answer = max(answer, calculate(split_exp, operators))

    return answer