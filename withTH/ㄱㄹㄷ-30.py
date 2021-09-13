n = input()

if '0' not in n:
    print(-1)
else:
    n_list = []
    for char in n:
        n_list.append(char)

    if sum(map(int, n_list)) % 3:
        print(-1)
    else:
        print(''.join(sorted(n_list, reverse=True)))
