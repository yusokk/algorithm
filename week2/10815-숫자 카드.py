import sys
sys.stdin = open("../test/num-card.txt", "r")

_ = int(input())
N = sorted(map(int, input().split()))
_ = int(input())
M = map(int, input().split())

def binary(n, l, start, end):
    if end < start:
        return 0
    mid = (start + end) // 2
    if n == l[mid]:
        return 1
    elif n < l[mid]:
        return binary(n, l, start, mid-1)
    else:
        return binary(n, l, mid+1, end)

dic_m = {}
for m in M:
    dic_m[m] = binary(m, N, 0, len(N)-1)
print(" ".join(str(dic_m[m]) for m in dic_m))