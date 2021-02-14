import sys
sys.stdin = open("../test/sales.txt")

city_num = int(input())
city_list = list()
for i in range(city_num):
    city_list.append(list(int(i) for i in input().split()))

flag = list(False for i in range(city_num))
cost = 0
cost_list = list()

def move(fr, to, start):
    global cost
    flag[fr] = True
    cost += city_list[fr][to]
    if to == start:
        cost_list.append(cost)
    elif flag.count(False) == 1 and city_list[to][start] != 0:
        move(to, start, start)
    else:
        for next in range(city_num):
            if city_list[to][next] != 0 and flag[next] == False:
                move(to, next, start)
    flag[fr] = False
    cost = cost - city_list[fr][to]


for start in range(city_num):
    for to in range(city_num):
        if to != start and city_list[start][to] != 0:
            move(start, to, start)

min_path = min(cost_list)
print(min_path)