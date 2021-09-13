import heapq


def solution(n, k, cmd):
    answer = ''
    check_list = [0 for i in range(n)]
    top_q = list(-i for i in range(k))
    bottom_q = list(i for i in range(k, n))
    pop_stack = []

    heapq.heapify(top_q)
    heapq.heapify(bottom_q)

    for c in cmd:
        if c == 'C':
            target = heapq.heappop(bottom_q)
            pop_stack.append(target)
            check_list[target] = 1
            if not bottom_q:
                heapq.heappush(bottom_q, -heapq.heappop(top_q))

        elif c == 'Z':
            target = pop_stack.pop()
            if bottom_q[0] < target:
                heapq.heappush(bottom_q, target)
            else:
                heapq.heappush(top_q, -target)
            check_list[target] = 0

        else:
            c, cnt = c.split()
            cnt = int(cnt)
            if c == 'D':
                while cnt:
                    heapq.heappush(top_q, -heapq.heappop(bottom_q))
                    cnt -= 1
            else:
                while cnt:
                    heapq.heappush(bottom_q, -heapq.heappop(top_q))
                    cnt -= 1

    for check in check_list:
        if check:
            answer += 'X'
        else:
            answer += 'O'

    return answer
