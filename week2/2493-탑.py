num = int(input())
towers = list(map(int, input().split()))

stack = list()
ans_list = list()
t_dic = {}

for index in range(len(towers)):
    t_dic[towers[index]] = index+1
    if stack:
        if stack[-1] > towers[index]:
            ans_list.append(t_dic[stack[-1]])
            stack.append(towers[index])
        else:
            while True:
                if stack[-1] < towers[index]:
                    stack.pop()
                    if not stack:
                        stack.append(towers[index])
                        ans_list.append(0)
                        break
                else:
                    ans_list.append(t_dic[stack[-1]])
                    stack.append(towers[index])
                    break
    else:
        stack.append(towers[index])
        ans_list.append(0)

print(*ans_list)