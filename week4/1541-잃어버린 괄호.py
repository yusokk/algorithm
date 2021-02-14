equation = list(map(sum, list(map(int, nums.split("+")) for nums in input().split("-"))))
answer = equation[0]
for i in range(1, len(equation)):
    answer -= equation[i]
print(answer)