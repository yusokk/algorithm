# 정렬하고 앞에서부터 짧은 회의
# 더 늦게 시작하고 빨리끝나는 회의가 더 좋을 수도?
# 먼저 끝나면 그걸로 대체하면 되겠네

n = int(input())
meetings = list(tuple(map(int, input().split())) for _ in range(n))
meetings.sort(key=lambda x: (x[0], x[1]))

count = 0
end = 0
for meeting in meetings:
    if meeting[0] >= end:
        end = meeting[1]
        count += 1
    elif meeting[1] < end:
        end = meeting[1]

print(count)