import sys
K, N = list(map(int, sys.stdin.readline().split()))
K_list = list()
for _ in range(K):
    temp = int(sys.stdin.readline())
    K_list.append(temp)

max_K = max(K_list)
previous = 0

def cut_lan():
    p1 = 0
    p2 = max_K
    while True:
        cut_num = 0
        cut = (p1+p2)//2
        if cut == 0:
            cut = 1
        for k in K_list:
            cut_num += k // cut
        if p2 <= p1:
            if N <= cut_num:
                return cut
            else:
                return cut-1
        if N <= cut_num:
            p1 = cut + 1
        else:
            p2 = cut - 1

ans = cut_lan()
print(ans)