# 시간이 작은 사람을 앞으로
n = int(input())
times = sorted(map(int, input().split()))

answer = 0
for i in range(n):
    answer += times[i] * (n-i)

print(answer)