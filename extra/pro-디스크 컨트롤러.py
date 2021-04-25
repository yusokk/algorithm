import heapq
def solution(jobs):
    answer = 0
    total = 0
    current = 0
    len_jobs = len(jobs)
    heap = []
    jobs.sort(reverse=True)

    def heappush():
        while jobs and jobs[-1][0] <= current:
            popped_job = jobs.pop()
            heapq.heappush(heap, (popped_job[1], popped_job[0]))
        if jobs and not heap:
            popped_job = jobs.pop()
            heapq.heappush(heap, (popped_job[1], popped_job[0]))

    while True:
        heappush()
        if not jobs and not heap: break
        current_job = heapq.heappop(heap)
        if current <= current_job[1]:
            total += current_job[0]
        else:
            total += current - current_job[1] + current_job[0]
        current += current_job[0]
    answer = total // len_jobs
    print(answer)
    return answer

solution([[0, 3], [1, 9], [2, 6]])