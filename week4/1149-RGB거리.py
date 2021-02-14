import sys
sys.stdin = open("../test/input.txt", "r")
read = sys.stdin.readline

n = int(read())
costs = list(list(map(int, read().rstrip().split())) for _ in range(n))
dp = list()
dp.append(costs[0])
for i in range(1, n):
    dp.append([])
    for k in range(3):
        new_cost = min(dp[i-1][(k+1) % 3], dp[i-1][(k+2) % 3]) + costs[i][k]
        dp[i].append(new_cost)

print(min(dp[n-1]))