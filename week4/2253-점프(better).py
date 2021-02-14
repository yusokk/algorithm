import sys
sys.stdin = open("../test/input.txt", "r")
read = sys.stdin.readline
inf = sys.maxsize
N, M = map(int, read().rstrip().split())
small_stones = [0] * (N+1)
for _ in range(M):
    small_stones[int(read())] = 1
dp = [[inf]*161 for _ in range(N+1)]


def jump():
    dp[2][1] = 1
    dp[2][2] = 1
    for i in range(3, N+1):
        for j in range(1, 160):
            if i - (j-1) <= 0: continue
            if not small_stones[i]:
                dp[i][j] = min(dp[i-(j-1)][j-1], dp[i-j][j], dp[i-(j+1)][j+1]) + 1


jump()
result = min(dp[N])
print(result if result < inf else -1)