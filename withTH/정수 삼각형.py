n = int(input())

dp = [0] * n

for i in range(n):
    current_layer = list(map(int, input().split()))
    last_dp = dp
    dp = [0] * n

    for j in range(i+1):
        if j > 0:
            last_max = max(last_dp[j], last_dp[j-1])
        else:
            last_max = last_dp[j]
        dp[j] = last_max + current_layer[j]

print(max(dp))