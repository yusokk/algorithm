import sys
read = sys.stdin.readline
# import math

# 무식한 방법
# def find_generator(n):
#     sum_dic = dict()
#     m = math.ceil(math.log(n, 10))
#     for i in range(m):
#         for j in range(10**i, 10**(i+1)):
#             temp = j
#             val = j
#             for k in range(i, -1, -1):
#                 q = temp // 10**k
#                 val += q
#                 temp -= q * 10**k
#             if val not in sum_dic:
#                 sum_dic[val] = j
#     if n in sum_dic:
#         print(sum_dic[n])
#     else:
#         print(0)
#
# n = int(read())
# find_generator(n)

def find_generator(n):
    range_cut = len(n) * 9
    num = int(n)
    for i in range(max(1, num - range_cut), num):
        string = str(i)
        if i + sum(int(s) for s in string) == num:
            print(i)
            break
    else:
        print(0)


n = read().rstrip()
find_generator(n)