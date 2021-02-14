import sys
sys.stdin = open("../test/hunter.txt", "r")

first_input = tuple(map(int, sys.stdin.readline().split()))
M = first_input[0] # 사대의 수
N = first_input[1] # 동물의 수
L = first_input[2] # 사정거리
m_list = sorted(map(int, sys.stdin.readline().split())) # 사대 위치 좌표들
count = 0

def binary(left, right):
    global count
    pl = 0
    pr = len(m_list)-1
    while True:
        pc = (pl+pr) // 2
        if left <= m_list[pc] <= right:
            count += 1
            break
        elif m_list[pc] < left:
            pl = pc + 1
        else:
            pr = pc - 1
        if pr < pl:
            break


for _ in range(N):
    temp = tuple(map(int, sys.stdin.readline().split()))
    if L - temp[1] >= 0:
        left = temp[0] - (L - temp[1])
        if left <= 0:
            left = 1
        right = temp[0] + (L - temp[1])
        if right > m_list[-1]:
            right = m_list[-1]
        binary(left, right)

print(count)