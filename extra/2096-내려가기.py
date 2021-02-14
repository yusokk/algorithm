import sys
read = sys.stdin.readline
n = int(read())

dp = [0, 0, 0, 0, 0, 0]


def down(n):
    a, b, c = map(int, read().rstrip().split())
    dp = [a, a, b, b, c, c]
    for i in range(1, n):
        a, b, c = map(int, read().rstrip().split())
        max_for_1 = max(dp[:4])
        min_for_1 = min(dp[:4])
        max_for_2 = max(dp)
        min_for_2 = min(dp)
        max_for_3 = max(dp[2:])
        min_for_3 = min(dp[2:])

        dp = [a+max_for_1, a+min_for_1, b+max_for_2, b+min_for_2, c+max_for_3, c+min_for_3]
    return [max(dp), min(dp)]

print(*down(n))