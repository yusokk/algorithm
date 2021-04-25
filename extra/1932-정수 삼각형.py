import sys
read = sys.stdin.readline


def find_max(top_floor):
    dp = []
    for i in range(top_floor):
        floor = list(map(int, read().rstrip().split()))
        last_dp = dp
        dp = []
        temp = [0]
        if i == 0: dp.append(floor[0])
        for j in range(i):
            if j == 0:
                dp.append(last_dp[j]+floor[j])
            else:
                temp.append(last_dp[j]+floor[j])
                dp.append(max(temp))
            if j == i-1:
                dp.append(last_dp[j]+floor[j+1])
            else:
                temp = []
                temp.append(last_dp[j]+floor[j+1])
    print(max(dp))


n = int(read())
find_max(n)