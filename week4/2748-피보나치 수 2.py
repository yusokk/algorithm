N = int(input())
dp = [0]*(N+1)

# 상향식(타뷸레이션)
def fibonacci(n):
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]#

# print(fibonacci(N))


# 하향식(메모이제이션)
def fibonacci2(n):
    if n <= 1:
        return n
    if dp[n]:
        return dp[n]
    dp[n] = fibonacci2(n-1) + fibonacci2(n-2)
    return dp[n]


# 변수 2개만 사용 공간 절약

def fib(n):
    x, y = 0, 1
    for i in range(N):
        x, y = y, x+y
    return x



print(fibonacci2(N))