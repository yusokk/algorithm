user_dict = {}
result_str = ['님이 들어왔습니다.', '님이 나갔습니다.']


def encode(record):
    ENTER = 0
    LEAVE = 1
    results = []

    for query in record:
        split_query = query.split(' ')

        if len(split_query) == 2:
            cmd, user_id = split_query
        else:
            cmd, user_id, user_name = split_query

        if cmd == 'Enter':
            if not user_dict.get(user_id):
                user_dict[user_id] = user_name
            elif user_dict[user_id] != user_name:
                user_dict[user_id] = user_name
            results.append([ENTER, user_id])
        elif cmd == 'Leave':
            results.append([LEAVE, user_id])
        else:
            user_dict[user_id] = user_name

    return results


def decode(result):
    return user_dict[result[1]] + result_str[result[0]]


def solution(record):
    results = encode(record)
    answer = list(map(decode, results))

    return answer