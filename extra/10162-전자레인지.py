def min_push(t):
    a = 300
    b = 60
    c = 10
    count_a, count_b, count_c = 0, 0, 0
    count_a = t // a
    rest_t = t % a
    count_b = rest_t // b
    rest_t = rest_t % b
    count_c = rest_t // c
    if rest_t % c == 0:
        print(count_a, count_b, count_c)
    else:
        print(-1)


T = int(input())
min_push(T)