import sys
sys.stdin = open("../test/1.txt", "r")
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N = int(read())
    count = 0
    newcomers = []
    for _ in range(N):
        newcomers.append(tuple(map(int, read().rstrip().split())))
    newcomers.sort()
    criteria = newcomers[0][1]
    for newcomer in newcomers:
        if newcomer[1] <= criteria:
            count += 1
            criteria = newcomer[1]
    print(count)