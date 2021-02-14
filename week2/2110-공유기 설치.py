N, C = map(int, input().split())

array = []
for _ in range(N):
    array.append(int(input()))
array.sort()  # 집의 좌표 오름차순으로 정렬

# pl, pr = 최소거리, 최대거리로 받는다

pl = 1
pr = array[-1] - array[0]
answer = 0

while pl <= pr:
    gap = (pl + pr) // 2
    value = array[0]
    count = 1

    for i in range(1, N):
        if array[i] >= value + gap:
            value = array[i]
            count += 1

    if count >= C:
        pl = gap + 1
        answer = max(answer, gap)
    else:
        pr = gap - 1

print(answer)
