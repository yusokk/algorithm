import sys
read = sys.stdin.readline

n = int(read())
nums = read().rstrip()

ans = 0
for i in range(len(nums)):
    ans += int(nums[i])

print(ans)