import sys
from collections import deque
sys.stdin = open("../test/input.txt", "r")
read = sys.stdin.readline
# N: 멀티탭 구멍 수, K: 전기용품 총 사용횟수
N, K = map(int, read().rstrip().split())
# 전기용품 사용 순서
use_order = tuple(map(int, read().rstrip().split()))
# 사용되는 순서를 순서대로 딕셔너리에 저장
count_dic = dict()
for i in range(len(use_order)):
    thing = use_order[i]
    if count_dic.get(thing, 0):
        count_dic[thing].append(i)
    else:
        count_dic[thing] = deque([i])
# 교환 횟수
count = 0
# 사용 되고 있는 제품 표시
now_use = dict()
# K-1 까지 인덱스 증가시키면서 확인
for i in range(K):
    now_thing = use_order[i]
    # 남는 구멍이 있으면 꽂는다.
    if len(now_use) < N:
        now_use[now_thing] = 1
        count_dic[now_thing].popleft()
    # 다 꽂혀 있으면 뒤에 누가 올지를 확인하고 판단해서 뺀다.
    else:
        # 만약 이미 꽂혀있으면 통과
        if now_use.get(now_thing, 0):
            count_dic[now_thing].popleft()
        # 꽂혀 있는 것 중 가장 늦게 나오는 것을 빼준다.
        else:
            temp = []
            for key, value in now_use.items():
                if value:
                    if count_dic[key]:
                        temp.append((count_dic[key][0], key))
                    else:
                        temp.append((101, key))
            del_key = max(temp)[1]
            now_use[del_key] = 0
            now_use[now_thing] = 1
            count_dic[now_thing].popleft()
            count += 1

print(count)