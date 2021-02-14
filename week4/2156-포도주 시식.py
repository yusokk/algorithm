import sys
sys.stdin = open("../test/input.txt", "r")
read = sys.stdin.readline

n = int(read())
dp = []
for i in range(n):
    dp.append([])
dp[0].append(0)
input_0 = int(read())
dp[0].append([input_0, input_0])

for i in range(1, n):
    volume = int(read())
    pre_max = max(dp[i-1][0], dp[i-1][1][0], dp[i-1][1][1])
    dp[i].append(pre_max)
    dp[i].append([dp[i-1][0]+volume])
    dp[i][1].append(dp[i-1][1][0]+volume)

print(dp)

answer = max(dp[n-1][0], dp[n-1][1][0], dp[n-1][1][1])
print(answer)