import sys
sys.stdin = open("../test/stick2.txt", "r")
num = int(sys.stdin.readline())
height_list = []
for _ in range(num):
    temp = int(sys.stdin.readline())
    height_list.append(temp)

forward = height_list[-1]
stk_list = [forward]
for i in range(1, num):
    if height_list[num-1-i] > stk_list[-1]:
        stk_list.append(height_list[num-1-i])


can_see = len(stk_list)
print(can_see)