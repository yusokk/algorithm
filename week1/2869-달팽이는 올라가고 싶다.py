import math
test_num = list(map(int, input().split()))
a = test_num[0]
b = test_num[1]
v = test_num[2]

ans = math.ceil((v-a)/(a-b)+1)
print(ans)