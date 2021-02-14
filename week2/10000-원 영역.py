import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("../test/o-area.txt", "r")
o_num = int(input())

stack = list()    # 괄호 넣어줄 스택
halves = list()   # 괄호(반원) 담아서 정렬할 리스트

# 원을 괄호로 쪼개서 스택에 넣어주는 과정
for _ in range(o_num):
    x, r = map(int, sys.stdin.readline().split())
    left = (x-r, 1, -r*2)                           # 좌표, 1: 왼쪽 괄호 0: 오른쪾 괄호, 지
    right = (x+r, 0, r*2)
    halves.append(left)
    halves.append(right)

halves.sort(key=lambda x: (x[0], x[1], x[2]))       # 0, 1, 2 인덱스 순으로 정렬름

count = 1
def inner(index):
    global count
    bigger = 0
    smaller = 0
    while index < len(halves):
        if halves[index][1] == 1:
            if bigger == 0:
                bigger = -halves[index][2]
                index += 1
            else:
                small, index = inner(index)
                smaller += small
        else:
            if smaller == bigger:
                count += 1
            count += 1
            index += 1
            return bigger, index

i=0
useless = 0
while i < len(halves):
    useless, i = inner(i)
print(count)
