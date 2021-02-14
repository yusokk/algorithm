test_num = int(input())
test_list = list()
for i in range(test_num):
    input_num = int(input())
    test_list.append(input_num)

temp_list = list(None for i in range(2001))
for i in test_list:
    temp_list[i + 1000] = i

ans_list = list()
for i in temp_list:
    if i is not None:
        ans_list.append(i)

for i in ans_list:
    print(i)