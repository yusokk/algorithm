from collections import Counter


def solution(N, stages):
    failure_rate = []
    counter = Counter(stages)

    remaining_users = len(stages)
    for stage in range(1, N + 1):
        if not remaining_users:
            failure_rate.append([stage, 0])
            continue

        current_users = 0 if not counter[stage] else counter[stage]
        failure_rate.append([stage, current_users / remaining_users])
        remaining_users -= current_users

    return list(map(lambda x: x[0], sorted(failure_rate, key=lambda x: -x[1])))