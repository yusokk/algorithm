def to_second(string_time):
    split_int = list(map(int, string_time.split(':')))
    return split_int[0] * 3600 + split_int[1] * 60 + split_int[2]


def solution(play_time, adv_time, logs):
    play_second = to_second(play_time)
    check = list(0 for _ in range(play_second + 1))
    starts = []
    ends = []

    for log in logs:
        split_log = log.split('-')
        time = list(map(to_second, split_log))
        starts.append(time[0])
        ends.append(time[1])
        print(time)

    starts.sort(reverse=True)
    ends.sort(reverse=True)

    t = starts[-1]
    current = 0

    while starts and ends and t <= play_second:
        while starts and starts[-1] == t:
            starts.pop()
            current += 1
        while ends and ends[-1] == t - 1:
            ends.pop()
            current -= 1
        check[t] = current
        t += 1

    adv_second = to_second(adv_time)
    max_time = sum(check[0:adv_second])
    current_time = max_time
    start_sec = 0

    i = adv_second + 1
    while i < play_second + 1:
        current_time = current_time - check[i - (adv_second + 1)] + check[i]
        print(current_time, max_time)
        if current_time > max_time:
            max_time = current_time
            start_sec = i - adv_second
        i += 1

    hour = '0' + str(start_sec // 3600)
    minute = '0' + str((start_sec % 3600) // 60)
    second = '0' + str(start_sec % 60)
    answer = [hour[-2:], minute[-2:], second[-2:]]

    return ':'.join(answer)

solution("02:03:55",	"00:14:15",	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])