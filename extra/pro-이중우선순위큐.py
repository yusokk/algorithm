import heapq

def solution(operations):
    lo, hi = [], []
    check = {}
    count = 0

    for o in operations:
        o = o.split(' ')
        cmd = o[0]
        n = int(o[1])

        if cmd == 'I':
            heapq.heappush(lo, n)
            heapq.heappush(hi, -n)
            if not check.get(n, 0):
                check[n] = 0
            check[n] += 1
            count += 1
        else:
            if count == 0:
                continue

            if n > 0:
                while not check.get(-hi[0]):
                    heapq.heappop(hi)
                pop = -heapq.heappop(hi)
            else:
                while not check.get(lo[0]):
                    heapq.heappop(lo)
                pop = heapq.heappop(lo)

            check[pop] -= 1
            count -= 1

    if not count:
        answer = [0, 0]
    else:
        while not check.get(-hi[0]):
            heapq.heappop(hi)
        while not check.get(lo[0]):
            heapq.heappop(lo)
        answer = [-heapq.heappop(hi), heapq.heappop(lo)]

    return answer