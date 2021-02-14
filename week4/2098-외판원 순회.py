import sys
sys.stdin = open("../test/input.txt", "r")
read = sys.stdin.readline

N = int(read())
dp = [[0]*(1 << N) for _ in range(N)]
costs = [list(map(int, read().rstrip().split())) for _ in range(N)]
inf = sys.maxsize


def tsp(last: int, visited: bin):
    if visited == (1 << N) - 1:
        return costs[0][last] or inf

    if dp[last][visited] != 0:
        return dp[last][visited]

    temp = inf
    for city_from in range(N):
        if visited & (1 << city_from) == 0 and costs[city_from][last]:
            temp = min(temp, tsp(city_from, visited | (1 << city_from)) + costs[city_from][last])
    dp[last][visited] = temp
    return temp


tsp(0, (1 << 0))
print(dp[0][1 << 0])