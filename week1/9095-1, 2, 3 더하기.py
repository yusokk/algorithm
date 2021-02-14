import sys
sys.stdin = open("../test/2.txt", "r")

test_num = int(input())
test_list = list()

for i in range(test_num):
    temp = int(input())
    test_list.append(temp)

def plus_to_3(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        num = plus_to_3(n-1) + plus_to_3(n-2) + plus_to_3(n-3)
    return num

for i in test_list:
    ans = plus_to_3(i)
    print(ans)