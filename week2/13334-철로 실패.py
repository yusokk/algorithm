import sys
import heapq
sys.stdin = open("../test/rail.txt", "r")
n = int(input())
houses =[]

for _ in range(n):
    temp = sorted(map(int, sys.stdin.readline().split()))
    houses.append(temp)

left_sorted = sorted(houses)
lefts = list()
for left in left_sorted:
    if left[0] not in lefts:
        lefts.append(left[0])
houses.sort(key=lambda x: x[1])
length = int(input())
max_house = 0

heap = []
temp = list()
for index in range(n):
    heapq.heappush(heap, (houses[index][1], houses[index][0]))

count = 0
max_n = 0
for left in lefts:
    while temp:
        pop = temp.pop()
        if pop[1] >= left:
            heapq.heappush(heap, pop)
    end = left + length
    while heap[0][0] <= end:
        popped = heapq.heappop(heap)
        if popped[1] >= left:
            temp.append(popped)
            count = len(temp)
        if not heap: break
    max_n = max(max_n, count)
    count = 0

print(max_n)