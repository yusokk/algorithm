input_num = int(input())

num_list = list()
for i in range(input_num):
    input_list = input().split()
    sum_val = int(input_list[0]) + int(input_list[1])
    num_list.append(sum_val)

for i in num_list:
    print(i)