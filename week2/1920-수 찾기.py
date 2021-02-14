import sys
sys.stdin = open("../test/find-num.txt", "r")
input_num1 = int(input())
origin_list = list(map(int, sys.stdin.readline().split()))
input_num2 = int(input())
new_list = list(map(int, sys.stdin.readline().split()))

origin_list.sort()
def binary_search(list, target, left, right):
    pl = left
    pr = right
    pc = (left+right) // 2
    if target == list[pc]:
        return 1
    else:
        if pl < pc:
            if target < list[pc]:
                return binary_search(list, target, pl, pc)
            else:
                return binary_search(list, target, pc, pr)
        else:
            if target == list[pr]:
                return 1
            else:
                return 0

for i in new_list:
    ans = binary_search(origin_list, i, 0, len(origin_list)-1)
    print(ans)