N, R, C = map(int, input().split())


def z(n, r, c):
    ret = 0
    if n == 1:
        ret = 2*r + c
        return ret

    is_prev_r, prev_r = divmod(r, 2**(n-1))
    is_prev_c, prev_c = divmod(c, 2**(n-1))
    if is_prev_r:
        ret += 2**((n-1)*2) * 2
    if is_prev_c:
        ret += 2**((n-1)*2)

    ret += z(n-1, prev_r, prev_c)

    return ret


answer = z(N, R, C)
print(answer)

