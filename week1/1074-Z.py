test_list = list(int(i) for i in input().split())
N = test_list[0]
r = test_list[1]
c = test_list[2]

def count(n, r, c):
    if n > 1:
        if 0 <= r < 2**(n-1):
            if 0 <= c < 2**(n-1):
                z_count = count(n-1, r, c)
            else:
                z_count = count(n-1, r, c-2**(n-1)) + 4**(n-1)
        else:
            if 0 <= c < 2**(n-1):
                z_count = count(n-1, r-2**(n-1), c) + 4**(n-1)*2
            else:
                z_count = count(n-1, r-2**(n-1), c-2**(n-1)) + 4**(n-1)*3
    else:
        z_list = [[0,1],[2,3]]
        z_count = z_list[r][c]
    return z_count

ans = count(N, r, c)
print(ans)




test_list = list(int(i) for i in input().split())
N = test_list[0]
r = test_list[1]
c = test_list[2]

def z_list(n):
    if n > 1:
        last_rlist, last_clist = z_list(n-1)
        new_rlist = [0, 0, 2 ** (n - 1), 2 ** (n - 1)]
        new_clist = [0, 2 ** (n - 1), 0, 2 ** (n - 1)]
        rlist = append_new(new_rlist, last_rlist)
        clist = append_new(new_clist, last_clist)
    else:
        rlist = [0, 0, 1, 1]
        clist = [0, 1, 0, 1]
    return rlist, clist

def append_new(new_list, last_list):
    return_list = list()
    for X in new_list:
        for x in last_list:
            new_x = X + x
            return_list.append(new_x)
    return return_list

def z_explore(n, r, c):
    rlist, clist = z_list(n)
    for index in range(4**n):
        if rlist[index] == r and clist[index] == c:
            return index
ans = z_explore(N, r, c)
print(ans)