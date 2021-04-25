import heapq

def solution(scoville, K):
    answer = 0
    heap = scoville
    heapq.heapify(heap)
    first = heapq.heappop(heap)
    second = 0
    while first < K:
        if not heap: return -1
        second = heapq.heappop(heap)
        new_food = first + (second * 2)
        heapq.heappush(heap, new_food)
        first = heapq.heappop(heap)
        answer += 1
    return answer