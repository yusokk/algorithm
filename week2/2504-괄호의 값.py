import sys
from collections import deque
import copy
# sys.stdin = open("../test/paren-val.txt", "r")
parens = input().strip()
dq = deque()
stack = list()

for i in range(len(parens)):
    dq.append(parens[i])

deq = copy.deepcopy(dq)


def check():
    while dq:
        temp = dq.popleft()
        if temp == "(" or temp == "[":
            stack.append(temp)
        else:
            if temp == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            else:
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
    if stack:
        return False
    return True


def calc():
    while deq:
        temp = deq.popleft()
        if temp == "(" or temp == "[":
            stack.append(temp)
        elif temp == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                stack.append(2)
            else:
                temp = stack.pop()
                while stack and stack[-1] != "(":
                    temp += stack.pop()
                stack.pop()
                stack.append(temp*2)
        else:
            if stack and stack[-1] == "[":
                stack.pop()
                stack.append(3)
            else:
                temp = stack.pop()
                while stack and stack[-1] != "[":
                    temp += stack.pop()
                stack.pop()
                stack.append(temp*3)
    return sum(stack)


if check():
    print(calc())
else: print(0)