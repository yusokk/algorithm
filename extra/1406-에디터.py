import sys
read = sys.stdin.readline


def editor(string, command):
    left = list(s for s in string)
    right = []
    for c in command:
        if c == "L":
            if left:
                right.append(left.pop())
        elif c == "D":
            if right:
                left.append(right.pop())
        elif c == "B":
            if left:
                left.pop()
        else:
            noob, p = c.split()
            left.append(p)
    ans = "".join(left) + "".join(right[::-1])
    print(ans)


s = read().rstrip()
n = int(read())
command = []
for i in range(n):
    command.append(read().rstrip())

editor(s, command)