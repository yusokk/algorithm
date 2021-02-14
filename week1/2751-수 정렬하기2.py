test_num = int(input())
test_list = list()
for i in range(test_num):
    num = int(input())
    test_list.append(num)

test_list.sort()
for i in test_list:
    print(i)