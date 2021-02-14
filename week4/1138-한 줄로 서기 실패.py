import sys
read = sys.stdin.readline
n = int(read())
line = [0]*n
front_nums = list(map(int, read().rstrip().split()))

for i in range(n):
    if i == 0:
        line[front_nums[i]] = i+1
    else:
        k = 0
        count = 0
        for j in range(i):
            if line[j] == 0:
                count += 1
        plus = front_nums[i] - count
        while line[front_nums[i]+plus+k] != 0:
            k += 1
        line[front_nums[i]+k] = i+1

print(*line)

# 7 4 2 6 5 1 3
# 5 2 4 1 2 1 0