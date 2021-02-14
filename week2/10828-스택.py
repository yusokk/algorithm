import sys
sys.stdin = open("../test/stack.txt", "r")
num = int(sys.stdin.readline())
com_list = list()
for _ in range(num):
    temp = sys.stdin.readline()
    com_list.append(temp)

stk_list = []

def command(string):
    if string[:4] == "push":
        push_list = string.split()
        stk_list.append(int(push_list[1]))
    elif string[:3] == "pop":
        if stk_list:
            pop_num = stk_list.pop()
            print(pop_num)
        else:
            print(-1)
    elif string[:4] == "size":
        print(len(stk_list))
    elif string[:3] == "top":
        if stk_list: print(stk_list[-1])
        else: print(-1)
    else:
        if stk_list: print(0)
        else: print(1)

for com in com_list:
    command(com)