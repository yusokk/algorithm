import sys
# sys.stdin = open("../test/make-max.txt", "r")

N, K = map(int, input().split())
string = input()
count = 0

stack = list()
for i in range(len(string)):
    if not stack:
        stack.append(int(string[i]))
    else:
        while True:
            if stack[-1] < int(string[i]) and count < K:
                stack.pop()
                count += 1
                if not stack:
                    stack.append(int(string[i]))
                    break
            else:
                stack.append(int(string[i]))
                break

while count < K:
    stack.pop()
    count += 1


print("".join(map(str, stack)))