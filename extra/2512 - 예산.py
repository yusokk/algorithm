N = int(input())
requests = list(map(int, input().split()))
M = int(input())

lo, hi = 1, max(requests)

best = 0
answer = 0
while lo <= hi:
    mid = (lo+hi) // 2
    total = 0
    for req in requests:
        total += (req if req <= mid else mid)

    if total <= M:
        if total >= best:
            best = total
            if mid > answer:
                answer = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)