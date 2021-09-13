import sys
read = sys.stdin.readline
test = int(read())


def solution():
    n = int(read())
    newbies = list(tuple(map(int, read().rstrip().split())) for _ in range(n))
    newbies.sort()

    count = 0
    cut_line = newbies[0][1]
    for newbie in newbies:
        if newbie[1] <= cut_line:
            count += 1
            cut_line = newbie[1]

    print(count)
    

for _ in range(test):
    solution()