import sys
read = sys.stdin.readline


def decimal(n):
    ans = 0
    if n[0] != "0":
            ans = int(n)
    elif n[1] != "x":
        for i in range(1, len(n)):
            if int(n[i]):
                ans += 8**(len(n)-i-1) * int(n[i])
    else:
        ans = int(n, 16)
    print(ans)


n = read().rstrip()
decimal(n)