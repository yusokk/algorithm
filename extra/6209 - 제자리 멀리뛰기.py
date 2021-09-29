import sys
read = sys.stdin.readline

d, n, m = map(int, read().rstrip().split())
stones = list(int(read()) for _ in range(n))
stones.sort()

if not stones:
    print(d)
else:
    gaps = [stones[0]]
    for i in range(1, len(stones)):
            gaps.append(stones[i] - stones[i-1])
    gaps.append(d - stones[-1])

    lo = 0
    hi = d

    while lo <= hi:
        mid = (lo + hi) // 2
        count = 0
        last = 0

        for gap in gaps:
            if gap + last < mid:
                count += 1
                last += gap
            else:
                last = 0

        if count <= m:
            lo = mid + 1
        else:
            hi = mid - 1

    print(lo-1)