from itertools import combinations


def f(tuple):
    ret = list(tuple)
    ret.sort()
    return ''.join(ret)


def solution(orders, course):
    answer = []

    for course_len in course:
        combi_dic = {}
        candidates = []

        for order in orders:
            combination = combinations(order, course_len)
            combis = map(f, combination)

            for combi in combis:
                if not combi_dic.get(combi, 0):
                    combi_dic[combi] = 0
                combi_dic[combi] += 1

        largest = 2
        for key, value in combi_dic.items():
            if value > largest:
                candidates = [key]
                largest = value
            elif value == largest:
                candidates.append(key)

        answer += candidates

    answer.sort()
    return answer


########

import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]