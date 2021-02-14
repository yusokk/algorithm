test_num = int(input())
for i in range(test_num):
    test_list = input().split()
    R = int(test_list[0])
    S = test_list[1]
    ans_list = list()
    for index in range(len(S)):
        rs = S[index]*R
        ans_list.append(rs)
    ans = "".join(ans_list)
    print(ans)