import sys
import copy
sys.setrecursionlimit(10**9)

row = int(input())
area = list()
count_list = list()
max_list = list()

for i in range(row):
    temp = list(map(int, input().split()))
    max_list.append(max(temp))
    area.append(temp)

max_height = max(max_list)
count = 0
flag =list()
for _ in range(row):
    flag.append(list(0 for i in range(row)))
def check(i, j):
    if area[i][j] > n and flag_record[i][j] == 0:
        flag_record[i][j] = count
        # for num in flag_record:
        #     print(num)
        #     print()
        # print("-"*20)
        if j+1 < row:
            check(i, j+1)
        if j-1 >= 0:
            check(i, j-1)
        if i+1 < row:
            check(i+1, j)
        if i-1 >= 0:
            check(i-1, j)

for n in range(0, max_height+1):
    flag_record = copy.deepcopy(flag)
    for i in range(row):
        for j in range(row):
            if area[i][j] > n and flag_record[i][j] == 0:
                count += 1
                check(i, j)
    count_list.append(count)
    # for i in flag_record:
    #     print(i)
    #     print()
    # print("-"*10)
    count = 0


max = max(count_list)
print(max)