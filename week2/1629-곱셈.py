import sys
# sys.stdin = open("../test/multiply.txt", "r")

input_nums = list(map(int, input().split()))

A = input_nums[0]
B = input_nums[1]
C = input_nums[2]

def calc(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a % c
    if b % 2:
        r = (calc(a, b//2, c) ** 2) * a
    else: r = calc(a, b//2, c) ** 2
    return r % c

ans = calc(A, B, C)
print(ans)

print(A**B % C)