num_list = list()
for i in range(9):
    num = int(input())
    num_list.append(num)
max_val = max(num_list)
for index, value in enumerate(num_list):
    if value == max_val:
        print(value)
        print(index+1)
        break