import copy
import sys
sys.stdin = open("../test/3.txt", "r")

q_num = int(input())
a_list = list()
p_list = list()

for _ in range(q_num):
    temp_list = input().split()
    a_list.append(temp_list)

for i in range(123, 988):
    temp_str = str(i)
    if temp_str[0] != temp_str[1] and temp_str[0] != temp_str[2] and temp_str[2] != temp_str[1]:
        if temp_str[0] != "0" and temp_str[1] != "0" and temp_str[2] != "0":
            p_list.append(temp_str)

def check(p):
    st_count = 0
    possible = str(p)
    if a == possible[0]: st_count += 1
    if b == possible[1]: st_count += 1
    if c == possible[2]: st_count += 1
    b_count = 0
    b_set = (possible[0], possible[1], possible[2])
    if a in b_set: b_count += 1
    if b in b_set: b_count += 1
    if c in b_set: b_count += 1
    b_count = b_count - st_count
    if int(strike) == st_count and int(ball) == b_count:
        return False
    else:
        return True


p_copy = copy.deepcopy(p_list)
for arr in a_list:
    p_list = copy.deepcopy(p_copy)
    num_to_check = arr[0]
    strike = arr[1]
    ball = arr[2]
    a = num_to_check[0]
    b = num_to_check[1]
    c = num_to_check[2]
    for p in p_list:
        if check(p):
            p_copy.remove(p)

ans = len(p_copy)
print(ans)