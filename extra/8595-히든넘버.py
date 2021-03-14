import sys
read = sys.stdin.readline

# ascii 65 = A

def make_sum(string):
    first = 0
    last = 0
    ans = 0
    while last < len(string):
        if ord(string[last]) < 65:
            first = last
            while ord(string[last]) < 65:
                last += 1
                if last == len(string):
                    break
            ans += int(string[first: last])
        last += 1
        if last == len(string):
            break
    print(ans)

noob = read()
s = read().rstrip()
make_sum(s)

# 개멋있다...

# from sys import stdin
# input = stdin.readline
#
# n = int(input())
# a = input().rstrip()
#
# for x in range(26):
#     a = a.replace(chr(ord('a') + x), ' ')
#     a = a.replace(chr(ord('A') + x), ' ')
#
# res = 0
#
# for x in a.split():
#     res += int(x)
#
# print(res)