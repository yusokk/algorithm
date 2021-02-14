import sys

number = int(sys.stdin.readline())
test_list = list()
for num in range(number):
    test_num = int(sys.stdin.readline())
    test_list.append(test_num)

prime_numbers = [2, 3, 5, 7]

for n in range(10, max(test_list) + 1):
    for i in prime_numbers:
        if n % i == 0:
            break
    else:
        prime_numbers.append(n)


for n in test_list:
    ans_list = list()
    min_val = n
    min_list = None

    for i in prime_numbers:
        if i + i > n:
            break
        for j in prime_numbers:
            if i + j == n:
                if i <= j:
                    ans_list.append([i, j])
                else:
                    ans_list.append([j, i])
            elif i + j > n:
                break
    for index in range(len(ans_list)):
        if ans_list[index][1] - ans_list[index][0] < min_val:
            min_list = list(map(str, ans_list[index]))
    print(" ".join(min_list))