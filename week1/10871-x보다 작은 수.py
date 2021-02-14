start = input().split()
N = int(start[0])
X = int(start[1])
input_list = input().split()
num_list = list()
for i in input_list:
    if int(i) < X:
        num_list.append(int(i))
for i in num_list:
    print(i, end=" ")