a = int(input())
b = int(input())

b_1 = b%10
b_10 = (b%100 - b%10) // 10
b_100 = b//100
first = a * b_1
second = a * b_10
third = a * b_100
fourth = first + second*10 + third*100

print(first)
print(second)
print(third)
print(fourth)