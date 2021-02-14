import sys
sys.stdin = open("../test/matrix.txt", "r")

def mul(n, matrix1, matrix2):
    result = [[0]*n for _ in range(n)]
    print(result)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000
    return result #곱해진 행렬을 리턴
# 2분할
def divide(n, b, matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return mul(n, matrix,matrix)
    else:
        temp = divide(n, b//2, matrix)
        # 제곱수가 2의 배수일 때
        if b % 2 == 0:
            return mul(n, temp, temp)
        # 제곱수가 홀수일 때
        else:
            return mul(n,mul(n, temp, temp), matrix)
# 입력
n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
result = divide(n, b, a)
for row in result:
    for num in row:
        print(num%1000, end=' ')
    print()
