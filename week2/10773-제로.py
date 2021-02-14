import sys
sys.stdin = open("../test/zero2.txt", "r")
K = int(sys.stdin.readline())
k_list = list()
for _ in range(K):
    k = int(sys.stdin.readline())
    if k != 0:
        k_list.append(k)
    else:
        k_list.pop()

sum_k = sum(k_list)
print(sum_k)