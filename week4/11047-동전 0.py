import sys
sys.stdin = open("../test/1.txt", "r")
read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
coins = [int(read()) for _ in range(N)]

def coins_need(n, k, coin_list):
    count = 0
    target = k
    for i in range(n-1, -1, -1):
        q, r = divmod(target, coin_list[i])
        count += q
        target = r
        if not target:
            break
    return count

print(coins_need(N, K, coins))