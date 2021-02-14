import sys
sys.setrecursionlimit(10**5)

N = int(input())
def possible_num(n):
    x, y = 1, 2
    for _ in range(1, N):
        x, y = y % 15746, (x + y) % 15746
    return x

print(possible_num(N))