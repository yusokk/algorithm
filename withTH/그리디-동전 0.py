n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))

answer = 0
while coins:
    current = coins.pop()

    if k >= current:
        answer += k // current
        k %= current

    if not k:
        break

print(answer)