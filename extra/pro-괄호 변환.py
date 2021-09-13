def split(str):
    open_p, close_p = 0, 0

    for idx in range(len(str)):
        if str[idx] == '(':
            open_p += 1
        else:
            close_p += 1

        if open_p == close_p:
            u = str[:idx + 1]
            v = str[idx + 1:]

            return [u, v]
    return [str, '']


def check_u(u):
    stack = []
    for p in u:
        if not stack:
            if p == ')':
                return False
            stack.append(p)
            continue

        if stack[-1] != p:
            stack.pop()
        else:
            stack.append(p)

    if stack:
        return False
    else:
        return True


def process(u, v):
    if check_u(u):
        return u + process(*split(v)) if split(v)[0] else u
    else:
        new_str = '('
        new_str += process(*split(v)) + ')' if split(v)[0] else ')'
        trans_table = u[1:-1].maketrans('()', ')(')
        return new_str + u[1:-1].translate(trans_table)


def solution(p):
    if not p:
        return p

    return process(*split(p))

print(solution("(()())()") == "(()())()")
print(solution(")(") == '()')
print(solution("()))((()") == "()(())()")