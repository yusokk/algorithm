import sys
sys.stdin = open("../test/sort3.txt", "r")

test_num = int(input())
num_list = [0]*10001

for i in range(test_num):
    num_list[int(sys.stdin.readline())-1] += 1

for index in range(len(num_list)):
    num = num_list[index]
    if num > 0:
        for i in range(num):
            print(index+1)