nums = input().split('-')

num_list = []
for num in nums:
    num_list.append(sum(map(int, num.split('+'))))

answer = num_list[0] - sum(num_list[1:] if len(num_list) > 1 else [])

print(answer)