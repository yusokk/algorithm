test_num = int(input())
test_list = list()
for i in range(test_num):
    string = input()
    if string not in test_list:
        test_list.append(string)

test_list = sorted(sorted(test_list, key=str.lower), key=len)

for index in range(len(test_list)):
    print(test_list[index])