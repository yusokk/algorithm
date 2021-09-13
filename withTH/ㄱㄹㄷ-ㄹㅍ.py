n = int(input())

ropes = sorted(int(input()) for _ in range(n))

max_weight = 0
for i in range(n):
    current = ropes[i] * (n-i)
    if max_weight < current:
        max_weight = current

print(max_weight)