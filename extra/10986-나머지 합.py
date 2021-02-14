import sys
from itertools import accumulate
from math import comb

read = sys.stdin.readline
n, m = map(int, read().split())
rests = tuple(map(lambda x: (x % m), accumulate(map(int, read().split()))))
rest_dic = dict()

for rest in rests:
    if rest not in rest_dic:
        rest_dic[rest] = 1
    else:
        rest_dic[rest] += 1
answer = 0
if rest_dic.get(0, 0):
    answer += rest_dic[0]
for v in rest_dic.values():
    if v >= 2:
        answer += comb(v, 2)

print(answer)