import sys
read = sys.stdin.readline


def get_count(A, B):
    a = map(int, A.split(" "))
    b = map(int, B.split(" "))
    set_dic = dict()
    for i in a:
        if set_dic.get(i, 0):
            set_dic[i] += 1
        else:
            set_dic[i] = 1
    for j in b:
        if set_dic.get(j, 0):
            set_dic[j] += 1
        else:
            set_dic[j] = 1
    ans = 0
    for val in set_dic.values():
        if val == 1:
            ans += 1
    print(ans)


noob = read()
A = read().rstrip()
B = read().rstrip()
get_count(A, B)