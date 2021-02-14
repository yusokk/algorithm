import sys
sys.stdin = open("../test/input.txt", "r")
read = sys.stdin.readline

n = int(read())
dp = [[0]*n for _ in range(n)]
matrix = []
for i in range(n):
    r, c = map(int, read().rstrip().split())
    matrix.append([0]*i)
    matrix[i].append((r, c))


def calc_matrix(m1, m2):
    return m1[0]*m1[1]*m2[1]


for i in range(1, n):
    for k in range(n):
        if i + k < n:
            temp_list = []
            for m in range(1, n):
                if i+k-m >= k and i+k+1-m <= i+k:
                    if dp[k][i+k-m] and dp[i+k+1-m][i+k]:
                        temp_list.append(calc_matrix(matrix[k][i+k-m], matrix[i+k+1-m][i+k]) + dp[k][i+k-m] + dp[i+k+1-m][i+k])
                    elif dp[k][i+k-m] and not dp[i+k+1-m][i+k]:
                        temp_list.append(dp[k][i+k-m] + calc_matrix(matrix[k][i+k-m], matrix[i+k+1-m][i+k]))
                    elif not dp[k][i+k-m] and dp[i+k+1-m][i+k]:
                        temp_list.append(dp[i+k+1-m][i+k] + calc_matrix(matrix[k][i+k-m], matrix[i+k+1-m][i+k]))
                    else:
                        if i > 1:
                            continue
                        temp_list.append(calc_matrix(matrix[k][i+k-m], matrix[i+k+1-m][i+k]))
            dp[k][i+k] = min(temp_list)
            matrix[k].append((matrix[k][k][0], matrix[i+k][i+k][1]))

print(dp[0][-1])