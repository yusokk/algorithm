from itertools import permutations

n = int(input())
nums = map(int, input().split())

perms = permutations(nums)

answer = 0
for perm in perms:
    last = perm[0]
    sum_diff = 0

    for i in range(1, n):
        sum_diff += abs(perm[i] - last)
        last = perm[i]

    if answer < sum_diff:
        answer = sum_diff

print(answer)