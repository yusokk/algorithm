num = int(input())
test_list = list()
for i in range(num):
    input_str = input()
    test_list.append(input_str)
count = 0
score = 0
for index in range(num):
    test_str = test_list[index]
    for i in range(len(test_str)):
        if test_str[i] == "O":
            score += 1 + count
            count += 1
        else:
            count = 0
    print(score)
    score = 0
    count = 0