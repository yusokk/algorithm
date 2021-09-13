def explode(string, bomb):
    stack = []
    for c in string:
        stack.append(c)
        if c != bomb[-1]:
            continue

        for i in range(len(bomb)):
            if len(bomb) - i > len(stack) or stack[len(stack) - len(bomb) + i] != bomb[i]:
                break
        else:
            for _ in range(len(bomb)):
                stack.pop()

    return stack


def solution():
    origin_string = input()
    bomb = input()

    string = explode(origin_string, bomb)

    if not string:
        print('FRULA')
    else:
        print(''.join(string))


solution()