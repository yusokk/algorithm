import sys
read = sys.stdin.readline

n, m = map(int, read().rstrip().split())
nums = list(map(int, read().rstrip().split()))

psum = [0]
for i in range(n):
    psum.append(nums[i]+psum[i])

for _ in range(m):
    i, j = map(int, read().rstrip().split())
    answer = psum[j] - psum[i-1]
    print(answer)