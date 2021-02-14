import sys
import heapq
read = sys.stdin.readline

n, k = map(int, read().rstrip().split())

jewelries = list(tuple(map(int, read().rstrip().split())) for _ in range(n))

knapsacks = list(int(read()) for _ in range(k))
knapsacks.sort(reverse=True)
jewelries.sort(reverse=True)
max_heap = []


def total_value():
    max_value = 0
    current_mass = 0

    while knapsacks:
        current_mass = knapsacks.pop()
        while jewelries:
            mass, value = jewelries[-1]
            if mass <= current_mass:
                jewelries.pop()
                heapq.heappush(max_heap, -value)
            else:
                break
        if max_heap:
            max_value -= heapq.heappop(max_heap)

    return max_value


print(total_value())