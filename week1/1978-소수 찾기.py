test_num = int(input())
test_list = list(map(int,input().split()))

prime_numbers = [2, 3, 5, 7]

for n in range(10, 1000 + 1):
    for i in prime_numbers:
        if n % i == 0:
            break
    else:
        prime_numbers.append(n)

count = 0

for i in test_list:
    if i in prime_numbers:
        count += 1

print(count)