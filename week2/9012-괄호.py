import sys
sys.stdin = open("../test/parenthesis2.txt", "r")
T = int(sys.stdin.readline())
ps_list = list()

for _ in range(T):
    temp = sys.stdin.readline()
    ps_list.append(temp)
stk_list = list()

for ps in ps_list:
    for i in range(len(ps)-1):
        if ps[i] == "(":
            stk_list.append(1)
        else:
            if stk_list:
                stk_list.pop()
            else:
                print("NO")
                break
    else:
        if stk_list:
            print("NO")
        else:
            print("YES")
    stk_list.clear()