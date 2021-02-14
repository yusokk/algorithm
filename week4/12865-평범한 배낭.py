import sys
sys.stdin = open("../test/1.txt", "r")
read = sys.stdin.readline
N, K = map(int, read().rstrip().split())
cargo = [tuple(map(int, read().rstrip().split())) for _ in range(N)]
pack = []

for i in range(0, N+1):
    pack.append([])
    for j in range(0, K+1):
        if i == 0 or j == 0:
            pack[i].append(0)
        elif cargo[i-1][0] <= j:
            pack[i].append(
                max(pack[i-1][j],
                    cargo[i-1][1] + pack[i-1][j-cargo[i-1][0]]
            ))
        else:
            pack[i].append(pack[i-1][j])
for i in range(N+1):
    print(*pack[i])

print(pack[-1][-1])