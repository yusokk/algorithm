def solution(stones, k):
    start = 1
    end = 200000000
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for stone in stones:
            if stone <= mid:
                count += 1
                if count == k:
                    end = mid - 1
                    break
            else:
                count = 0
        else:
            start = mid + 1
    answer = start

    return answer