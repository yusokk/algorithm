# from sys import stdin
# stdin = open("../test/num-card2.txt", 'r')
#
# _ = stdin.readline()
# N = sorted(map(int, stdin.readline().split()))
# _ = stdin.readline()
# M = map(int, stdin.readline().split())
#
#
# def binary(arr, left, right, key):
#     if left > right:
#         return 0
#     med = (left+right) // 2
#     if arr[med] == key:
#         i, j = 1, 0
#         while med + i <= right:
#             if arr[med + i] == key:
#                 i += 1
#             else: break
#         while med - j >= left:
#             if arr[med - j] == key:
#                 j += 1
#             else: break
#         return i+j -1
#     elif arr[med] < key:
#         return binary(arr, med+1, right, key)
#     else:
#         return binary(arr, left, med-1, key)
#
#
# n_dic = {}
# for n in N:
#     left = 0
#     right = len(N)-1
#     if n not in n_dic:
#         n_dic[n] = binary(N, left, right, n)
#
# print(" ".join(str(n_dic[x]) if x in n_dic else "0" for x in M))


###########################################################################


from sys import stdin
stdin = open("../test/num-card2.txt", 'r')

_ = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
_ = stdin.readline()
M = list(map(int, stdin.readline().split()))
index, m_dic = 0, {}

for m in sorted(M):
    cnt = 0
    if m not in m_dic:
        while index < len(N):
            if N[index] == m:
                index += 1; cnt += 1
            elif N[index] < m:
                index += 1
            else: break
        m_dic[m] = cnt

print(" ".join(str(m_dic[m]) for m in M))