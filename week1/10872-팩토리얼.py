test_num = int(input())

def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

ans = factorial(test_num)
print(ans)