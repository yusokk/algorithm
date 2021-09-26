def solution(n, times):
    times.sort()
    MAX = times[-1] * n

    lo, hi = 1, MAX
    while lo <= hi:
        time = (lo + hi) // 2

        count = 0
        for t in times:
            if t > time:
                break
            count += time // t

        if count >= n:
            hi = time - 1
        else:
            lo = time + 1

    answer = lo

    return answer