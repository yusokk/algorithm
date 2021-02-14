import sys
read = sys.stdin.readline

dp = []
n = int(read())
first_step = int(read())

# dp[계단번호-1][점수] -> 두번째 index 0: 안밟는 경우, 1: 밟고 전에껀 안밟았던 경우, 2: 밟고 전 계단도 밟았던 경우
dp.append([0, first_step, first_step])

for i in range(1, n):
    current_step = int(read())
    dp.append([max(dp[i-1][1], dp[i-1][2])])
    dp[i].append(dp[i-1][0] + current_step)
    dp[i].append(dp[i-1][1] + current_step)

print(max(dp[n-1][1], dp[n-1][2]))