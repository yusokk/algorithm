N = int(input())
star_list = [''] * N


def make_star(n, row):
    if n // 3 == 1:
        star_list[row] += '***'
        star_list[row+1] += '* *'
        star_list[row+2] += '***'
        return
    else:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    for k in range(n//3):
                        star_list[row+(i*(n//3))+k] += ' ' * (n//3)
                else:
                    make_star(n//3, row+(i*(n//3)))


make_star(N, 0)
for i in range(N):
    print(star_list[i])