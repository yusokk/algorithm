import sys
read = sys.stdin.readline

def prime_factorization(num):
    for i in range(2, num+1):
        while num % i == 0:
            num //= i
            print(i)
        if num == i:
            print(i)
            break

prime_factorization(int(read()))