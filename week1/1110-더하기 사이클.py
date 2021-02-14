num = int(input())
count = 0
def make_num(n, origin, count):
    count += 1
    str_n = str(n)
    if n < 10:
        idx0 = "0"
        idx1 = str_n
    else:
        idx0 = str_n[0]
        idx1 = str_n[1]
    new_idx1_num = int(idx0) + int(idx1)
    new_idx1 = str(new_idx1_num)[-1]
    new_num = int(idx1 + str(new_idx1))
    if new_num != origin:
        count = make_num(new_num, origin, count)
    return count
ans = make_num(num, num, count)
print(ans)